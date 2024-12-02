import os

from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.service import Service

from common.cleanup_utils import cleanup_reports
from common.load_data_from_file import find_project_root
from main import env_conf


def initialize_selenium_driver():
    """
    初始化selenium驱动；其中驱动路径存储在data/config/test_paths.json
    """
    chrome_testing_path = env_conf["chrome_testing_path"]
    chromedriver_path = env_conf["chromedriver_path"]
    chrome_user_data_dir = env_conf["chrome_user_data_dir"]

    options = selenium_webdriver.ChromeOptions()
    options.binary_location = chrome_testing_path
    options.add_experimental_option("detach", True)
    options.add_argument(f"user-data-dir={chrome_user_data_dir}")  # 读取用户配置文件来实现保存登陆数据
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(chromedriver_path)
    driver = selenium_webdriver.Chrome(service=service, options=options)
    vars = {"window_handles": driver.window_handles}

    reports_directory = os.path.join(find_project_root(), "output", "latest")
    cleanup_reports(reports_directory, days=7)  # 清除七天以前的报告文件
    return driver
