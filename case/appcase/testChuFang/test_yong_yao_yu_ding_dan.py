from pageobject.doc.po_index import PageIndex


class TestYongYaoYuDingDan:
    """
    该类用于测试开处方功能，继承自开处方页面对象类。
    """

    def test_yong_yao_yu_ding_dan(self, doc_driver):
        """
        测试医生在应用中执行开处方的完整流程，包括：
        1. 点击进入详情页面。
        2. 执行滑动操作，填写处方信息。
        3. 生成处方。

        :param doc_driver: pytest 提供的 Appium 驱动，用于控制移动应用。
        """
        PageIndex().jie_wen_zhen(doc_driver)
        PageIndex().yong_yao_yu_ding_dan(doc_driver)
