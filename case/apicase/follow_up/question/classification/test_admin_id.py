import pytest

from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

admin_id_td = load_test_data_from_csv('data/api/follow-up/question/classification/admin/id.csv')


@pytest.mark.parametrize("td", admin_id_td)
def test_admin_id_get(api_client_admin, td):
    headers = {
        **common_headers_admin,
    }
    api_client_admin.get(f'/follow-up/question/classification/admin/{td["id"]}', td, headers=headers)
