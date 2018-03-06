#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

import requests
from data.data.vip_data import VipData, keys
import allure

data = VipData.data


@allure.feature('用户vip')
@allure.story('vip详情')
class TestUserVip(object):
    @allure.testcase("用例名：获取vip信息")
    def test_vip_info(self):
        api = data.get(keys.vip_info)
        url = api.get('url')
        params = api.get('data')
        try:
            res = requests.get(url, params=params)
            response = res.json()
            assert response.get("rc") == 0
        except Exception:
            assert False
