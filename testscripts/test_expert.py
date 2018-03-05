#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

import requests
from testdata.data.expert import ExpertGuid, keys
from tools.tpoint import ExpertTpoint
import allure

data = ExpertGuid.data
expert_tpoint = ExpertTpoint()


class TestExpert(object):
    @allure.feature('专家频道')
    @allure.story('专家引导')
    class TestExpertGuid(object):

        @allure.testcase("用例名：引导页5各分类标签")
        def test_all_label(self):
            api = data.get(keys.expert_label)
            url = api.get('url')
            try:
                res = requests.get(url)
                response = res.json()
                assert response.get("rc") == 0
            except Exception:
                assert False

        @allure.testcase("用例名：自定义分类")
        def test_create_label(self):
            api = data.get(keys.create_label)
            url = api.get('url')
            api_data = api.get('data')
            allure.attach("用例参数", "{0}".format(api))
            try:
                res = requests.post(url=url, params=api_data)
                response = res.json()
                assert response.get("rc") == 0
            except Exception:
                assert False


        @allure.testcase("用例名：修改分类")
        def test_modify_label(self):
            api = data.get(keys.modify_label)
            url = api.get('url')
            api_data = api.get('data')
            allure.attach("用例参数", "{0}".format(api))
            try:
                res = requests.post(url=url, params=api_data)
                response = res.json()
                assert response.get("rc") == 0
            except Exception:
                assert False

    @allure.feature('专家频道')
    @allure.story('专家频道')
    class TestExpertGuid(object):

        @allure.testcase("用例名：专家频道首页推荐专家")
        def test_expert_recommend(self):
            api = data.get(keys.expert_recommend)
            url = api.get('url')
            api_data = api.get('data')
            allure.attach("用例参数", "{0}".format(api))
            try:
                res = requests.post(url=url, params=api_data)
                response = res.json()
                assert response.get("rc") == 0
            except Exception:
                assert False
