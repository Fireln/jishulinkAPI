#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

import requests
from data.data import eve
from data.data.expert_data import ExpertGuid, ExpertContent
from tools.allure_assert import allure, AllureAssert
from tools.check_point import CheckPoint
from data.keys.expert_keys import ExpertContentKeys, ExpertGuidKeys
from tools.my_request import MyRequest

my_request = MyRequest()

data = ExpertGuid.data
content_data = ExpertContent.data
check = CheckPoint()
allure_assert = AllureAssert()


@allure.feature('专家频道')
@allure.story('专家引导')
class TestExpertGuid(object):
    @allure.testcase("用例名：引导页5各分类标签")
    def test_all_label(self):
        api = data.get(ExpertGuidKeys.expert_label)
        my_request.Url().post(api=api)

    @allure.testcase("用例名：自定义分类")
    def test_create_label(self):
        api = data.get(ExpertGuidKeys.create_label)
        my_request.Params().post(api=api)

    @allure.testcase("用例名：修改分类")
    def test_modify_label(self):
        api = data.get(ExpertGuidKeys.modify_label)
        my_request.Params().put(api=api)

    @allure.testcase("用例名：专家审核")
    def test_become_expert(self):

        commit_res = self.commit()
        if isinstance(commit_res, dict):
            assert False
        elif isinstance(commit_res, str):
            assert False, '接口异常'
        else:
            self.expert_true()
            self.expert_false()

    @allure.step("申请成为专家")
    def commit(self):
        api = data.get(ExpertGuidKeys.commit)
        try:
            res = requests.post(url=api.get('url'))
            responst = res.json()
            rc = responst.get('rc')
            if rc == 0 or rc == 1:
                assert True
            else:
                return rc
        except Exception:
            return api

    @allure.step("后台审核专家")
    def expert_true(self):
        api = data.get(ExpertGuidKeys.expert_true)
        my_request.Params().post(api=api)

    @allure.step("后台管理审核失败")
    def expert_false(self):
        api = data.get(ExpertGuidKeys.expert_false)
        my_request.Params().post(api=api)


@allure.feature('专家频道')
@allure.story('专家频道内容')
class TestExpertContent(object):
    @allure.testcase("用例名：专家频道首页推荐专家")
    def test_expert_recommend(self):
        api = content_data.get(ExpertContentKeys.expert_recommend)
        my_request.Params().post(api=api)

    @allure.testcase("用例名：查看用户认证的完成进度，包括个人描述与微信绑定、各种认证状态")
    def test_cert_process(self):
        api = content_data.get(ExpertContentKeys.cert_progress)
        my_request.Params().post(api=api)

    @allure.testcase("用例名：移动端专家频道首页banner")
    def test_app_expert_banner(self):
        api = content_data.get(ExpertContentKeys.app_home_expert)
        my_request.Params().post(api=api)

    @allure.testcase("用例名：获取某个一级分类下的分类")
    def test_expert_channel(self):
        api = content_data.get(ExpertContentKeys.expert_channel)
        my_request.Params().post(api=api)

    @allure.testcase("用例名：按分类搜索专家")
    def test_expert_search(self):
        self.expert_search_one()
        self.expert_search_two()
        self.expert_search_all()
        self.fuzzy()
        self.expert_search_keyword()
        self.expert_city()
        self.vocation_list()

    @allure.step("一级分类搜索专家")
    def expert_search_one(self):
        api = content_data.get(ExpertContentKeys.expert_search)
        my_request.Params().post(api=api)

    @allure.step("按分类ID搜索专家")
    def expert_search_two(self):
        api = content_data.get(ExpertContentKeys.expert_search)
        api.get('data')['tPointIds'] = 'C255B987-2BDD-4881-BA2C-1EE736EF44C0'
        my_request.Params().post(api=api)

    @allure.step("所有可搜索项进行搜索")
    def expert_search_all(self):
        api = content_data.get(ExpertContentKeys.expert_search)
        api.get('data')['tPointIds'] = '7FE5042A-9474-40A5-A11D-A3D528E4E982,9147F030-BAF1-4E5F-9B1E-57D874A28C70'
        api.get('data')['category'] = 'PAY_ANSWER_EXPERT'
        api.get('data')['cities'] = '杭州市'
        api.get('data')['degrees'] = 'BACHELOR'
        api.get('data')['ranges'] = '0TO5'
        my_request.Params().post(api=api)

    @allure.step("关键字搜索")
    def expert_search_keyword(self):
        api = content_data.get(ExpertContentKeys.expert_search)
        api['data'] = {
            'userId': eve.user_id,
            'begin': 0,
            'length': 30,
            'keyword': 'CAD'
        }
        my_request.Params().post(api=api)

    @allure.step("城市搜索项")
    def expert_city(self):
        api = content_data.get(ExpertContentKeys.expert_popular_cities)
        my_request.Params().post(api=api)

    @allure.step("获取行业列表，按手动排序")
    def vocation_list(self):
        api = content_data.get(ExpertContentKeys.vocation_list)
        my_request.Params().post(api=api)

    @allure.step("智能提示")
    def fuzzy(self):
        api = content_data.get(ExpertContentKeys.fuzzy)
        my_request.Params().post(api=api)


if __name__ == '__main__':
    test = TestExpertGuid()
    test.test_all_label()
