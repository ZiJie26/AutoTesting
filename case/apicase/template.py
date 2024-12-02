from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

_td = load_test_data_from_csv('')


def defname(ac, td):
    headers = {
        **common_headers_admin,
    }
    ac.get('', td, headers=headers, params={})


import pytest


class Test:

    @pytest.mark.parametrize('td', _td)
    def test_check_patient_prepared_get(self, api_client_admin, td):
        defname(api_client_admin, td)


import pytest

from common.load_data_from_file import load_test_data_from_csv
from data.api.common_api_data import *

td = load_test_data_from_csv('')


@pytest.mark.parametrize("td", td)
def test_(api_client_admin, td):
    headers = {
        **common_headers_admin,
    }
    api_client_admin.get('', td, headers=headers)
