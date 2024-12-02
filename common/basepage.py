# 其他
import json
import time

import pyautogui
# appium相关
from appium.webdriver.common.appiumby import AppiumBy
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def trans_json(data):
    return json.dumps(data.json(), indent=4, ensure_ascii=False)


class BasePage():
    driver = None

    # @classmethod
    # def set_driver(cls, driver):
    #     if driver is None:
    #         raise ValueError("Driver must be initialized")
    #     cls.driver = driver

    def tap_by_relative_coordinates(self, rel_a: int, rel_b: int):
        """
        appium专用
        根据相对坐标点击屏幕上的某个位置
        请注意你获取坐标的设备分辨率应为1280x720
        :param rel_a: 横向坐标
        :param rel_b: 纵向坐标
        """
        # 获取当前屏幕大小
        screen_size = self.driver.get_window_size()
        width = screen_size["width"]
        height = screen_size["height"]

        # 录制的设备分辨率
        rec_a = 720
        rec_b = 1280

        # 计算点击位置的实际坐标
        x = rel_a / rec_a * width
        y = rel_b / rec_b * height

        # 使用 tap 进行点击操作
        self.driver.tap([(x, y)])

    def wait_for_element_show(self, by, value, timeout=10):
        """
        等待指定元素出现，并返回该元素。

        :param by: 定位策略，如 AppiumBy.ANDROID_UIAUTOMATOR、By.ID、By.XPATH等。
        :param value: 定位值，具体取决于所使用的定位策略，例如：
                      'new UiSelector().text("接问诊")' 对于 Android UI Automator，
                      '//*[@id="example"]' 对于 XPATH。
        :param timeout: 最长等待时间（秒），默认值为10秒。如果在此时间内未找到元素，将抛出 TimeoutException。
        :return: 找到的 WebElement 对象。如果元素在指定时间内未出现，则抛出 TimeoutException。
        """

        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((by, value))
        )

    def wait_for_elements_show(self, by, value, timeout=10):
        """
        等待指定多个元素出现，并返回这些元素的列表。

        :param by: 定位策略，如 AppiumBy.ANDROID_UIAUTOMATOR、By.ID、By.XPATH等。
        :param value: 定位值，具体取决于所使用的定位策略，例如：
                      'new UiSelector().text("接问诊")' 对于 Android UI Automator，
                      '//*[@class="example"]' 对于 XPATH。
        :param timeout: 最长等待时间（秒），默认值为10秒。如果在此时间内未找到任何元素，将抛出 TimeoutException。
        :return: 找到的 WebElement 对象列表。如果没有元素在指定时间内出现，则返回空列表。
        """

        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((by, value))
        )

    def wait_and_click(self, by, value, timeout=10):
        """
        等待元素出现并点击
        :param by: 定位策略，如 AppiumBy.ANDROID_UIAUTOMATOR
        :param value: 定位值，如 'new UiSelector().text("接问诊")'
        :param timeout: 最长等待时间（秒）
        """
        element = self.wait_for_element_show(by, value, timeout)
        element.click()

    # TODO: 改成持续滚动直到找到特定元素而不是文本
    def find_element_until_text(self, text, max_scrolls=10):
        """
        通过滚动页面，直到找到包含指定文本的元素或达到最大滚动次数。

        :param text: 要查找的元素的文本内容。
        :param max_scrolls: 最大滚动次数，默认为10次。在达到最大滚动次数之前，会持续查找该文本的元素。
        :return: 找到的 WebElement 对象。如果在最大滚动次数内未找到，返回 None。

        方法逻辑：
        1. 循环执行指定次数的滚动，每次检查页面上是否有包含指定文本的元素。
        2. 如果找到匹配的元素，立即返回该元素。
        3. 如果在最大滚动次数内未找到，输出信息并返回 None。

        注意：
        - 该方法假设页面的元素可以通过滚动加载。
        - 滚动操作的参数（起点和终点坐标）可以根据页面的布局进行调整。
        - 滚动后会等待1秒，以确保页面加载完毕。
        """
        for i in range(max_scrolls):
            elements = self.driver.find_elements(
                by=AppiumBy.ANDROID_UIAUTOMATOR,
                value=f'new UiSelector().text("{text}")',
            )
            if elements:
                print(f"Element with text '{text}' found!")
                return elements[0]
            else:
                print(
                    f"Element with text '{text}' not found. Scrolling... ({i + 1}/{max_scrolls})"
                )
                # 执行滚动操作
                self.driver.swipe(500, 1000, 500, 400, 500)
                time.sleep(1)

        print(f"Element with text '{text}' not found after {max_scrolls} scrolls.")
        return None

    # TODO: 把使用这个方法的改成使用wait for element show
    def wait_for_clickable(self, by_locator, timeout=10):
        """
        该方法已废除，不要使用！
        等待页面中的指定元素变为可点击状态，并返回该元素。

        :param by_locator: 元素的定位器，通常是一个元组，如 (By.ID, 'element_id')，用于定位页面上的元素。
        :param timeout: 等待的最长时间（秒），默认值为10秒。如果在指定时间内元素不可点击，将抛出 TimeoutException。
        :return: 找到的可点击的 WebElement 对象。

        说明：
        - 该方法使用 WebDriverWait 和 expected_conditions 来等待指定的元素变为可点击状态。
        - 如果元素在超时时间内变为可点击，则返回该元素，否则抛出 TimeoutException。
        - 适用于需要等待页面加载或动态内容更新，确保元素可交互时再执行点击操作。
        """
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(by_locator)
        )

    def hover_to_element(self, by, value):
        """
        将鼠标悬浮在指定的元素上。

        :param by: 定位元素的方式（如 'id', 'name', 'xpath' 等）。
        :param value: 定位元素的值，根据 'by' 参数用于精确定位目标元素。
        :return: 无返回值，但执行悬浮操作。

        方法逻辑：
        1. 根据给定的定位方式和值，找到需要悬浮的 Web 元素。
        2. 创建一个 ActionChains 对象，用于模拟鼠标操作。
        3. 将鼠标移动到该元素上，执行悬浮操作。
        4. 悬浮后等待2秒，以确保悬浮效果能够被观察到。

        注意：
        - 该方法会在执行悬浮后暂停2秒，便于观察效果或处理页面上的悬浮事件。
        - 该方法假设传入的定位方式和值能唯一定位到目标元素，否则会抛出异常。
        """
        # 找到要悬浮的元素
        element_to_hover = self.driver.find_element(by, value)
        # 创建ActionChains对象
        actions = ActionChains(self.driver)
        # 悬浮在元素上
        actions.move_to_element(element_to_hover).perform()
        time.sleep(2)

    @staticmethod
    def upload_file(path):
        """
        通过模拟键盘输入的方式上传指定路径的文件。

        :param path: 要上传文件的完整路径字符串。该路径应为可访问的文件路径。
        :return: 无返回值，但该方法会模拟输入路径并按下回车键。

        方法逻辑：
        1. 使用 pyautogui 库模拟键盘输入，将文件路径输入到上传对话框中。
        2. 模拟按下回车键以确认上传操作。

        注意：
        - 该方法假设上传对话框已打开并处于活动状态，确保键盘输入能正确传输。
        - 需要在运行此方法前确保 pyautogui 库已正确安装，并在适当的环境中运行。
        - 使用前请确认路径的正确性，以避免文件上传失败或错误。
        """
        pyautogui.typewrite(path)
        pyautogui.press("enter")
