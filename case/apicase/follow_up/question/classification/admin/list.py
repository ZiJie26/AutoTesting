from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

list_td = load_test_data_from_csv('data/api/follow-up/question/classification/admin/list.csv')


def list_get(ac, td):
    headers = {
        **common_headers_admin,
    }
    return ac.get('/follow-up/question/classification/admin/list', td, headers=headers, params={})
