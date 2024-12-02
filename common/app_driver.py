import os

from appium import webdriver as appium_webdriver
from appium.options.common import AppiumOptions
from selenium.common import WebDriverException

from main import env_conf


def initialize_appium_driver(app_port):
    """
    初始化 Appium 驱动，用于 Android 设备连接和自动化操作设置。

    :param app_port: 设备连接的端口号。
    :return: 配置完成的 Appium driver 实例。
    """
    if app_port == env_conf['test_doc_port']:
        print("Setting up Appium driver for doc")
    elif app_port == env_conf['test_med_port']:
        print("Setting up Appium driver for med")

    options = AppiumOptions()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:platformVersion", "12")
    options.set_capability("appium:deviceName", f"127.0.0.1:{app_port}")
    options.set_capability("appium:udid", f"127.0.0.1:{app_port}")
    options.set_capability("appium:appPackage", env_conf['appPackage'])
    options.set_capability("appium:appActivity", env_conf["appActivity"])
    options.set_capability("appium:systemPort", 8200)
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:noReset", True)
    options.set_capability("appium:ensureWebviewsHavePages", True)
    options.set_capability("appium:nativeWebScreenshot", True)
    options.set_capability("appium:newCommandTimeout", 3600)
    options.set_capability("appium:connectHardwareKeyboard", True)

    driver = appium_webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver


def close_app_gracefully(driver):
    """
    尝试关闭当前打开的应用，确保退出前先终止指定应用进程。

    :param driver: Appium driver 实例。
    """
    try:
        app_package = driver.capabilities.get("appPackage")
        if app_package:
            driver.terminate_app(app_package)
        else:
            print("Warning: Unable to find appPackage in capabilities")
    except Exception as e:
        print(f"Error terminating app: {e}")


def safe_quit_driver(driver):
    """
    安全地退出 Appium 驱动，若出现异常则使用强制退出。

    :param driver: Appium driver 实例。
    """
    try:
        if driver.session_id:
            driver.quit()
    except WebDriverException as e:
        print(f"WebDriverException during quit: {e}")
        force_stop_app(driver)
    except Exception as e:
        print(f"Unexpected error during quit: {e}")


def force_stop_app(driver):
    """
    在正常方法失败后强制停止应用进程。

    :param driver: Appium driver 实例。
    """
    try:
        app_package = driver.capabilities.get("appPackage")
        if app_package:
            os.system(f"adb shell am force-stop {app_package}")
        else:
            print("Warning: Unable to find appPackage in capabilities")
    except Exception as e:
        print(f"Error force stopping app: {e}")
