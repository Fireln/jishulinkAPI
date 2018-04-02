#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/20

from data.data import eve
import requests
import string
import random
from tools.conn import ConnMysql
from tools.check_response import CheckResponse

res = CheckResponse()
pay_answer_order = None


class DeleteZ(object):
    conn = ConnMysql()

    def delete(self):
        query = "DELETE FROM tbl_vw_certification_third_record WHERE realname = '周依依'"
        self.conn.do_delete(query)

    def sel(self, user_id):
        query = "SELECT cert_id from tbl_vw_certification_career WHERE user_id = '{}'".format(user_id)
        res = self.conn.do_select(query)
        return res[0].get("cert_id")


class Regiester(object):

    def regiest(self, tel):
        url = eve.server + "/user/register"
        data = {
            "telephone": tel,
            "password": "111111",
            "verificationCode": "bobo",
            "realname": "测试" + tel[:5],
            "inviterUserId": 0
        }
        response = res.to_json(requests.post(url, json=data))
        res.check(response, "注册")
        return response[1].get("ret").get("registerInfo").get("userId")


class RenZheng(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def renzehng(self, tel):
        """进行实名认证"""
        d = DeleteZ()
        d.delete()
        url = r"http://t.jishulink.com:8080/jishulink_test/member/cert/identity/{}".format(self.user_id)
        files = [
            ("telephone", (None, tel)),
            ("identityNumber", (None, "330304199407213323")),
            ("realname", (None, "周依依")),
            ("allowPublic", (None, "true")),
        ]
        response = res.to_json(requests.post(url, files=files))
        res.check(response, "实名认证")

    def career(self):
        """进行职场认证"""
        url = r"http://t.jishulink.com:8002/jishulink/member/cert/career/{}".format(self.user_id)
        files = [
            ("vocation", (None, "电子电器")),
            ("workAge", (None, "10")),
            ("workUnit", (None, "杭州前缀网络科技有限公司")),
            ("allowPublic", (None, "false")),
            ("duty", (None, "测试")),
            ("socialTitles", (None, "")),
        ]
        response = res.to_json(requests.post(url, files=files))
        res_check = res.check(response, "职场认证")
        if res_check:
            self.approve()

    def open_pay_answer(self):
        url = eve.server + r"/payanswer/payanswer?userId={}&price=100&description=test".format(self.user_id)
        response = res.to_json(requests.get(url))
        res.check(response, "申请开通付费答疑")
        if response or response[0]:
            return response[1].get("ret")

    def change_audit_status(self, pay_answer_id):
        url = eve.server + r"/payanswer/{}/change_audit_status?auditStatus=1&reason=test".format(pay_answer_id)
        response = res.to_json(requests.get(url))
        if res.check(response, "审核通过付费答疑"):
            return True

    def approve(self):
        d = DeleteZ()
        cert_id = d.sel(self.user_id)
        url = eve.server + r"/member/cert/approve/{user_id}?operator=admin&category=CAREER&certId={cert_id}".format(
            user_id=self.user_id, cert_id=cert_id)
        response = res.to_json(requests.put(url))
        res.check(response, "职场审核")


class Two(object):

    def __init__(self, user_id):
        self.user_id = user_id

    def add_balance(self):
        url = eve.server + r"/trade/addBalance/user/{}?money=1000".format(self.user_id)
        response = res.to_json(requests.put(url))
        res.check(response, "添加余额")

    def create_pao(self, pay_answer_id):
        url = eve.server + r"/payanswer_order/place"
        files = [
            ("payAnswerId", (None, pay_answer_id)),
            ("customerId", (None, self.user_id)),
            ("content", (None, "test")),
            ("telephone", (None, "telephone")),
        ]
        response = res.to_json(requests.post(url, files=files))
        if res.check(response, "生成答疑订单"):
            pao = response[1].get("ret")
            self.payment(pao)

    def payment(self, pao):
        url = eve.server + r"/payanswer_order/new_payment"
        body = {
            "orderId": pao,
            "tag": "PayAnswerOrder",
            "balanceAmount": "100",
            "payAmountUnit": "CNY",
            "method": "",
            "ticketIds": [],
            "sceneType": 0,
            "returnPath": "%2Fdayi%2Fpay%2Fpao10287%2Fsuccess",
            "coins": 0,
            "smsCode": "bobo",
            "description": ""
        }
        response = res.to_json(requests.post(url, json=body))
        res.check(response, "答疑付款")


if __name__ == '__main__':
    tel1 = "171" + "".join(random.sample(string.digits, 8))
    tel2 = "171" + "".join(random.sample(string.digits, 8))
    r = Regiester()
    user_id = r.regiest(tel1)
    pay_user_id = r.regiest(tel2)
    url = eve.server + "/jishulink/user/{0}/follow_user?followedUserId={1}".format(pay_user_id, user_id)
    ren = RenZheng(user_id=user_id)
    ren.renzehng(tel1)
    ren.career()
    # pay_answer_id = ren.open_pay_answer()
    # if pay_answer_id:
    #     if ren.change_audit_status(pay_answer_id):
    #         for i in range(3):
    #             pay = Two(pay_user_id)
    #             pay.add_balance()
    #             pay.create_pao(pay_answer_id)
    # response = res.to_json(requests.put(url))
    # res.check(response, "关注")
