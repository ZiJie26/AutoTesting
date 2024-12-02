from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

delete_id_delete_td = load_test_data_from_csv('data/api/follow-up/question/classification/admin/delete/id.csv')


def delete_id_delete(ac, td):
    headers = {
        **common_headers_admin,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    ac.delete(f'/follow-up/question/classification/admin/delete/{td["id"]}', td, headers=headers, data={})
