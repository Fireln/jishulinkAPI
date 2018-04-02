#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/27


class CheckResponse(object):
    """处理请求结果"""

    def to_json(self, response):
        """
        请求转换为json数据
        :param response:接口返回json结果
        :return: 1.（bool,obj）2.None
        """
        if response.status_code == 200:
            json_data = response.json()
            if json_data.get("rc") != 0:
                return False, json_data
            else:
                return True, json_data

    def check(self, response, str):
        if response:
            if response[0]:
                print("%s成功" % str, response[1])
                return True
            else:
                print("%s失败" % str, response[1])
        else:
            print("%s失败" % str, response)
