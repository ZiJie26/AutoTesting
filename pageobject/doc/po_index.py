from common.basepage import *
from pageobject.doc.po_chufang import ChuFang
from pagelocators.doc.pl_index import *


class PageIndex(ChuFang):
    def jie_wen_zhen(self, doc_driver):
        self.driver = doc_driver
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, jiewenzhen)

    def jie_tu_wen(self, doc_driver):
        """
        测试医生接收图文问诊的完整流程，包括：
        1. 进入图文问诊列表。
        2. 查看首个问诊的详情。
        3. 接诊并确认操作。

        :param doc_driver: pytest 提供的 Appium 驱动，用于控制应用的操作。
        """
        self.driver = doc_driver
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, tuwen)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, check_deteil)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, jiezhen)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, queding)

    def yong_yao_yu_ding_dan(self, doc_driver):
        """
        测试医生在应用中执行开处方的完整流程，包括：
        1. 点击进入详情页面。
        2. 执行滑动操作，填写处方信息。
        3. 生成处方。

        :param doc_driver: pytest 提供的 Appium 驱动，用于控制移动应用。
        """
        self.driver = doc_driver
        self.tap_by_relative_coordinates(400, 400)
        time.sleep(2)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, check_deteil)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, likekaichufang)
        time.sleep(3)
        self.driver.swipe(500, 1000, 500, 400, 500)  # 执行滑动操作
        self.find_and_click_edit_elements()  # 填写处方相关信息
        time.sleep(2)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, shengchengchufang)
        time.sleep(1)
