import time
from selenium.webdriver.common.by import By
from common.basepage import BasePage  # 导入基类


class TestMoBanSheZhi(BasePage):
    """
    该类用于测试“动态字典”功能的操作流程，继承自 BasePage。
    """

    def test_dongtai(self, web_driver):
        """
        测试在后台管理系统中添加“动态字典”记录的流程，包括以下步骤：
        1. 导航到指定页面并点击菜单和子菜单项。
        2. 选择特定树节点并进入添加配置页面。
        3. 输入字典相关信息，包括字典名称和类型。
        4. 提交并保存动态字典的配置。

        :param web_driver: pytest 提供的 WebDriver 实例，用于操作网页。
        """
        self.driver = web_driver
        self.driver.get("https://op-test.aidmed.net/hospital-operate/index")

        self.wait_for_clickable((By.CSS_SELECTOR, "div:nth-child(2) > .el-submenu span:nth-child(2)")).click()
        self.wait_for_clickable((By.CSS_SELECTOR, ".is-opened .nest-menu:nth-child(1) .el-menu-item")).click()
        self.wait_for_clickable(
            (By.XPATH, "//div[@class='el-tree']//div[@class='el-tree-node__content']/div[.='自动化测试专用']")).click()

        self.wait_for_clickable((By.CSS_SELECTOR, ".page-config-add span")).click()
        self.wait_for_clickable((By.CSS_SELECTOR, ".is-required:nth-child(1) .el-input__inner")).click()
        self.wait_for_clickable((By.XPATH, "//form/div/div/div/div/div/div/input")).send_keys("ceshi1")
        self.wait_for_clickable((By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(2) > .el-form-item__content > .el-input > .el-input__inner")).send_keys(
            "动态字典")

        self.wait_for_clickable((By.XPATH,
                                 "//div[@class='el-form-item is-required el-form-item--medium']//i[@class='el-select__caret el-input__icon el-icon-arrow-up']")).click()
        time.sleep(2)
        self.wait_for_clickable((By.XPATH, "//li[contains(.,'动态字典（Map）')]")).click()

        self.wait_for_clickable((By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary > span")).click()
        time.sleep(2)

    def test_fuwenben(self, web_driver):
        """
        测试添加富文本配置项的完整流程，具体步骤包括：
        1. 导航到指定配置页面。
        2. 选择自动化测试的树节点并进入添加页面。
        3. 输入相关信息，包括名称和类型。
        4. 在富文本编辑器中输入内容并提交。

        :param web_driver: pytest 提供的 WebDriver 实例，用于操作网页。
        """
        self.driver = web_driver
        self.driver.get("https://op-test.aidmed.net/hospital-operate/config-item/templates")

        # 选择“自动化测试专用”树节点
        self.wait_for_clickable(
            (By.XPATH, "//div[@class='el-tree']//div[@class='custom-tree-node']/div[.='自动化测试专用']")).click()

        # 点击“添加”按钮
        self.wait_for_clickable((By.CSS_SELECTOR, ".page-config-add > .el-button")).click()

        # 输入配置项名称和显示名称
        self.wait_for_clickable((By.XPATH,
                                 "//div[@class='el-col el-col-11']/div[@class='el-col el-col-24']/div[1]//input[@class='el-input__inner']")).send_keys(
            "autotest.ceshi3")
        self.wait_for_clickable((By.XPATH,
                                 "//div[@class='el-col el-col-11']//div[@class='el-form-item is-required el-form-item--medium']//div[@class='el-input el-input--small']/input[@class='el-input__inner']")).send_keys(
            "富文本")

        # 选择富文本类型
        self.wait_for_clickable((By.XPATH,
                                 "//div[@class='el-form-item is-required el-form-item--medium']//i[@class='el-select__caret el-input__icon el-icon-arrow-up']")).click()
        self.wait_for_clickable((By.XPATH, "//li[contains(.,'富文本')]")).click()

        # 点击富文本编辑器并输入内容
        self.wait_for_clickable((By.XPATH, "//div[@class='el-col el-col-11']//div[@class='w-e-scroll']/div[1]")).click()
        time.sleep(1)
        self.wait_for_clickable(
            (By.XPATH, "//div[@class='el-col el-col-11']//div[@class='w-e-scroll']/div[1]")).send_keys("ceshi")

        # 提交表单
        self.wait_for_clickable((By.XPATH,
                                 "//body[@class='el-popup-parent--hidden']/div[@class='el-dialog__wrapper']//button[@class='el-button el-button--primary el-button--medium']")).click()

        time.sleep(2)

    def test_jintai(self, web_driver):
        """
        测试添加静态字典配置项的完整流程，主要步骤包括：
        1. 导航到指定配置页面并选择特定节点。
        2. 输入配置项名称和显示名称。
        3. 选择字典类型为“静态字典”并添加静态字典项。
        4. 填写字典项的键、名称和选择项，并保存配置。

        :param web_driver: pytest 提供的 WebDriver 实例，用于操作网页。
        """
        self.driver = web_driver
        self.driver.get("https://op-test.aidmed.net/hospital-operate/config-item/templates")

        # 选择指定节点并进入添加页面
        self.wait_for_clickable(
            (By.XPATH, "//div[@class='el-tree']//div[@class='custom-tree-node']/div[.='自动化测试专用']")).click()
        time.sleep(1)
        self.wait_for_clickable((By.CSS_SELECTOR, ".page-config-add > .el-button")).click()

        # 输入配置项名称和显示名称
        self.wait_for_clickable((By.CSS_SELECTOR, ".is-required:nth-child(1) .el-input__inner")).click()
        self.wait_for_clickable((By.CSS_SELECTOR, ".is-required:nth-child(1) .el-input__inner")).send_keys("ceshi2")
        self.wait_for_clickable((By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(2) > .el-form-item__content > .el-input > .el-input__inner")).click()
        self.wait_for_clickable((By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(2) > .el-form-item__content > .el-input > .el-input__inner")).send_keys(
            "静态字典")

        # 选择“静态字典”类型
        self.wait_for_clickable((By.XPATH,
                                 "//div[@class='el-form-item is-required el-form-item--medium']//i[@class='el-select__caret el-input__icon el-icon-arrow-up']")).click()
        time.sleep(2)
        self.wait_for_clickable((By.XPATH, "//li[contains(.,'静态字典（Class）')]")).click()

        # 添加字典项
        self.wait_for_clickable((By.CSS_SELECTOR, ".el-icon-circle-plus-outline")).click()
        self.wait_for_clickable((By.CSS_SELECTOR, ".el-form > .is-required:nth-child(1) .el-input__inner")).click()
        self.wait_for_clickable((By.CSS_SELECTOR, ".el-form > .is-required:nth-child(1) .el-input__inner")).send_keys(
            "key1")
        self.wait_for_clickable((By.CSS_SELECTOR, ".el-form > .el-form-item:nth-child(2) .el-input__inner")).send_keys(
            "name1")

        # 选择字典项的类型和关联动态字典
        self.wait_for_clickable((By.XPATH,
                                 "//body[@class='el-popup-parent--hidden']//form[@class='el-form']/div[@class='el-form-item is-required el-form-item--medium']//i[@class='el-select__caret el-input__icon el-icon-arrow-up']")).click()
        self.wait_for_clickable((By.XPATH, "//body[@class='el-popup-parent--hidden']//li[5]/span[.='选择项']")).click()
        self.wait_for_clickable(
            (By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input:nth-child(1) .el-select__caret")).click()
        self.wait_for_clickable((By.XPATH, "//span[.='autotest.ceshi1 — 动态字典']")).click()

        # 保存字典项并提交配置
        self.wait_for_clickable((By.XPATH, "//body[@class='el-popup-parent--hidden']/div[5]//span[.='保 存']")).click()
        time.sleep(2)
        self.wait_for_clickable((By.XPATH, "//body[@class='el-popup-parent--hidden']/div[3]//span[.='保 存']")).click()

        time.sleep(2)

    def test_xuanzexiang(self, web_driver):
        """
        测试添加“选择项”配置的完整流程，包括以下步骤：
        1. 导航到配置页面并选择特定的节点。
        2. 输入配置项的名称和显示名称。
        3. 选择配置项类型为“选择项”并关联动态字典。
        4. 提交并保存配置。

        :param web_driver: pytest 提供的 WebDriver 实例，用于操作网页。
        """
        self.driver = web_driver
        self.driver.get("https://op-test.aidmed.net/hospital-operate/config-item/templates")
        time.sleep(2)

        # 选择“自动化测试专用”节点并点击“添加”按钮
        self.wait_for_clickable(
            (By.XPATH, "//div[@class='el-tree']//div[@class='custom-tree-node']/div[.='自动化测试专用']")).click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".page-config-add > .el-button").click()
        time.sleep(2)

        # 输入配置项的名称和显示名称
        self.driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(1) .el-input__inner").send_keys("ceshi4")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(2) > .el-form-item__content > .el-input > .el-input__inner").send_keys(
            "选择项")
        time.sleep(2)

        # 选择“选择项”类型
        self.wait_for_clickable((By.XPATH,
                                 "//div[@class='el-form-item is-required el-form-item--medium']//i[@class='el-select__caret el-input__icon el-icon-arrow-up']")).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[contains(.,'选择项')]").click()
        time.sleep(2)

        # 关联动态字典
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(2) .el-input:nth-child(1) .el-select__caret").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[contains(.,'autotest.ceshi1 — 动态字典')]").click()
        time.sleep(2)

        # 提交并保存配置
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
        time.sleep(5)
