import json

import allure
import requests

from common.load_data_from_file import find_project_root  # 导入项目根目录查找工具


def load_cookies(cookies_file):
    """
    从指定的 JSON 文件加载 cookies。

    :param cookies_file: cookies 文件路径。
    :return: 以字典格式返回加载的 cookies，若文件不存在或解析失败则返回空字典。
    """
    try:
        with open(cookies_file, 'r') as f:
            cookies = json.load(f)
            return cookies
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


class APIClient:
    """
    该类用于与 API 进行交互，提供标准的 GET、POST、PUT 和 DELETE 请求方法。
    支持从文件中加载 cookies，并在请求中自动携带这些 cookies。
    """

    cookies_file_path = find_project_root() / 'data' / 'config' / 'api_cookies.json'

    def __init__(self, base_url, headers=None, cookies_file=cookies_file_path):
        """
        初始化 APIClient 实例，设置基础 URL、请求头信息，并从指定文件加载 cookies。

        :param base_url: API 的基础 URL。
        :param cookies_file: cookies 文件的路径，默认为 cookies_file_path。
        """
        self.base_url = base_url
        self.headers = headers or {}  # 如果没有提供 headers，则初始化为空字典
        self.cookies = load_cookies(cookies_file)

        # 转换 cookies 格式
        if isinstance(self.cookies, list):
            self.cookies = {cookie['name']: cookie['value'] for cookie in self.cookies}

    def get(self, endpoint, td, headers=None, params=None):
        """
        发送带有 cookies 的 GET 请求。

        :param params:
        :param td:
        :param headers: 请求头
        :param endpoint: 请求的 API 端点。
        :return: requests.Response 对象。
        """
        url = f"{self.base_url}{endpoint}"
        # 初始化 params 和 test_data

        for key, value in headers.items():
            self.headers[key] = value
        print(headers)
        if params is None:
            params = {}
        else:
            # 自动生成 params，排除最后一个键
            keys = list(td.keys())[:-1]  # 获取除最后一个键之外的所有键
            # 更新 params
            for key in keys:
                params[key] = td[key]
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        self.print_formatted_response(response)
        try:
            self.assert_status_code(response, td['EV'])
        except KeyError:
            print("no EV")
        self.headers = {}
        return response

    def post(self, endpoint, td, headers=None, data=None, json_data=None):
        """
        发送带有 cookies 的 POST 请求。

        :param td:
        :param endpoint: 请求的 API 端点。
        :param data: 可选的表单数据。
        :param json_data: 可选的 JSON 数据。
        :param headers: 可选的请求头字典，可以覆盖初始化时的 headers。
        :return: requests.Response 对象。
        """
        url = f"{self.base_url}{endpoint}"
        self.headers = {
            'Content-Type': 'application/json'
        }
        for key, value in headers.items():
            self.headers[key] = value

        # 更新 data 或 json_data
        def update_dict(d, td):
            for key, value in td.items():
                keys = key.split('.')
                sub_dict = d
                for k in keys[:-1]:
                    sub_dict = sub_dict.setdefault(k, {})
                sub_dict[keys[-1]] = value

        data_temp = {}
        json_data_temp = {}
        if data is not None:
            data_temp = data.copy()
            update_dict(data_temp, td)
        if json_data is not None:
            json_data_temp = json_data.copy()
            update_dict(json_data_temp, td)
        response = requests.post(url, headers=self.headers, cookies=self.cookies, data=data_temp, json=json_data_temp)
        self.print_formatted_response(response)
        if 'EV' not in td or not td['EV']:
            td['EV'] = {}
        self.assert_status_code(response, td['EV'])
        self.headers = {}
        return response

    def put(self, endpoint, td, headers=None, data=None, json_data=None):
        """
        发送带有 cookies 的 PUT 请求。

        :param json_data:
        :param headers:
        :param endpoint: 请求的 API 端点。
        :param data: 可选的请求数据。
        :return: requests.Response 对象。
        """
        url = f"{self.base_url}{endpoint}"
        self.headers = {
            'Content-Type': 'application/json'
        }
        for key, value in headers.items():
            self.headers[key] = value

        # 更新 data 或 json_data
        def update_dict(d, td):
            for key, value in td.items():
                keys = key.split('.')
                sub_dict = d
                for k in keys[:-1]:
                    sub_dict = sub_dict.setdefault(k, {})
                sub_dict[keys[-1]] = value

        data_temp = {}
        json_data_temp = {}
        if data is not None:
            data_temp = data.copy()
            update_dict(data_temp, td)
        if json_data is not None:
            json_data_temp = json_data.copy()
            update_dict(json_data_temp, td)
        print(json_data_temp, self.headers, data_temp)
        response = requests.put(url, headers=self.headers, cookies=self.cookies, data=data_temp, json=json_data_temp)
        self.print_formatted_response(response)
        if 'EV' not in td or not td['EV']:
            td['EV'] = {}
        self.assert_status_code(response, td['EV'])
        self.headers = {}
        return response

    def delete(self, endpoint, td, headers=None, data=None):
        """
        发送带有 cookies 的 DELETE 请求。

        :param td:
        :param headers:
        :param endpoint: 请求的 API 端点。
        :param data: 可选的请求数据。
        :return: requests.Response 对象。
        """
        url = f"{self.base_url}{endpoint}"
        self.headers = {}
        for key, value in headers.items():
            self.headers[key] = value

        # 更新 data 或 json_data
        def update_dict(d, td):
            for key, value in td.items():
                keys = key.split('.')
                sub_dict = d
                for k in keys[:-1]:
                    sub_dict = sub_dict.setdefault(k, {})
                sub_dict[keys[-1]] = value

        data_temp = {}
        if data is not None:
            update_dict(data_temp, td)
        response = requests.delete(url, headers=self.headers, cookies=self.cookies, data=data_temp)
        self.print_formatted_response(response)
        if 'EV' not in td or not td['EV']:
            td['EV'] = {}
        self.assert_status_code(response, td['EV'])
        self.headers = {}
        return response

    @staticmethod
    def print_formatted_response(response):
        # 格式化并打印响应内容，确保以美观的方式输出，并支持中文显示
        formatted_response = json.dumps(response.json(), indent=4, ensure_ascii=False)
        print(formatted_response)
        allure.attach(formatted_response)

    @staticmethod
    def assert_status_code(response, expected_value):
        """
        对响应进行断言，通过状态码以及某个数据是否等于期望值
        :param response: 发送请求得到的响应
        :param expected_value: 期望的数据
        """
        # 如果期望的状态码是200，进一步验证响应内容
        if expected_value != {}:
            if response.status_code == 200:
                if response.json().get("code") == expected_value:  # 如果得到的code与期望值相等，将得到的数据打印
                    print(response.json().get('code'))
                    print(response.json().get('msg'))
                else:
                    assert False, f"expect {expected_value},but ger error code {response.json().get('code')}!"
            else:
                # 如果状态码不是200，断言连接错误
                assert False, f"Connection error: status code {response.status_code}"
