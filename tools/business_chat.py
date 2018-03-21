#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/20

from data.data import eve
import requests
import string
import random


class Regiester(object):

    def regiest(self, tel):
        url = eve.server + "/user/register"
        data = {
            "telephone": tel,
            "password": "111111",
            "verificationCode": "bobo",
            "realname": "".join(random.sample(string.digits, 4)) + tel,
            "inviterUserId": 0
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("************************************************************", response.json())
            return response.json().get("ret").get("registerInfo").get("userId")

        else:
            print("GG", response.text)


class RenZheng(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def renzehng(self, tel):
        url = r"http://t.jishulink.com:8080/jishulink_test/member/cert/identity/{}".format(self.user_id)
        files = [
            ("telephone", (None, tel)),
            ("identityNumber", (None, "330304199407213323")),
            ("realname", (None, "周依依")),
            ("allowPublic", (None, "true")),
        ]
        response = requests.post(url, files=files)
        if response.status_code == 200:
            if response.json().get("rc") == 0:
                return response.json()

    def career(self):
        url = r"http://t.jishulink.com:8080/jishulink_test/member/cert/career/{}".format(self.user_id)
        files = [
            ("vocation", (None, "电子电器")),
            ("workAge", (None, "10")),
            ("workUnit", (None, "杭州前缀网络科技有限公司")),
            ("allowPublic", (None, "false")),
            ("duty", (None, "测试")),

        ]
        response = requests.post(url, files=files)
        if response.status_code == 200:
            if response.json().get("rc") == 0:
                pass

    def open_pay_answer(self):
        url = eve.server + r"/payanswer/create?userId={}&price=100&description=test".format(self.user_id)
        response = requests.get(url)
        if response.status_code == 200:
            if response.json().get("rc") == 0:
                return response.json().get("ret")

    def change_audit_status(self, pay_answer_id):
        url = eve.server + r"/payanswer/{}/change_audit_status?auditStatus=1&reason=test".format(pay_answer_id)
        response = requests.post(url)
        if response.status_code == 200:
            if response.json().get("rc") == 0:
                return response.json()


if __name__ == '__main__':
    # tel1 = '17100001216'
    # tel2 = '17100001217'
    # r = Regiester()
    # user_id = r.regiest(tel1)
    # r.regiest(tel2)
    ren = RenZheng(user_id="1629ddcb-4b52-42e4-a0fe-9ba7506d7c12")
    ren.renzehng("17100001216")
    ren.career()
    pay_answer_id = ren.open_pay_answer()
    ren.change_audit_status(pay_answer_id)
