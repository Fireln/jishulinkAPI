#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/29

from data.keys import business_keys
from data.data import eve

pay_answer_keys = business_keys.PayAnswer()


class PayAnswer(object):
    data = {
        pay_answer_keys.publish: {
            "url": eve.server + "/payanswer/create?userId={user_id}&price=100&description=test",
        },
        pay_answer_keys.change_audit_status: {
            "url": eve.server + "/payanswer/{pay_answer_id}/change_audit_status?auditStatus=1&reason=test",
        },
        pay_answer_keys.modify: {
            "url": eve.server + "/payanswer/{pay_answer_id}/update?price=100&description=modify",
        },
        pay_answer_keys.close: {
            "url": eve.server + "/payanswer/{pay_answer_id}/close",
        },
        pay_answer_keys.open: {
            "url": eve.server + "/payanswer/{pay_answer_id}/open",
        },
        pay_answer_keys.detail_pid: {
            "url": eve.server + "/payanswer/{pay_answer_id}",
        },
        pay_answer_keys.detail_user_id: {
            "url": eve.server + "/payanswer/by_user?userId={user_id}",
        },
        pay_answer_keys.place: {
            "url": eve.server + "/payanswer_order/place",
        },
        pay_answer_keys.abandon: {
            "url": eve.server + "/payanswer_order/{order_id}/abandon?reason=放弃预约",
        },
        pay_answer_keys.accept: {
            "url": eve.server + "/payanswer_order/{order_id}/accept",
        },
        pay_answer_keys.complete: {
            "url": eve.server + "/payanswer_order/{order_id}/complete",
        },
        pay_answer_keys.refuse: {
            "url": eve.server + "/payanswer_order/{order_id}/refuse?reason=拒绝答疑",
        },
        pay_answer_keys.order_info: {
            "url": eve.server + "/payanswer_order/{order_id}/info",
        },
        pay_answer_keys.list_customer: {
            "url": eve.server + "/payanswer_order/customer_orders?userId={user_id}&status=&begin=0&length=10",
        },
        pay_answer_keys.list_expert: {
            "url": eve.server + "/payanswer_order/expert_orders?userId={user_id}&status=&begin=0&length=10",
        },
        pay_answer_keys.pay_answer_orders: {
            "url": eve.server + "/payanswer_order/pay_answer_orders?status=&begin=0&length=10&payAnswerId={pay_answer_id}",
        },
        pay_answer_keys.payanswer_order: {
            "url": eve.server + "/payanswer_order/{order_id}/consultation",
        },
        pay_answer_keys.vote: {
            "url": eve.server + "/payanswer_order/{order_id}/vote?star=5&voteText=test",
        },
        pay_answer_keys.votes: {
            "url": eve.server + "/payanswer/{pay_answer_id}/votes?begin=0&length=10",
        },
        pay_answer_keys.complain: {
            "url": eve.server + "/payanswer_order/{order_id}/complain",
            "data": [("text", (None, "申诉测试"))]
        },
        pay_answer_keys.payment: {
            "url": eve.server + "/payanswer_order/new_payment",
            "data": {
                "orderId": "pao10681",
                "payerId": eve.user_id_two,
                "balanceAmount": "1",
                "smsCode": "bobo",
            }
        },

    }
