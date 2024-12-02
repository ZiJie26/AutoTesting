import csv
import json
import os
from pathlib import Path


def find_project_root():
    """
    查找项目根目录（通过识别 main.py 或 .git 目录来定位根目录）
    :return: 返回项目根目录
    """

    current_path = Path(__file__).resolve()

    # 向上查找包含 main.py 或 .git 的目录
    for parent in current_path.parents:
        if (parent / "main.py").exists() or (parent / ".git").exists():
            return parent

    # 如果未找到，则返回当前路径的两级父目录作为项目根目录的假设
    return current_path.parent.parent


def load_json_file(file_name):
    """
    从相对路径加载 JSON 文件。
    :param file_name: 文件的相对路径（相对于项目根目录）
    :return: 解析后的 JSON 数据
    """
    # 调用 find_project_root 来定位项目根目录
    file_path = os.path.join(find_project_root(), file_name)

    # 打开并加载 JSON 文件
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def load_test_data_from_csv(file_name):
    """
    从csv中读取数据存放到字典中
    :param file_name: 文件路径
    :return: 转换后的字典
    """
    test_data = []
    file_path = os.path.join(find_project_root(), file_name)
    # 使用 'utf-8-sig' 编码打开文件，去除 BOM
    with open(file_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_case = {}
            for key, value in row.items():
                key = key.strip()  # 去掉键的空格
                value = value.strip() if value else None  # 如果值为空，赋值为 None

                # 检查是否为空值并赋予默认值或跳过
                if value is None or value == '':
                    test_case[key] = None  # 或者设置其他默认值
                else:
                    try:
                        test_case[key] = int(value) if value.isdigit() else value
                    except ValueError:
                        test_case[key] = value  # 保持为字符串

            test_data.append(test_case)

    return test_data
