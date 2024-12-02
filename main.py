import sys

import pytest

from common.load_data_from_file import load_json_file, find_project_root
from suites import *

# 将所有测试套件添加到一个字典中
all_suites = {
    # 添加测试套件,记得加逗号
    # "testf": test_suite,
    "moban": moban_suite,
    "yong_yao_yu_ding_dan": yong_yao_yu_ding_dan_suite,
    "wen_zhen_kai_fang": wen_zhen_kai_fang_suite,
}

env_conf = load_json_file("data/config/prod_paths.json")

# 获取项目根目录的绝对路径
project_root = find_project_root()

# 添加项目根目录到sys.path
sys.path.append(project_root)


def main():
    if len(sys.argv) > 1:
        # 使用命令行参数中指定的测试套件
        for arg in sys.argv[1:]:
            if arg in all_suites:
                pytest.main(all_suites[arg])
            else:
                print(f"Test suite '{arg}' not found.")
    else:
        # 运行所有测试套件
        all_test_files = []
        for suite_name, suite in all_suites.items():
            print(f"Adding test suite: {suite_name}")
            all_test_files.extend(suite)
        pytest.main(all_test_files)


if __name__ == "__main__":
    main()
