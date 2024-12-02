from pageobject.doc.po_index import PageIndex


class TestJieTuWen:
    """
    该类用于测试医生在应用中接收图文问诊的流程操作。
    """

    def test_jie_tu_wen(self, doc_driver):
        """
        测试医生接收图文问诊的完整流程，包括：
        1. 进入图文问诊列表。
        2. 查看首个问诊的详情。
        3. 接诊并确认操作。

        :param doc_driver: pytest 提供的 Appium 驱动，用于控制应用的操作。
        """

        PageIndex().jie_wen_zhen(doc_driver)
        PageIndex().jie_tu_wen(doc_driver)
