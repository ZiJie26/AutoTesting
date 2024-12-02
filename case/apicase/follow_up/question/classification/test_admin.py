import pytest

from case.apicase.follow_up.question.classification.admin.add import *
from case.apicase.follow_up.question.classification.admin.delete_id import delete_id_delete, delete_id_delete_td
from case.apicase.follow_up.question.classification.admin.edit import edit_put, edit_td
from case.apicase.follow_up.question.classification.admin.list import list_get, list_td


class TestAdmin:

    def test_classification_base(self, api_client_admin):
        td_add = {
            "name": "自动化测试1"
        }
        add_post(api_client_admin, td_add)
        td_list = {
            "pageNum": "1",
            "pageSize": "1",
            "EV": 200,
        }
        id = list_get(api_client_admin, td_list).json().get('data')[0].get('id')
        td_edit = {
            "id": id,
            "revision": 1,
            "name": "自动化测试2"
        }
        edit_put(api_client_admin, td_edit)
        td_delete = {
            "id": id,
            "revision": 1
        }
        delete_id_delete(api_client_admin, td_delete)

    @pytest.mark.parametrize("td", add_post_td)
    def test_add_post(self, api_client_admin, td):
        add_post(api_client_admin, td)

    @pytest.mark.parametrize("td", edit_td)
    def test_edit_put(self, api_client_admin, td):
        edit_put(api_client_admin, td)

    @pytest.mark.parametrize("td", delete_id_delete_td)
    def test_delete_id_delete(self, api_client_admin, td):
        delete_id_delete(api_client_admin, td)

    @pytest.mark.parametrize("td", list_td)
    def test_list_get(self, api_client_admin, td):
        list_get(api_client_admin, td)
