import json
import pymysql
from common.load_data_from_file import find_project_root  # 导入项目根目录查找工具


class DatabaseUtils:
    """
    提供与 MySQL 数据库连接和配置管理的实用工具类。
    从配置文件加载数据库连接信息，支持连接、关闭和获取数据库连接。
    """

    def __init__(self, config_file=None):
        """
        初始化 DatabaseUtils 实例，加载数据库配置文件并准备连接。

        :param config_file: 可选，数据库配置文件路径，默认值为项目根目录下的 "data/config/db_config.json"。
        """
        project_root = find_project_root()
        if config_file is None:
            config_file = project_root / "data" / "config" / "db_config.json"
        self.config_file = config_file
        self.connection = None
        self.db_config = self._load_db_config()

    def _load_db_config(self):
        """
        从 JSON 配置文件中加载数据库连接信息。

        :return: 包含数据库配置信息的字典。
        :raises FileNotFoundError: 如果配置文件未找到。
        :raises ValueError: 如果 JSON 文件解析失败。
        """
        try:
            with open(self.config_file, "r") as file:
                db_config = json.load(file)
            return db_config
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from {self.config_file}.")

    def connect(self):
        """
        使用加载的配置信息连接到 MySQL 数据库。

        :raises pymysql.MySQLError: 如果数据库连接失败。
        """
        if self.connection is None and self.db_config:
            try:
                self.connection = pymysql.connect(
                    host=self.db_config["host"],
                    port=self.db_config["port"],
                    user=self.db_config["user"],
                    password=self.db_config["password"],
                    database=self.db_config["database"],
                )
                print("Connected to MySQL database")
            except pymysql.MySQLError as e:
                raise pymysql.MySQLError(f"Error connecting to MySQL database: {e}")

    def close(self):
        """
        关闭当前的数据库连接，并释放资源。
        """
        if self.connection:
            self.connection.close()
            self.connection = None
            print("MySQL connection is closed")

    def get_connection(self):
        """
        获取当前数据库连接实例。

        :return: 当前的 pymysql 连接实例。
        :raises Exception: 如果数据库连接未建立。
        """
        if self.connection is None:
            raise Exception("Database connection is not established.")
        return self.connection
