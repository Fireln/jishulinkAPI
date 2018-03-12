#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/12


from data.data.home_data import HomeData, home_keys
import allure
from tools.my_request import MyRequest
from tools.allure_assert import AllureAssert
from tools.check_point import CheckPoint
import random
import string

home_data = HomeData.data
request = MyRequest()
allure_assert = AllureAssert()
check = CheckPoint()


@allure.feature("首页")
@allure.story("进入首页")
class TestHome(object):
    @allure.testcase("进入首页")
    def open_home(self):
        self.login()
        self.report_terminal_info()
        self.ordertask()
        self.latest_version()
        self.getAppHomeData()
        self.getUserGuideData()
        self.check_sign_status()
        self.new_feeds()
        self.app_version()
        self.lottery()

    @allure.step("自动登录")
    def login(self):
        api = home_data.get(home_keys.authenticate)
        request.Params().get(api=api)

    @allure.step("发送移动端信息")
    def report_terminal_info(self):
        api = home_data.get(home_keys.report_terminal_info)
        request.Url().get(api=api)

    @allure.step("获取用户协作消息")
    def ordertask(self):
        api = home_data.get(home_keys.ordertask)
        request.Url().get(api=api)

    @allure.step("获取APP最新版本信息")
    def latest_version(self):
        api = home_data.get(home_keys.latest_version)
        request.Url().get(api=api)

    @allure.step("用户引导")
    def getUserGuideData(self):
        api = home_data.get(home_keys.getUserGuideData)
        request.Url().get(api=api)

    @allure.step("登录信息")
    def check_sign_status(self):
        api = home_data.get(home_keys.check_sign_status)
        request.Url().get(api=api)

    @allure.step("getAppHomeData")
    def getAppHomeData(self):
        api = home_data.get(home_keys.getAppHomeData)
        request.Url().get(api=api)

    @allure.step("new_feeds")
    def new_feeds(self):
        api = home_data.get(home_keys.new_feeds)
        request.Url().get(api=api)

    @allure.step("lottery")
    def lottery(self):
        api = home_data.get(home_keys.lottery)
        request.Url().get(api=api)

    @allure.step("app_version")
    def app_version(self):
        api = home_data.get(home_keys.app_version)
        request.Url().get(api=api)


if __name__ == '__main__':
    t = TestHome()
    t.open_home()