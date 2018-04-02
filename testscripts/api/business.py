#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/29

from data.keys import business_keys
from tools.check_response import CheckResponse
from tools.allure_assert import AllureAssert
from tools.conn import ConnMysql
from data.data import business_data
from tools import url, params, file, json
from data.data import auth
import allure
from data.data import eve

conn = ConnMysql()
allure_assert = AllureAssert()
check_response = CheckResponse()
my_auth = auth.Auth()
pay_answer_data = business_data.PayAnswer()
pay_answer_keys = business_keys.PayAnswer()


class PayAnswer(object):
    def __init__(self):
        self.order_id = None

    @allure.step("发布付费答疑")
    def publish(self, user_id):
        api = pay_answer_data.data.get(pay_answer_keys.publish)
        api["url"] = api["url"].format(user_id=user_id)
        res = url.get(api)
        if res:
            return res.get("ret")

    @allure.step("审核通过付费答疑")
    def approve(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.change_audit_status)
        api["url"] = api["url"].format(pay_answer_id=pay_answer_id)
        if url.get(api):
            return True

    @allure.step("修改付费答疑")
    def modify(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.modify)
        api["url"] = api["url"].format(pay_answer_id=pay_answer_id)
        url.get(api)

    @allure.step("关闭付费答疑")
    def close(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.close)
        api["url"] = api["url"].format(pay_answer_id=pay_answer_id)
        url.get(api)

    @allure.step("开通付费答疑")
    def open(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.open)
        api["url"] = api["url"].format(pay_answer_id=pay_answer_id)
        url.get(api)

    @allure.step("根据ID获取付费答疑详情")
    def detail_pid(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.detail_pid)
        api["url"] = api["url"].format(pay_answer_id=pay_answer_id)
        url.get(api)

    @allure.step("根据userID获取付费答疑详情")
    def detail_user_id(self, user_id):
        api = pay_answer_data.data.get(pay_answer_keys.detail_user_id)
        api["url"] = api["url"].format(user_id=user_id)
        url.get(api)

    @allure.step("生成答疑订单")
    def place(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.place)
        api["data"] = [
            ("payAnswerId", (None, pay_answer_id)),
            ("customerId", (None, eve.user_id)),
            ("content", (None, "test")),
            ("telephone", (None, "13783783183")),
        ]
        res = file.post(api)
        if res:
            return res.get("ret")

    @allure.step("支付订单")
    def payment(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.payment)
        api["data"]["orderId"] = order_id
        json.post(api)

    @allure.step("用户取消订单")
    def abandon(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.abandon)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("专家接收订单")
    def accept(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.accept)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("专家完成订单")
    def complete(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.complete)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("专家拒绝订单")
    def refuse(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.refuse)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("订单详情")
    def order_info(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.order_info)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("购买的答疑列表")
    def list_customer(self):
        api = pay_answer_data.data.get(pay_answer_keys.list_customer)
        api["url"] = api.get("url").format(user_id=eve.user_id)
        url.get(api)

    @allure.step("出售的答疑列表")
    def list_expert(self, user_id):
        api = pay_answer_data.data.get(pay_answer_keys.list_expert)
        api["url"] = api.get("url").format(user_id=user_id)
        url.get(api)

    @allure.step("付费答疑订单列表")
    def pay_answer_orders(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.pay_answer_orders)
        api["url"] = api.get("url").format(pay_answer_id=pay_answer_id)
        url.get(api)

    @allure.step("获取咨询需求详情")
    def payanswer_order(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.payanswer_order)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("评论投票")
    def vote(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.vote)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("评论投票列表")
    def votes(self, pay_answer_id):
        api = pay_answer_data.data.get(pay_answer_keys.votes)
        api["url"] = api.get("url").format(pay_answer_id=pay_answer_id)
        url.get(api)

    @allure.step("付费答疑申诉")
    def complain(self, order_id):
        api = pay_answer_data.data.get(pay_answer_keys.complain)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)


if __name__ == '__main__':
    t = PayAnswer()
    t.payment("pao10681")
