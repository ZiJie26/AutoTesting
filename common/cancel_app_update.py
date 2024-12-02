import warnings

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from common.basepage import BasePage


class AppUpdateRequiredException(Exception):
    """自定义异常，用于标记需要热更新的情况"""
    pass


def cancel_app_update(driver):
    base_page = BasePage()
    base_page.driver = driver
    try:
        base_page.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")')
        warning_message = "APP需要热更新！"
        warnings.warn(warning_message, UserWarning)
        allure.attach(warning_message, name="APP需要热更新！", attachment_type=allure.attachment_type.TEXT)
        # 找到“取消”元素后引发自定义异常
        raise AppUpdateRequiredException(warning_message)
    except TimeoutException:
        # 如果元素不存在，不做任何操作
        pass
    except AppUpdateRequiredException as e:
        # 捕获自定义异常并将其附加到 Allure 报告中
        allure.attach(str(e), name="APP需要热更新！", attachment_type=allure.attachment_type.TEXT)
        # 重新引发异常以确保 Allure 将状态标记为 broken
        raise
