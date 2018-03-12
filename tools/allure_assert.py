#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/6
import allure


class AllureAssert(object):

    def my_assert(self, res, api):
        if res[0]:
            assert True
        else:
            if isinstance(res[1], dict):
                allure.attach("参数", "{0}".format(api))
                allure.attach("结果", "{0}".format(res[1]))
                assert AssertionError
            else:
                allure.attach("参数", "{0}".format(api))
                allure.attach("结果", "{0}".format(res[1]))
                assert AssertionError

    def request_error(self, api):
        allure.attach("参数", "{0}".format(api))
        allure.attach("结果", "请求失败或服务器超时")
        assert AssertionError
