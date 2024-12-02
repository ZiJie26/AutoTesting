from common.basepage import *


class ChuFang(BasePage):
    def kai_chu_fang(self, doc_driver):
        self.driver = doc_driver
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("处方模板")')  # 选择处方模板
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("诊断").instance(0)')  # 选择诊断
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生成处方  ")')  # 生成处方
        time.sleep(2)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.View").instance(2)')
        time.sleep(2)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.View").instance(2)')

    def check_time(self, doc_driver):
        self.driver = doc_driver
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("首页").instance(0)')  # 返回首页
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("处方状态")')  # 进入处方状态
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("u-tab-item-1")')  # 点击刚开的方
        time.sleep(1)
        # 获取生成的处方时间
        date_time = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().textContains("2024-")').text
        print(date_time)
        return date_time

    def find_and_click_edit_elements(self):
        """
        为每个药品调整用法用量
        查找所有文本为"编辑"的元素，点击并执行后续操作
        """
        driver = self.driver
        selector = 'new UiSelector().text("编辑")'
        edit_elements = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, selector)

        print(f"总共找到 {len(edit_elements)} 个'编辑'元素")

        for i, element in enumerate(edit_elements, 1):
            try:
                # 等待元素可点击
                WebDriverWait(driver, 10).until(
                    expected_conditions.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("编辑").instance({i - 1})')
                    ))

                # 点击"编辑"元素
                element.click()
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)')
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")')
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(1)')
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")')
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(2)')
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")')
                self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("保存  ")')

                # 执行后续操作
                print(f"完成第 {i} 个'编辑'元素的所有操作")

                # 如果需要，可以在这里添加返回上一页的逻辑
                # driver.back()

            except Exception as e:
                print(f"处理第 {i} 个'编辑'元素时出错: {str(e)}")

        if not edit_elements:
            print("没有找到任何'编辑'元素")
