#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/4/8
from data.keys import course_keys
from data.data import eve

c_keys = course_keys.CourseKeys()


class CourseData(object):
    data = {
        c_keys.create: {
            "url": eve.server + "/vcourse/create",
            "data": [
                ("userId", (None, eve.user_id)),
                ("title", (None, "创建课程测试创建课程测试")),
                ("description", (None, "创建课程测试创建课程测试")),
                ("price", (None, "1000")),
                ("totalChapter", (None, "2")),
                ("cover",
                 ('1.png', open(r"D:\pycharm\jishulinktest\data\data\static\imgs\test.png", "rb"), "image/png")),
            ]
        },
        c_keys.update: {
            "url": eve.server + "/vcourse/{course_id}/update",
            "data": [
                ("userId", (None, eve.user_id)),
                ("title", (None, "修改课程测试修改课程测试")),
                ("description", (None, "修改课程测试修改课程测试")),
                ("price", (None, "1")),
                ("totalChapter", (None, "2")),
                ("cover",
                 ('1.png', open(r"D:\pycharm\jishulinktest\data\data\static\imgs\test.png", "rb"), "image/png")),
            ]
        },
        c_keys.add_videos: {
            "url": eve.server + "/vcourse/{course_id}/add_video",
            "data": {
                "videos": [
                    {
                        "title": "框架结构地震作用分析20170326.wmv",
                        "videoId": eve.videos[0]
                    },
                    {
                        "title": "框架结构地震作用分析20170326.wmv",
                        "videoId": eve.videos[1]
                    },
                ]
            }
        },
        c_keys.publish: {
            "url": eve.server + "/vcourse/{course_id}/publish"
        },
        c_keys.add_tpoint: {
            "url": eve.server + "/vcourse/{course_id}/add_tpoint?tPointIds=" + eve.t_point_id
        },
        c_keys.remove_tpoint: {
            "url": eve.server + "/vcourse/{course_id}/remove_tpoint?tPointIds=" + eve.t_point_id
        },
        c_keys.info: {
            "url": eve.server + "/vcourse/{course_id}/info"
        },
        c_keys.videos: {
            "url": eve.server + "/vcourse/{course_id}/videos"
        },
        c_keys.down_video: {
            "url": eve.server + "/vcourse/{course_id}/down_video?videoId={video_id}"
        },
        c_keys.up_video: {
            "url": eve.server + "/vcourse/{course_id}/up_video?videoId={video_id}"
        },
        c_keys.place: {
            "url": eve.server + "/vcourse_order/place?videoCourseId={course_id}&customerUserId=" + eve.user_id_two
        },
        c_keys.close: {
            "url": eve.server + "/vcourse_order/{order_id}/close"
        },
        c_keys.remove: {
            "url": eve.server + "/vcourse_order/{order_id}/remove"
        },
        c_keys.order_info: {
            "url": eve.server + "/vcourse_order/{order_id}"
        },
        c_keys.customer_orders: {
            "url": eve.server + "/vcourse_order/" + eve.user_id_two + "/customer_orders"
        },
        c_keys.payment: {
            "url": eve.server + "/vcourse_order/new_payment",
            "data": {
                "orderId": "",
                "payerId": eve.user_id_two,
                "balanceAmount": "1",
                "payAmountUnit": "CNY",
                "method": "",
                "ticketIds": [],
                "sceneType": 0,
                "coins": 0,
                "smsCode": "bobo",
                "description": ""
            }
        },
        c_keys.reply: {
            "url": eve.server + "/vcourse/{course_id}/reply",
            "data": {
                "parentId": "",
                "authorId": eve.user_id_two,
                "title": "测试",
                "body": "测试测试测试"
            }
        },
        c_keys.reply_list: {
            "url": eve.server + "/vcourse/{course_id}/replys"
        },
        c_keys.signedUrl: {
            "url": eve.server + "/vcourse/{course_id}/{video_id}/signedUrl?userId=" + eve.user_id_two
        },
        c_keys.checkUserId: {
            "url": eve.server + "/vcourse/{course_id}/purchased_status?checkUserId=" + eve.user_id_two
        },
        c_keys.vote: {
            "url": eve.server + "/vcourse/{course_id}/vote",
            "data": {
                "userId": eve.user_id_two,
                "starts": 4
            }
        },
        c_keys.update_charge_status: {
            "url": eve.server + "/vcourse/{course_id}/update_charge_status",
            "data": {
                "videoId": "",
                "isFree": "1"
            }
        },

    }
