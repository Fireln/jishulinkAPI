#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/29
import allure
from testscripts.api import cert, pay_answer

cert_real_name_res = None
user_id = "f72687ae-9a0e-41f3-8814-b6586b7adb45"
pay_answer_id = None


@allure.feature("认证")
@allure.severity("blocker")
class TestRealName(object):
    @allure.story("实名认证")
    def test_real_name(self):
        global cert_real_name_res
        global user_id
        user_id = cert.regiest()
        cert_real_name_res = cert.cert_real_name()

    @allure.story("职场认证")
    def test_career(self):
        if cert_real_name_res:
            cert.cert_career()
            cert.review_career()

    @allure.story("教育认证")
    def test_edu(self):
        if cert_real_name_res:
            cert.cert_edu()
            cert.review_edu()


@allure.feature("付费答疑")
@allure.severity("normal")
class TestPayAnswer(object):
    @allure.testcase("申请开通付费答疑")
    def test_publish(self):
        global pay_answer_id
        if user_id:
            # pay_answer_id = pay_answer.publish(user_id)
            pay_answer_id = "pa10199"

    @allure.testcase("审核通过付费答疑")
    def test_approve_true(self):
        if pay_answer_id:
            pay_answer.approve(pay_answer_id)

    @allure.testcase("付费答疑详情")
    def test_change(self):
        if pay_answer_id:
            pay_answer.detail_user_id(user_id)
            pay_answer.detail_pid(pay_answer_id)

    @allure.testcase("修改付费答疑")
    def test_change(self):
        if pay_answer_id:
            pay_answer.close(pay_answer_id)
            pay_answer.open(pay_answer_id)
            pay_answer.modify(pay_answer_id)

    @allure.testcase("购买答疑流程")
    def test_buy(self):
        if pay_answer_id:
            pay_answer_order_id = pay_answer.place(pay_answer_id)
            if pay_answer_order_id:
                pay_answer.payment(pay_answer_order_id)
                pay_answer.accept(pay_answer_order_id)
                pay_answer.complete(pay_answer_order_id)
                pay_answer.vote(pay_answer_order_id)
                pay_answer.votes(pay_answer_id)
                pay_answer.order_info(pay_answer_order_id)
                pay_answer.list_customer()
                pay_answer.list_expert(user_id)
                pay_answer.pay_answer_orders(pay_answer_id)
                pay_answer.payanswer_order(pay_answer_order_id)

    @allure.testcase("用户取消订单")
    def test_abandon(self):
        if pay_answer_id:
            pay_answer_order_id = pay_answer.place(pay_answer_id)
            if pay_answer_order_id:
                pay_answer.payment(pay_answer_order_id)
                pay_answer.abandon(pay_answer_order_id)

    @allure.testcase("专家拒绝订单")
    def test_refuse(self):
        if pay_answer_id:
            pay_answer_order_id = pay_answer.place(pay_answer_id)
            if pay_answer_order_id:
                pay_answer.payment(pay_answer_order_id)
                pay_answer.refuse(pay_answer_order_id)

    @allure.testcase("用户申诉")
    def test_complain(self):
        if pay_answer_id:
            pay_answer_order_id = pay_answer.place(pay_answer_id)
            if pay_answer_order_id:
                pay_answer.payment(pay_answer_order_id)
                pay_answer.complete(pay_answer_order_id)
                pay_answer.complain(pay_answer_order_id)


if __name__ == '__main__':
    t = TestPayAnswer()
    t.test_publish()
