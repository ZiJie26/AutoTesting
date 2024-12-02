import time

from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

edit_td = load_test_data_from_csv('data/api/follow-up/question/classification/admin/edit.csv')


def edit_put(ac, td):
    time.sleep(3)
    headers = {
        **common_headers_admin,
        "Content-Type": "application/json",
    }
    ac.put('/follow-up/question/classification/admin/edit', td, headers=headers, json_data={})
