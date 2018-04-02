#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/29
from data.data import eve
import random
import string


class Auth(object):
    tel = "".join(random.sample(string.digits, 8)),
    data = {
        "regiest": {
            "url": eve.server + "/user/register",
            "data": {
                "telephone": None,
                "password": "111111",
                "verificationCode": "bobo",
                "realname": None,
                "inviterUserId": 0
            }
        }
    }
