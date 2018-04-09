#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/4/8

from data.data import course_data
from tools import url, params, file, json
import allure


class CourseApi(object):

    def __init__(self):
        self.keys = course_data.c_keys
        self.data = course_data.CourseData().data

    @allure.step("发布课程")
    def create(self):
        api = self.data.get(self.keys.create)
        res = file.post(api)
        if res:
            return res.get("ret")

    @allure.step("向课程中添加视频")
    def add_videos(self, course_id):
        api = self.data.get(self.keys.add_videos)
        api["url"] = api.get("url").format(course_id=course_id)
        json.post(api)

    @allure.step("发布课程")
    def publish(self, course_id):
        api = self.data.get(self.keys.publish)
        api["url"] = api.get("url").format(course_id=course_id)
        url.get(api)

    @allure.step("修改课程")
    def update(self, course_id):
        api = self.data.get(self.keys.update)
        api["url"] = api.get("url").format(course_id=course_id)
        file.post(api)

    @allure.step("添加技术点")
    def add_tpoint(self, course_id):
        api = self.data.get(self.keys.add_tpoint)
        api["url"] = api.get("url").format(course_id=course_id)
        url.get(api)

    @allure.step("移除技术点")
    def remove_tpoint(self, course_id):
        api = self.data.get(self.keys.remove_tpoint)
        api["url"] = api.get("url").format(course_id=course_id)
        url.get(api)

    @allure.step("课程详情")
    def info(self, course_id):
        api = self.data.get(self.keys.info)
        api["url"] = api.get("url").format(course_id=course_id)
        url.get(api)

    @allure.step("课程视频列表")
    def videos(self, course_id):
        api = self.data.get(self.keys.videos)
        api["url"] = api.get("url").format(course_id=course_id)
        res = url.get(api)
        if res:
            return res.get("ret").get("results")[0].get("videoId")

    @allure.step("更改视频排序，上升指定视频序列")
    def up_video(self, course_id, video_id):
        api = self.data.get(self.keys.up_video)
        api["url"] = api.get("url").format(course_id=course_id, video_id=video_id)
        url.get(api)

    @allure.step("更改视频排序，下降指定视频序列")
    def down_video(self, course_id, video_id):
        api = self.data.get(self.keys.down_video)
        api["url"] = api.get("url").format(course_id=course_id, video_id=video_id)
        url.get(api)

    @allure.step("生成订单")
    def place(self, course_id):
        api = self.data.get(self.keys.place)
        api["url"] = api.get("url").format(course_id=course_id)
        res = url.get(api)
        if res:
            return res.get("ret")

    @allure.step("取消订单")
    def close(self, order_id):
        api = self.data.get(self.keys.close)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("删除订单")
    def remove(self, order_id):
        api = self.data.get(self.keys.remove)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("订单信息")
    def order_info(self, order_id):
        api = self.data.get(self.keys.order_info)
        api["url"] = api.get("url").format(order_id=order_id)
        url.get(api)

    @allure.step("订单列表")
    def customer_orders(self):
        api = self.data.get(self.keys.customer_orders)
        url.get(api)

    @allure.step("支付订单")
    def payment(self, order_id):
        api = self.data.get(self.keys.payment)
        api["data"]["orderId"] = order_id
        return json.post(api)

    @allure.step("评论课程")
    def reply(self, course_id):
        api = self.data.get(self.keys.reply)
        api["url"] = api.get("url").format(course_id=course_id)
        return json.post(api)

    @allure.step("评论列表")
    def reply_list(self, course_id):
        api = self.data.get(self.keys.reply_list)
        api["url"] = api.get("url").format(course_id=course_id)
        return url.get(api)

    @allure.step("获取课程里的视频播放地址等信息")
    def signed_url(self, course_id, video_id):
        api = self.data.get(self.keys.signedUrl)
        api["url"] = api.get("url").format(course_id=course_id, video_id=video_id)
        return url.get(api)

    @allure.step("设置课程视频是否为免费")
    def update_charge_status(self, course_id, video_id):
        api = self.data.get(self.keys.update_charge_status)
        api["url"] = api.get("url").format(course_id=course_id)
        api["data"]["videoId"] = video_id
        return params.get(api)

    @allure.step("判断用户是否已购买课程")
    def checkUserId(self, course_id):
        api = self.data.get(self.keys.checkUserId)
        api["url"] = api.get("url").format(course_id=course_id)
        return url.get(api)

    @allure.step("投票")
    def vote(self, course_id):
        api = self.data.get(self.keys.vote)
        api["url"] = api.get("url").format(course_id=course_id)
        return params.get(api)


if __name__ == '__main__':
    t = CourseApi()
    print(t.vote("c10922"))
