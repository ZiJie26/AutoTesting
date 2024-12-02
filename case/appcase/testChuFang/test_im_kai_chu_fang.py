import os

from common.basepage import *  # 导入基类和其他通用方法
from common.load_data_from_file import find_project_root
from pageobject.app_im_shengfang import get_date_time_from_file  # 导入文件读写相关方法
from pageobject.doc.po_chufang import ChuFang
from pageobject.doc.po_im import IM

file_path = os.path.join(find_project_root(), "data/tempdata/date_time.json")


class TestIMKaiChuFang(BasePage):
    """
    该类用于测试IM列表中，给第一个患者开处方并使用第一个西药模板的流程。
    测试涉及到从列表中选择患者，生成处方并检查处方状态。
    """

    def test_im_kai_chu_fang(self, doc_driver):
        """
        测试IM模块的开处方流程，具体步骤如下：
        1. 选择第一个患者。
        2. 进入开处方界面，选择处方模板并生成处方。
        3. 记录并打印生成处方的时间信息。
        4. 将处方时间写入文件，供后续测试使用。

        :param doc_driver: 由 pytest 提供的Appium驱动实例，用于操作移动应用。
        """
        IM().choose_first(doc_driver)
        IM().kaichufang_button(doc_driver)
        time.sleep(2)
        ChuFang().kai_chu_fang(doc_driver)
        date_time = ChuFang().check_time(doc_driver)
        assert date_time is not None, "Read time failed"
        # 准备要写入的数据
        data = {"date_time": date_time}

        # 打开并写入 JSON 文件
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Date time updated in file: {date_time}")

    def test_shenfanglast(self, med_driver):
        """
        测试IM模块的审方功能，流程如下：
        1. 从文件中读取上一个测试生成的处方时间。
        2. 根据时间在处方列表中查找对应的处方。
        3. 点击该处方并进行审方操作。

        :param med_driver: 由 pytest 提供的Appium驱动实例，用于操作移动应用。
        """
        self.driver = med_driver
        date_time = get_date_time_from_file()  # 从文件中获取处方时间
        time.sleep(3)
        self.tap_by_relative_coordinates(112, 835)  # 选择处方项
        time.sleep(1)
        print(date_time)

        # 根据时间查找对应处方
        self.find_element_until_text(date_time)
        self.wait_and_click(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{date_time}")')  # 点击处方
        time.sleep(1)
        self.tap_by_relative_coordinates(531, 1230)  # 审方确认
        time.sleep(2)
