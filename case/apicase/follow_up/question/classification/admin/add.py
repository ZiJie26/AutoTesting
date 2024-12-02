import time

from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

add_post_td = load_test_data_from_csv('data/api/follow-up/question/classification/admin/add.csv')


def add_post(api_client_admin, td):
    time.sleep(3)
    headers = {
        **common_headers_admin,
        "Content-Type": "application/json",
    }
    api_client_admin.post('/follow-up/question/classification/admin/add', td, headers=headers, json_data={})
