from case.apicase.follow_up.hospital_admin.classification import *

from data.api.common_api_data import *


class TestGateWay:
    """
    测试中白名单设置为:
    - /follow-up/hospital-admin/**
    - /follow-up/exam-record
    测试中黑名单设置为:
    - /follow-up/hospital-admin/warn/*
    - /follow-up/question/classification/admin/add
    """

    def test_in_whitelist(self, api_client_admin):
        params_warn = {
            'followUpRecordId': '611',  # 随访记录id
            'EV': 200
        }

        api_client_admin.get('/follow-up/hospital-admin/warn', params_warn, headers=common_headers_admin,
                             params={})  # 在白名单
        params_warn2 = {
            'followUpRecordId': '611',  # 随访记录id
            'EV': 200
        }
        api_client_admin.get('/follow-up/hospital-admin/warn', params_warn2, headers=common_headers_admin,
                             params={})  # 在白名单
        params_exam_record = {
            'patientIdNumber': '152',
            'hospitalId': '1',
            'EV': 401
        }

        api_client_admin.get('/follow-up/exam-record', params_exam_record, headers=common_headers_patient,
                             params={})  # 在白名单
        params_exam_record2 = {
            'patientIdNumber': '152',
            'hospitalId': '1',
            'EV': 401
        }

        api_client_admin.get('/follow-up/exam-record', params_exam_record2, headers=common_headers_patient,
                             params={})  # 在白名单

    def test_in_blacklist(self, api_client_admin):
        headers_warn = common_headers_admin
        td_warn_id_get = {
            "EV": 500,
        }
        api_client_admin.get('/follow-up/hospital-admin/warn/66', td_warn_id_get, headers=headers_warn)  # 在黑名单
        td_warn_id_get_repeat = {
            "EV": 502,
        }
        api_client_admin.get('/follow-up/hospital-admin/warn/66', td_warn_id_get_repeat, headers=headers_warn)  # 在黑名单
        time.sleep(1)
        td_warn_id_get_repeat = {
            "EV": 500,
        }
        api_client_admin.get('/follow-up/hospital-admin/warn/66', td_warn_id_get_repeat, headers=headers_warn)  # 在黑名单
        headers_add = {
            **common_headers_admin,
            "Content-Type": "application/json",
        }
        td_add_post = {
            "name": "",
            "EV": 500,
        }
        api_client_admin.post('/follow-up/question/classification/admin/add', td_add_post, headers=headers_add,
                              json_data={})
        td_add_post2 = {
            "name": "",
            "EV": 502,
        }
        api_client_admin.post('/follow-up/question/classification/admin/add', td_add_post2, headers=headers_add,
                              json_data={})
        time.sleep(1)
        td_add_post3 = {
            "name": "",
            "EV": 500,
        }
        api_client_admin.post('/follow-up/question/classification/admin/add', td_add_post3, headers=headers_add,
                              json_data={})

    def test_not_in_black_or_whitelist(self, api_client_admin):
        td_admin_id_get = {
            "id": "0",
            "EV": 500,
        }
        api_client_admin.get(f'/follow-up/question/classification/admin/{td_admin_id_get["id"]}', td_admin_id_get,
                             headers=common_headers_admin)
        td_admin_id_get_re = {
            "id": "0",
            "EV": 502,
        }
        api_client_admin.get(f'/follow-up/question/classification/admin/{td_admin_id_get_re["id"]}', td_admin_id_get_re,
                             headers=common_headers_admin)
        time.sleep(1)
        td_admin_id_get_re2 = {
            "id": "0",
            "EV": 500,
        }
        api_client_admin.get(f'/follow-up/question/classification/admin/{td_admin_id_get_re2["id"]}',
                             td_admin_id_get_re2,
                             headers=common_headers_admin)

    def test_header(self, api_client_admin):
        headers_warn_header1 = {
            **common_headers_admin,
            "x-test": "a"
        }
        td_warn_id_get = {
            "EV": 500,
        }
        api_client_admin.get('/follow-up/hospital-admin/warn/66', td_warn_id_get, headers=headers_warn_header1)  # 在黑名单
        headers_warn_header2 = {
            **common_headers_admin,
            "x-test": "b"
        }
        headers_warn_header3 = {
            **common_headers_admin,
        }
        api_client_admin.get('/follow-up/hospital-admin/warn/66', td_warn_id_get, headers=headers_warn_header2)  # 在黑名单
        api_client_admin.get('/follow-up/hospital-admin/warn/66', td_warn_id_get, headers=headers_warn_header3)  # 在黑名单

    def test_in_v1_compatible_whitelist(self, api_client_admin):
        td_check_duplicate = {
            "id": 1,
            "name": "通用",
            "EV": 200,
        }
        api_client_admin.get('/follow-up/question/classification/admin/check-duplicate', td_check_duplicate,
                             headers=common_headers_admin, params={})
        api_client_admin.get('/follow-up/question/classification/admin/check-duplicate', td_check_duplicate,
                             headers=common_headers_admin, params={})
