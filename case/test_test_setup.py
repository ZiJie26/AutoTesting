import time

from selenium.webdriver.common.by import By

from common.basepage import trans_json, BasePage
from common.sl_cookies import CookieManager


class TestDoc(BasePage):
    """
    该类用于调试各个部分的driver是否正常；
    以及进行部分代码的调试
    """

    def test_2(self, web_driver):
        self.driver = web_driver
        web_driver.get("https://op-test.aidmed.net/hospital-operate/config-item/setting")
        time.sleep(5)
        self.wait_for_clickable(
            (By.XPATH, "//div[@class='el-tree']//div[@class='custom-tree-node']/div[.='自动化测试专用']")).click()
        self.wait_and_click(By.XPATH, '//*[@id="w-e-element-3"]')
        time.sleep(5)
        self.hover_to_element(By.XPATH,
                              '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/div[1]/div[4]/div[3]/form/div/div/div/div/div[1]/div/div[21]/button')
        self.wait_for_clickable((By.XPATH,
                                 '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/div[1]/div[4]/div[3]/form/div/div/div/div/div[1]/div/div[21]/div/div/button')).click()
        time.sleep(5)
        self.upload_file('C:\\cat.jpg')
        time.sleep(5)
        cookie = CookieManager(web_driver)
        cookie.save_cookies()

    def test_doc(self, doc_driver):
        time.sleep(5)

    def test_med(self, med_driver):
        time.sleep(5)

    def test_api(self, api_client_admin):
        print(api_client_admin.get("/stage-api/code"))

        print(trans_json(api_client_admin.get("/stage-api/code")))
