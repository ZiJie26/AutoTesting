import pytest

from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

check_duplicate_td = load_test_data_from_csv('data/api/follow-up/question/classification/admin/check-duplicate.csv')


@pytest.mark.parametrize("td", check_duplicate_td)
def test_check_duplicate_get(api_client_admin, td):
    headers = {
        **common_headers_admin,
    }
    api_client_admin.get('/follow-up/question/classification/admin/check-duplicate', td, headers=headers, params={})
