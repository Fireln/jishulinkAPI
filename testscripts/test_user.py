#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from data.data.user_data import VipData, keys
import allure
from tools.my_request import MyRequest
from tools.allure_assert import AllureAssert
from tools.check_point import CheckPoint
from tools import url
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

    @allure.testcase("注册")
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

    @allure.testcase("领取奖励金")
    def test_receive_award(self):
        api = vip_data.get(keys.receive_award)
        with requests.get(url=api.get('url')) as response:
            if response.status_code == 200:
                data = response.json()
                if data.get('rc') == 0:
                    assert True
                elif data.get('rc') == 1 and data.get('ret') == "仅在读工科生可参与该活动":
                    assert True
                else:
                    assert False
            else:
                allure_assert.request_error(response.status_code, api)


if __name__ == '__main__':
    t = TestUserVip()
    t.regiest()
