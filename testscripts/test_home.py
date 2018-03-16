#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/12


from data.data.home_data import HomeData, home_keys
import allure
from tools import url, params

home_data = HomeData.data


@allure.feature("首页")
@allure.story("进入首页")
class TestHome(object):

    @allure.testcase("自动登录")
    def test_login(self):
        api = home_data.get(home_keys.authenticate)
        params.get(api=api)

    @allure.testcase("发送移动端信息")
    def test_report_terminal_info(self):
        api = home_data.get(home_keys.report_terminal_info)
        url.get(api=api)

    @allure.testcase("获取用户协作消息")
    def test_ordertask(self):
        api = home_data.get(home_keys.ordertask)
        url.get(api=api)

    @allure.testcase("获取APP最新版本信息")
    def test_latest_version(self):
        api = home_data.get(home_keys.latest_version)
        url.get(api=api)

    @allure.testcase("用户引导")
    def test_getUserGuideData(self):
        api = home_data.get(home_keys.getUserGuideData)
        url.get(api=api)

    @allure.testcase("登录信息")
    def check_sign_status(self):
        api = home_data.get(home_keys.check_sign_status)
        url.get(api=api)

    @allure.testcase("getAppHomeData")
    def test_getAppHomeData(self):
        api = home_data.get(home_keys.getAppHomeData)
        url.get(api=api)

    @allure.testcase("new_feeds")
    def test_new_feeds(self):
        api = home_data.get(home_keys.new_feeds)
        url.get(api=api)

    @allure.testcase("lottery")
    def test_lottery(self):
        api = home_data.get(home_keys.lottery)
        url.get(api=api)

    @allure.testcase("app_version")
    def test_app_version(self):
        api = home_data.get(home_keys.app_version)
        url.get(api=api)


if __name__ == '__main__':
    t = TestHome()
    t.test_app_version()
