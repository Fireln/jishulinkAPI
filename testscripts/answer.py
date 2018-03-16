#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/16

from data.data.answer_data import AnswerData, keys
import allure
from tools import url, params, file, form

answer_data = AnswerData.data
answer_id = None


@allure.feature("问答")
@allure.story("发布问答")
class TestAnswer(object):

    @allure.testcase("发布问答")
    def publish(self):
        api = answer_data.get(keys.publish)
        res = form.post(api=api)
        if res:
            answer_id = res.get("ret")

    def test(self):
        print(answer_id)


if __name__ == '__main__':
    t = TestAnswer()
    t.publish()
    t.test()
