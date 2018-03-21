#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/20
from data.data import eve
import requests
import allure
import json


class OpenPostDetail(object):

    @allure.step("发布悬赏问答")
    def create_post(self):
        data = {
            "url": eve.server + "/post/publish",
            "files": [
                ('authorId', (None, eve.user_id)),
                ('subject', (None, '测试测试测试测试?')),
                ('bodyText', (None, '测试测试测试测试测试测试测试测试测试测试测试测试')),
                ('postType', (None, 'QA')),
                ('coins', (None, '20')),
            ]
        }
        response = requests.post(url=data.get("url"), files=data.get("files"))
        if response.status_code == 200:
            res = response.json()
            if res.get("rc") == 0:
                return True, res
            else:
                return False, res
        else:
            return False, response.text


if __name__ == '__main__':
    t = PostCoin()
    print(t.create_post())
