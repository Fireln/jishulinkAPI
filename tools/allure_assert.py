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
                assert False, "rc状态码不为0"
            else:
                allure.attach("参数", "{0}".format(api))
                allure.attach("结果", "{0}".format(res[1]))
                assert False, "没有rc码返还，无法定位错误"

    def request_error(self, status, api):
        allure.attach("参数", "{0}".format(api))
        assert False, "接口调用失败，错误为：{}".format(status)
