#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

import requests
from testdata.data.expert import ExpertGuid, keys
from tools.tpoint import ExpertTpoint
import allure

data = ExpertGuid.data
expert_tpoint = ExpertTpoint()


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
            res = requests.put(url=url, params=api_data)
            response = res.json()
            assert response.get("rc") == 0
        except Exception:
            assert False

    @allure.testcase("用例名：成为专家")
    def test_become_expert(self):

        commit_res = self.commit()
        if commit_res == 0:
            true = self.expert_true
            if true == 0:
                self.expert_false
            else:
                assert False
        else:
            assert False

    @allure.step("申请成为专家")
    def commit(self):
        api = data.get(keys.commit)
        try:
            res = requests.post(url=api.get('url'))
            responst = res.json()
            rc = responst.get('rc')
            if rc == 0 or rc == 1:
                assert True
            else:
                assert False
        except Exception:
            assert False

    @allure.step("后台管理审核通过")
    def expert_true(self):
        api = keys.expert_true
        try:
            res = requests.post(url=api.get('url'), params=api.get('data'))
            responst = res.json()
            assert responst.get('rc') == 0
            return responst.get('rc')
        except Exception:
            assert False

    @allure.step("后台管理审核失败")
    def expert_false(self):
        api = keys.expert_false
        try:
            res = requests.post(url=api.get('url'), params=api.get('data'))
            responst = res.json()
            assert responst.get('rc') == 0
        except Exception:
            assert False


@allure.feature('专家频道')
@allure.story('专家频道')
class TestExpertContent(object):
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


if __name__ == '__main__':
    test = TestExpertGuid()
    test.commit()
