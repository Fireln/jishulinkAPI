#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/16

from data.keys import answer_key
from data.data import eve
import random
import string
import os

keys = answer_key.AnswerKeys()
static_path = os.path.split(os.path.abspath(__file__))[0] + '\static'


class AnswerData(object):
    data = {
        keys.publish: {
            "url": eve.server + "/post/publish",
            "data": {
                "authorId": eve.user_id,
                "subject": "测试测试测试测试?",
                "bodyText": "测试测试测试测试测试测试测试测试测试测试测试测试",
                "postType": "QA",
                "imgs": open(r"{}\imgs\test.png".format(static_path), "rb"),
                "coins": "20",
                "charge": "false",
                "isAnonymous": "false",
            },
            "header": {}
        },
        keys.ads: {
            "url": eve.server + "/management/ad/group?labels=report"
        }, keys.top_activity_users: {
            "url": eve.server + "/user/top_activity_users"
        }, keys.search: {
            "url": eve.server + "/postCommon/college/search",
            "data": {
                "express": "QA", "resolved": False
            }
        }, keys.followed_qa: {
            "url": eve.server + "/qa/" + eve.user_id + "/followed_qa",
        }, keys.followed: {
            "url": eve.server + "/tpoint/followed/{}/qa".format(eve.user_id),
        }, keys.top_navigation: {
            "url": eve.server + "/tpoint/qa/top_navigation",
        },
    }


if __name__ == '__main__':
    print(AnswerData().data["publish"])
