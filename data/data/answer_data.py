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
            "data": [
                ('authorId', (None, eve.user_id)),
                ('subject', (None, 'CAD可以3D打印吗?')),
                ('bodyText', (None, 'CAD可以3D打印吗')),
                ('postType', (None, 'QA')),
                ('coins', (None, '20')),
            ]
        },
        keys.detail: {"url": eve.server + "/post/{}"},
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
        keys.is_like: {"url": eve.server + "/post/{}/is_liked_by/" + eve.user_id_two, },
        keys.new_reply_list: {"url": eve.server + "/qa/{}/new_reply_list"},
        keys.adopt_answer: {"url": eve.server + "/post/qa/adopt_answer?postId={}&userId=" + eve.user_id + "&coins=5"},
        keys.recommend: {"url": eve.server + "/qa/reply/{}/recommend/" + eve.user_id},
        keys.delete_replay: {
            "url": eve.server + "/post/{answer_id}?operatorId=" + eve.user_id},
        keys.chat: {
            "url": eve.server + "/post/getChat?postId={}&userOneId=" + eve.user_id + "&userTwoId=" + eve.user_id_two + "&begin=0&length=5"},
        keys.reply: {"url": eve.server + "/reply",
                     "data": [
                         ("bodyText", (None, "可以的")),
                         ("authorId", (None, eve.user_id_two)),
                     ]},
    }


if __name__ == '__main__':
    print(AnswerData().data["publish"])
