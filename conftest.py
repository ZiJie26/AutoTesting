from datetime import datetime

import pytest

from common.api_client import APIClient
from common.app_driver import *
from common.cancel_app_update import cancel_app_update
from common.database_utils import DatabaseUtils
from common.load_data_from_file import find_project_root
from common.logging_config import setup_logging
from common.web_driver import initialize_selenium_driver
from main import env_conf


@pytest.fixture(scope="function")
def web_driver():
    """
    初始化Selenium driver
    """
    driver = initialize_selenium_driver()

    yield driver

    # 关闭Selenium驱动
    driver.quit()


@pytest.fixture(scope="function")
def doc_driver():
    """
    初始化Appium driver，针对 doc 设备
    """
    app_port = env_conf["test_doc_port"]
    driver = initialize_appium_driver(app_port)
    cancel_app_update(driver)

    yield driver

    # 关闭Appium驱动
    close_app_gracefully(driver)
    safe_quit_driver(driver)


@pytest.fixture(scope="function")
def med_driver():
    """
    初始化Appium driver，针对 med 设备
    """
    app_port = env_conf["test_med_port"]
    driver = initialize_appium_driver(app_port)
    cancel_app_update(driver)

    yield driver

    # 关闭Appium驱动
    close_app_gracefully(driver)
    safe_quit_driver(driver)


# 使用 fixture 初始化 API 客户端
@pytest.fixture(scope="function")
def api_client_admin():
    """
    初始化api client，针对接口测试
    :return:
    """
    return APIClient(base_url=env_conf["admin_url"])


# 使用 fixture 初始化 API 客户端
@pytest.fixture(scope="function")
def api_client_op():
    """
    初始化api client，针对接口测试
    :return:
    """
    return APIClient(base_url=env_conf["op_url"])


@pytest.fixture(scope="module")
def db_connection():
    # 初始化数据库连接
    db_utils = DatabaseUtils()
    db_utils.connect()

    # 返回连接对象供测试用例使用
    yield db_utils.get_connection()

    # 测试结束后关闭连接
    db_utils.close()


logger = setup_logging()  # Initialize logging


# 定义命令行选项，允许用户指定日志文件保留的天数
def pytest_addoption(parser):
    """
    添加命令行选项 --log-retention，用于设置日志文件保留天数。

    :param parser: pytest 提供的解析器对象。
    """
    parser.addoption(
        "--log-retention",
        action="store",
        default="30",
        help="Number of days to retain log files.",
    )


def get_log_retention_days(config):
    """
    从配置中获取日志保留天数，默认为 30 天。

    :param config: pytest 配置对象。
    :return: 日志文件保留天数。
    """
    return int(config.getoption("--log-retention", default=30))  # 确保返回的是整数


def pytest_terminal_summary(config):
    """
    在测试完成后执行清理旧日志文件并打印测试摘要信息。

    :param config: pytest 配置对象。
    """
    log_dir = find_project_root() / 'output' / 'logs'
    retention_days = get_log_retention_days(config)

    # 清理旧日志文件
    now = datetime.now()
    for file in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file)
        try:
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - file_time).days > retention_days:
                os.remove(file_path)
                logger.info(f"Removed old log file: {file}")
        except Exception as e:
            logger.error(f"Error removing log file {file}: {e}")
    logger.info("=" * 100)


def pytest_runtest_logreport(report):
    """
    记录每个测试用例的结果到日志中。

    :param report: pytest 提供的测试报告对象。
    """
    if report.when == "call":
        if report.passed:
            logger.info(f"Test {report.nodeid} PASSED")
        elif report.failed:
            logger.error(f"Test {report.nodeid} FAILED")
            logger.error(f"Failure reason: {report.longrepr}")
        elif report.skipped:
            logger.warning(f"Test {report.nodeid} SKIPPED")


@pytest.fixture(autouse=True)
def log_test_details(request):
    logger.info(f"Running test: {request.node.name}")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 获取当前日期
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 设置报告目录为项目根目录下的 report 文件夹
    report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'latest'))

    # 如果目录不存在，则创建目录
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # 设置报告文件名
    report_path = os.path.join(report_dir, f"report_{date_str}.html")

    # 更新 pytest 的 addopts
    config.option.htmlpath = report_path

    # 获取当前文件所在目录的绝对路径，再上溯到项目根目录
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # 设置 Allure 报告目录路径为项目根目录下的 output/allure-results
    allure_results_dir = os.path.join(root_dir, 'output', 'allure-results')

    # 确保 allure 结果目录存在
    os.makedirs(allure_results_dir, exist_ok=True)

    # 将 --alluredir 参数更新为绝对路径
    config.option.allure_report_dir = allure_results_dir
