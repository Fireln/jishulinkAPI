#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

class Main(object):
    server = "http://t.jishulink.com:8002/jishulink"


class Dev(Main):
    user_id = "7515dec3-3668-4020-9777-9d5524bf89b9"
    user_id_two = "64596392-2c82-4da9-9932-40a83024b155"
    lotteryId = "0329aba0-ce77-4233-85b2-f16c5e564e05"
    post_id = "aeace18f-d26f-4ff8-af7a-8f48d6dc3146"
    app_version = "4.2.0"
    mysql = {
        "host": "120.55.131.33",
        "user": "jishulink_test",
        "pwd": "jishulink1194",
        "base": "jishulink-view-test"

    }
    business = {
        "pay_answer_id": "pa10619",
        "cooperation_id": "pa10619",
        "live_id": "pa10619",
    }
    ali_oss = {
        "AK": "",
        "AkS": ""
    }
    videos = ["5a5591cd421aa9644c788e71", "5a3b5414421aa934614af54d"]
    t_point_id = "98AA695F-4C63-4701-BDD1-0F8FC33030B6"


class Release(Main):
    server = 'http://cloud.jishulink.com/jishulink'
    user_id = '7dd9bebb-aa05-409a-8568-44f8e8bad259'
    user_id_two = "b2eb07dd-9a1a-47c2-922b-0487dcd2749f"
    lotteryId = "85f24b3b-05a5-4c07-a15a-96817d3419a9"
    post_id = "e2e04bf1-1cd0-4f70-8ee1-b8b6d23087d3"
    app_version = "4.1.8"
    business = {
        "pay_answer_id": "pa10619",
        "cooperation_id": "pa10619",
        "live_id": "pa10619",
    }


def get_eve(eve):
    if eve == "dev":
        return Dev()
    else:
        return Release()
