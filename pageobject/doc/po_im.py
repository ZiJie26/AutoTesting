from common.basepage import *


class IM(BasePage):
    def choose_first(self, doc_driver):
        self.driver = doc_driver
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("icon_huanzhe1")')  # 选择第一个患者
        time.sleep(1)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.View").instance(116)')
        time.sleep(2)

    def kaichufang_button(self, doc_driver):
        self.driver = doc_driver
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("开处方").instance(0)')  # 点击“开处方”按钮
