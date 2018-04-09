#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/4/9

from .api import course
import allure

course_api = course.CourseApi()
course_id = None
publish_res = None
payment_res = None


@allure.feature("视频课程")
@allure.story("发布课程")
class TestVideoCourse(object):
    @allure.testcase("创建课程")
    def test_create(self):
        global course_id
        global publish_res
        course_id = course_api.create()
        if course_id:
            if course_api.add_videos(course_id):
                if course_api.publish(course_id):
                    publish_res = True

    @allure.testcase("更新课程")
    def test_modify(self):
        if publish_res:
            course_api.update(course_id)
            course_api.add_tpoint(course_id)
            course_api.remove_tpoint(course_id)
            course_api.info(course_id)
            video_id = course_api.videos(course_id)
            if video_id:
                course_api.down_video(video_id)
                course_api.up_video(video_id)
                course_api.signed_url(course_id, video_id)
                course_api.update_charge_status(course_id, video_id)


@allure.feature("视频课程")
@allure.story("购买课程")
class TestPayment(object):
    @allure.testcase("支付订单")
    def test_payment(self):
        global payment_res
        if publish_res:
            order_id = course_api.place(course_id)
            if order_id:
                if course_api.payment(order_id):
                    payment_res = True

    @allure.testcase("订单管理")
    def test_order(self):
        if publish_res:
            order_id = course_api.place(course_id)
            if order_id:
                course_api.order_info(order_id)
                course_api.customer_orders(order_id)
                course_api.close(order_id)
                course_api.remove(order_id)


@allure.feature("视频课程")
@allure.story("购买后操作")
class TestPaymentOut(object):

    @allure.testcase("投票评论等操作")
    def test_vote(self):
        if payment_res:
            course_api.reply(course_id)
            course_api.reply_list(course_id)
            course_api.checkUserId(course_id)
            course_api.vote(course_id)
