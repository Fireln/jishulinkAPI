#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/4/24
from data.data import eve
from tools import conn
import requests
import random


class RegisterTags(object):
    """注册标签设置"""

    def __init__(self):
        self.url = eve.server + "/register_tags/create"
        self.data = {
            "name": "航空技术",
            "baseMemberCount": 123,
            "tPointId": "22F9E499-77C4-479D-BF05-092C7FED1F64",
            "operator": "admin"
        }
        self.conn = conn.ConnMysql()
        self.old_names = ['机械工程',
                          '电子科学及技术',
                          '电气工程',
                          '材料科学与工程',
                          '航空技术',
                          '控制科学与工程',
                          '兵器科学与技术',
                          '动力工程及工程热物理',
                          '土木建筑',
                          '水利工程',
                          '力学',
                          '测绘技术',
                          '船舶与海洋工程',
                          '交通运输工程',
                          '冶金工程',
                          '矿业工程',
                          '石油与天然气工程',
                          '仪器科学及技术',
                          '核科学与技术',
                          '地质资源与地质工程',
                          '信息与通信工程',
                          '环境科学与工程',
                          '纺织科学与工程',
                          '光学工程',
                          '生物化学工程',
                          '生物医学工程',
                          '声学工程',
                          '食品工程',
                          '轻工技术与工程',
                          '计算机科学与技术'
                          ]
        self.new_names = ['机械工程',
                          '电子技术',
                          '电气工程',
                          '材料科学',
                          '航空技术',
                          '控制工程',
                          '兵器技术',
                          '动力工程',
                          '土木建筑',
                          '水利工程',
                          '力学',
                          '测绘技术',
                          '船舶海工',
                          '交通运输',
                          '冶金工程',
                          '矿业工程',
                          '石油天然气',
                          '仪器科学',
                          '核技术',
                          '地质工程',
                          '通信工程',
                          '环境工程',
                          '纺织工程',
                          '光学工程',
                          '生物化学',
                          '生物医学',
                          '声学工程',
                          '食品工程',
                          '轻工技术',
                          '计算机',
                          ]

    def add(self):
        for old_name, new_name in zip(self.old_names, self.new_names):
            query = "SELECT t_point_id FROM tbl_vw_technical_points WHERE `name` ='{}' ".format(old_name)
            t_id = self.conn.do_select(query=query)[0].get("t_point_id")
            self.data["name"] = new_name
            self.data["tPointId"] = t_id
            self.data["baseMemberCount"] = random.randint(10000, 30000)
            with requests.post(url=self.url, json=self.data) as response:
                if response.status_code == 200:
                    res = response.json()
                    print(res)


if __name__ == '__main__':
    t = RegisterTags()
    t.add()
