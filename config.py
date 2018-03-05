#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

class Main(object):
    server = "http://t.jishulink.com:8080/jishulink_test"


class Dev(Main):
    user_id = "577eecfc-1155-4d48-a90f-b990b21896e5"
    pass


class Release(Main):
    server = ''
    user_id = ''


def get_eve(eve):
    if eve == "dev":
        return Dev()
    else:
        return Release()
