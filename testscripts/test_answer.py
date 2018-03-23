#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/16

from data.data.answer_data import AnswerData, keys
import allure
from tools import url, params, file
from data.data import eve

answer_data = AnswerData.data
answer_id = eve.post_id
reply_id = None


@allure.feature("问答")
@allure.story("进入问答频道")
@allure.severity("critical")  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
class TestAnswer(object):

    @allure.testcase("问答广告")
    def test_ads(self):
        api = answer_data.get(keys.ads)
        url.get(api)

    @allure.testcase("答疑明星")
    def test_top_activity_users(self):
        api = answer_data.get(keys.top_activity_users)
        url.get(api)

    @allure.testcase("未解决提问")
    def test_searchy_false(self):
        api = answer_data.get(keys.search)
        params.get(api)

    @allure.testcase("已解决提问")
    def test_searchy_true(self):
        api = answer_data.get(keys.search)
        api["data"]["resolved"] = True
        params.get(api)

    @allure.testcase("关注的提问")
    def test_followed_qa(self):
        api = answer_data.get(keys.followed_qa)
        url.get(api)

    @allure.testcase("关注的板块")
    def test_followed_model(self):
        api = answer_data.get(keys.followed)
        url.get(api)

    @allure.testcase("获取提问页右侧技术标签")
    def test_top_navigation(self):
        api = answer_data.get(keys.top_navigation)
        url.get(api)


@allure.feature("问答")
@allure.story("进入问答详情")
@allure.severity("trivial")
class TestPost(object):

    @allure.testcase("发布问答")
    def test_publish(self):
        global answer_id
        api = answer_data.get(keys.publish)
        res = file.post(api=api)
        if res:
            answer_id = res.get("ret")

    @allure.testcase("问答详情")
    def test_open_post_detail(self):
        api = answer_data.get(keys.detail)
        api["url"] = api["url"].format(answer_id)
        url.get(api)

    @allure.testcase("是否点赞")
    def test_is_like(self):
        api = answer_data.get(keys.is_like)
        api["url"] = api["url"].format(answer_id)
        url.get(api)


@allure.feature("问答")
@allure.story("回复")
@allure.severity("critical")
class TestReplay(object):

    @allure.testcase("评论/回复")
    def test_replay(self):
        self.replay()
        self.replay_list()
        self.recommend()
        self.replay_next()
        self.chat()
        self.adopt_answer()
        self.delete_replay()

    @allure.step("进行评论")
    def replay(self):
        global reply_id
        api = answer_data.get(keys.reply)
        replyTo = ("replyTo", (None, answer_id))
        api["data"].append(replyTo)
        return file.post(api)

    @allure.step("进行回复")
    def replay_next(self):
        if reply_id:
            api = answer_data.get(keys.reply)
            replyTo = ("replyTo", (None, reply_id))
            api["data"].append(replyTo)
            return file.post(api)

    @allure.step("对话列表")
    def chat(self):
        if answer_id and reply_id:
            api = answer_data.get(keys.chat)
            api["url"] = api["url"].format(answer_id)
            return url.get(api)

    @allure.step("评论列表")
    def replay_list(self):
        global reply_id
        api = answer_data.get(keys.new_reply_list)
        api["url"] = api["url"].format(answer_id)
        res = url.get(api)
        if res:
            reply_list = res.get("ret").get("results")
            reply_id = reply_list[0].get("replyId")

    @allure.step("推荐")
    def recommend(self):
        if reply_id:
            api = answer_data.get(keys.recommend)
            api["url"] = api["url"].format(reply_id)
            url.put(api)

    @allure.step("采纳")
    def adopt_answer(self):
        if reply_id:
            api = answer_data.get(keys.adopt_answer)
            api["url"] = api["url"].format(reply_id)
            url.post(api)

    @allure.step("删除问答")
    def delete_replay(self):
        if reply_id:
            api = answer_data.get(keys.delete_replay)
            api["url"] = api["url"].format(answer_id)
            url.dele(api)


if __name__ == '__main__':
    t = TestReplay()
    t.test_replay()
