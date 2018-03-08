#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from data.data.user_data import VipData, keys
import allure
from tools.my_request import MyRequest
from tools.allure_assert import AllureAssert
from tools.check_point import CheckPoint
import random
import string
import requests

vip_data = VipData.data
request = MyRequest()
allure_assert = AllureAssert()
check = CheckPoint()


@allure.feature('用户模块')
@allure.story('vip相关')
class TestUserVip(object):
    @allure.testcase("用例名：进入个人中心")
    def test_open_center(self):
        self.vip_info()
        self.base_info()
        self.profile_info()

    @allure.step("获取用户VIP信息")
    def vip_info(self):
        api = vip_data.get(keys.vip_info)
        request.Url().get(api=api)

    @allure.step("获取用户baseinfo")
    def base_info(self):
        api = vip_data.get(keys.base_info)
        request.Url().get(api=api)

    @allure.step("获取用户profile")
    def profile_info(self):
        api = vip_data.get(keys.user_profile)
        request.Url().get(api=api)

    @allure.testcase("邀请注册获得VIP")
    def test_three_mon_vip(self):
        self.regiest()

    @allure.step("注册新账号")
    def regiest(self):
        api = vip_data.get(keys.register)
        api.get('data')['telephone'] = "171" + "".join(random.sample(string.digits, 8))
        api.get('data')['realname'] = "Test" + "".join(random.sample(string.ascii_letters, 4))
        res = request.Json().post(api=api)
        if res.get('rc') != 0:
            return self.regiest()

    @allure.step("三个人接收邀请")
    def send(self):
        pass

    @allure.step("五个人接收邀请")
    def send(self):
        pass

    @allure.step("十人接收邀请")
    def send(self):
        pass

    @allure.step("检查VIP时间")
    def send(self):
        pass


if __name__ == '__main__':
    t = TestUserVip()
    t.test_open_center()
