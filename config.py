#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

class Main(object):
    server = "http://t.jishulink.com:8002/jishulink"


class Dev(Main):
    user_id = "7515dec3-3668-4020-9777-9d5524bf89b9"
    lotteryId = "0329aba0-ce77-4233-85b2-f16c5e564e05"
    app_version = "4.2.0"
    pass


class Release(Main):
    server = ''
    user_id = ''
    lotteryId = "0329aba0-ce77-4233-85b2-f16c5e564e05"
    app_version = "4.2.0"


def get_eve(eve):
    if eve == "dev":
        return Dev()
    else:
        return Release()
