#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/6
import allure


class AllureAssert(object):
    """
    简单封装allure断言
    """

    def my_assert(self, res, api):
        """rc码检查，当前只判断rc==0时正确"""
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
        """接口调用http状态码不为200时调用"""
        allure.attach("参数", "{0}".format(api))
        assert False, "接口调用失败，错误为：{}".format(status)

    def error_message(self, error_message):
        """测试套件执行前提未达成时调用"""
        assert False, "测试用例执行失败，原因是：{}".format(error_message)
