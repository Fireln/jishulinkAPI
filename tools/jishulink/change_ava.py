#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/4/19
import os
import random

from tools.conn import ConnMysql
from data.data import eve
import requests
from tools.check_response import CheckResponse


class ChangeAva(object):
    """修改头像"""

    def __init__(self):
        self.path = os.path.split(__file__)[0] + "/static/ava"
        self.conn = ConnMysql()
        self.check = CheckResponse()

    def get_ava_list(self):
        ava_list = []
        for root, dirs, file_list in os.walk(self.path):
            for file_name in file_list:
                path_file = os.path.join(root, file_name)
                ava_list.append(path_file)
        if ava_list:
            return ava_list
        else:
            raise Exception("文件不存在")

    def get_user_id(self):
        sql = "SELECT user_id FROM tbl_vw_match_rater"
        if "http://t." in eve.server:
            return self.conn.do_select(query=sql)
        else:
            raise Exception("请切换环境到测试服")

    def change_ava(self, user_list, ava_list):
        url = eve.server + "/user/{userId}/update/avatar"
        for user in user_list:
            user_id = user.get("user_id")
            real_url = url.format(userId=user_id)
            ava = random.choice(ava_list)
            files = [("avatar", ('1.png', open(ava, "rb"), "image/png"))]
            res = requests.request("post", url=real_url, files=files)
            self.check.check(self.check.to_json(res), "修改头像")


if __name__ == '__main__':
    t = ChangeAva()
    t.change_ava(t.get_user_id(), t.get_ava_list())
