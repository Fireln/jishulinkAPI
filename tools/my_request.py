#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/7
import requests
from tools.allure_assert import AllureAssert
from tools.check_point import CheckPoint

check = CheckPoint()
allure_assert = AllureAssert()


def client(method, url=None, params=None, json=None, file=None, api=None, data=None):
    """
    发起request请求接口
    :param method: 方法类型
    :param url: 接口地址
    :param params: query参数
    :param json: body参数
    :param file: 文件参数
    :param api: 失败时要写入测试报告的请求数据，包括url和参数
    :return: 返回dict类型的response数据，以后完善功能时可以做检查点
    """
    with requests.request(method, url=url, params=params, json=json, files=file, data=data) as response:
        if response.status_code == 200:
            res = check.check_rc(response)
            allure_assert.my_assert(res, api)
            return res[1]
        else:
            allure_assert.request_error(response.text, api)


class MyRequest(object):
    """二次封装request"""

    class Url(object):
        """参数在url中的接口"""

        def get(self, api):
            return client(method='get', url=api.get('url'), api=api)

        def put(self, api):
            return client(method='put', url=api.get('url'), api=api)

        def post(self, api):
            return client(method='post', url=api.get('url'), api=api)

        def dele(self, api):
            return client(method='delete', url=api.get('url'), api=api)

    class Params(object):
        """query类型参数入口"""

        def get(self, api):
            return client(method='get', url=api.get('url'), params=api.get('data'), api=api)

        def put(self, api):
            return client(method='put', url=api.get('url'), params=api.get('data'), api=api)

        def post(self, api):
            return client(method='post', url=api.get('url'), params=api.get('data'), api=api)

    class Json(object):
        """body类型参数入口"""

        def get(self, api):
            return client(method='get', url=api.get('url'), json=api.get('data'), api=api)

        def put(self, api):
            return client(method='put', url=api.get('url'), json=api.get('data'), api=api)

        def post(self, api):
            return client(method='post', url=api.get('url'), json=api.get('data'), api=api)

    class File(object):
        def get(self, api):
            return client(method='get', url=api.get('url'), file=api.get('data'), api=api)

        def put(self, api):
            return client(method='put', url=api.get('url'), file=api.get('data'), api=api)

        def post(self, api):
            return client(method='post', url=api.get('url'), file=api.get('data'), api=api)

    class Data(object):
        def get(self, api):
            return client(method='get', url=api.get('url'), data=api.get('data'), api=api)

        def put(self, api):
            return client(method='put', url=api.get('url'), data=api.get('data'), api=api)

        def post(self, api):
            return client(method='post', url=api.get('url'), data=api.get('data'), api=api)
