#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/29

from data.keys import cert_Keys
from tools.check_response import CheckResponse
from tools.allure_assert import AllureAssert
from tools.conn import ConnMysql
from data.data import cert_data
from tools import params, file
from data.data import auth
import allure
import requests
import random
import string

conn = ConnMysql()
allure_assert = AllureAssert()
check_response = CheckResponse()
keys = cert_Keys.CertKeys()
my_auth = auth.Auth()

user_id = None


class Cert(object):
    def __init__(self):
        self.cert_data = None

    @allure.step("注册")
    def regiest(self):
        global user_id
        api = my_auth.data.get("regiest")
        tel = "171" + "".join(random.sample(string.digits, 8))
        api["data"]["telephone"] = tel
        api["data"]["realname"] = "测试" + "".join(random.sample(string.ascii_letters, 3))
        response = requests.post(url=api.get("url"), json=api.get("data"))
        if response.status_code == 200:
            json_data = response.json()
            if json_data.get("rc") == 0:
                user_id = json_data.get("ret").get("registerInfo").get("userId")
                self.cert_data = cert_data.CertData(user_id, tel)
                return user_id
            elif json_data.get("rc") == 1001:
                return self.regiest()
        else:
            assert False

    @allure.step("实名认证")
    def cert_real_name(self):
        query = "DELETE FROM tbl_vw_certification_third_record WHERE realname = '周依依'"
        conn.do_delete(query)
        api = self.cert_data.data.get(keys.real_name)
        if file.post(api):
            return True

    @allure.step("职场认证")
    def cert_career(self):
        api = self.cert_data.data.get(keys.career)
        file.post(api)

    @allure.step("审核通过职场认证")
    def review_career(self):
        query = "SELECT cert_id from tbl_vw_certification_career WHERE user_id = '{}'".format(user_id)
        cert_id = conn.do_select(query)[0].get("cert_id")
        api = self.cert_data.data.get(keys.review)
        api["data"]["certId"] = cert_id
        params.put(api)

    @allure.step("教育认证")
    def cert_edu(self):
        api = self.cert_data.data.get(keys.education)
        file.post(api)

    @allure.step("审核通过教育认证")
    def review_edu(self):
        query = "SELECT cert_id FROM  tbl_vw_certification_education WHERE user_id ='{}'".format(user_id)
        cert_id = conn.do_select(query)[0].get("cert_id")
        api = self.cert_data.data.get(keys.review)
        api["data"]["certId"] = cert_id
        api["data"]["category"] = "EDUCATION"
        params.put(api)


if __name__ == '__main__':
    c = Cert()
    c.regiest()
    c.cert_real_name()
    c.cert_edu()
    c.review_edu()
