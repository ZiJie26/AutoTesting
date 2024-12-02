import json
import os.path

from common.load_data_from_file import find_project_root

file_path = os.path.join(find_project_root(), "data/tempdata/date_time.json")


def get_date_time_from_file():
    """
    用于读取时间数据确定需要审核的处方
    :return: JSON 文件中的时间数据
    """

    # 打开并读取 JSON 文件
    with open(file_path, "r") as f:
        data = json.load(f)

    return data["date_time"]
