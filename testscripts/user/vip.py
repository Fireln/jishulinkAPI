#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/8


class Vip():

    def __init__(self):
        self.data = None
        self.keys = None

    @allure.step("获取用户VIP信息")
    def vip_info(self):
        api = self.data.get(self.keys.vip_info)
        request.Url().get(api=api)

    @allure.step("获取用户baseinfo")
    def base_info(self):
        api = vip_data.get(self.keys.base_info)
        request.Url().get(api=api)

    @allure.step("获取用户profile")
    def profile_info(self):
        api = vip_data.get(keys.user_profile)
        request.Url().get(api=api)
