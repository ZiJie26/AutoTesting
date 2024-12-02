import json
import os
from common.load_data_from_file import find_project_root  # 导入项目根目录查找工具

class CookieManager:
    """
    管理浏览器 cookies 的实用工具类。
    支持将 cookies 保存到指定文件，并从文件加载 cookies。
    """

    def __init__(self, driver, file_name="cookies.json"):
        """
        初始化 CookieManager 实例，设置驱动和 cookies 文件路径。

        :param driver: 浏览器驱动实例。
        :param file_name: 保存 cookies 的文件名，默认为 "cookies.json"。
        """
        self.driver = driver
        root_dir = find_project_root()
        self.file_path = os.path.join(root_dir, "data", "config", file_name)

    def save_cookies(self):
        """
        将当前浏览器的 cookies 保存到文件。
        如果文件路径不存在，将自动创建目录。
        """
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        cookies = self.driver.get_cookies()
        print("Saving cookies:", cookies)  # 打印 cookies
        print("Saving to file:", self.file_path)  # 打印文件路径

        with open(self.file_path, "w") as file:
            json.dump(cookies, file)

    def load_cookies(self):
        """
        从文件加载 cookies 并添加到当前浏览器会话。
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
