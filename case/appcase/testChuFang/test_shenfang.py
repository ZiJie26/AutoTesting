from datetime import datetime
from common.basepage import *  # 导入基类及通用方法


class TestShenfang(BasePage):
    """
    该类用于测试审方功能，通过定位并点击最新的时间元素，模拟审方操作。
    继承自 BasePage，包含通用页面操作方法。
    """

    def test_shenfang(self, med_driver):
        """
        测试审方的完整流程，包括：
        1. 点击进入指定位置进行审方操作。
        2. 通过滚动查找并点击时间最新的元素。

        :param med_driver: pytest 提供的 Appium 驱动，用于控制移动应用。
        """
        self.driver = med_driver
        time.sleep(5)
        self.tap_by_relative_coordinates(112, 835)  # 点击指定位置进入审方
        time.sleep(5)
        self.find_and_click_latest_element()  # 查找并点击最新的时间元素

        time.sleep(2)
        self.tap_by_relative_coordinates(531, 1230)  # 确认操作
        time.sleep(5)

    def find_and_click_latest_element(self):
        """
        在当前页面通过滚动查找时间最新的元素并点击，步骤如下：
        1. 获取当前可见的时间元素，判断时间格式是否正确。
        2. 记录所有时间元素并找到最新的时间。
        3. 滑动页面加载更多内容，直到找到最新的时间元素为止。
        4. 点击时间最新的元素。

        如果没有找到任何有效的时间元素，输出提示信息。
        """
        elements = []
        latest_element = None

        while True:
            visible_elements = self.wait_for_elements_show(AppiumBy.ANDROID_UIAUTOMATOR,
                                                           'new UiSelector().textContains("2024")')

            if not visible_elements:
                print("No elements found on current view.")
                break

            for element in visible_elements:
                time_text = element.text
                try:
                    element_time = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S")
                    elements.append((element, element_time))
                except ValueError:
                    print(f"Invalid time format for element: {time_text}")
                    continue

            current_latest_element = max(elements, key=lambda x: x[1])[0]

            if latest_element and current_latest_element.text == latest_element.text:
                self.driver.swipe(250, 900, 250, 500, 200)  # 滑动加载更多元素
                if latest_element and current_latest_element.text == latest_element.text:
                    print(f"Reached the bottom. Latest element found: {latest_element.text}")
                break

            latest_element = current_latest_element

            self.driver.swipe(250, 900, 250, 500, 200)  # 滑动加载更多元素

        if latest_element:
            print(f"Clicking on element with latest time: {latest_element.text}")
            latest_element.click()
        else:
            print("No elements found with valid time format.")
