#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from data.keys import user_keys
from data.data import eve
import random
import string

keys = user_keys.User()


class VipData(object):
    data = {
        keys.register: {
            'url': eve.server + '/user/register',
            'data':
                {
                    "password": "123456",
                    "verificationCode": "bobo",
                    "telephone": "171" + "".join(random.sample(string.digits, 8)),
                    "inviterUserId": 0,
                    "realname": "Test" + "".join(random.sample(string.ascii_letters, 4))
                }
        },
        keys.vip_info: {
            'url': eve.server + '/user/vip_info?userId=' + eve.user_id,
        },
        keys.base_info: {
            'url': eve.server + '/user/' + eve.user_id + '/baseinfo',
        },
        keys.user_profile: {
            'url': eve.server + '/user/' + eve.user_id + '/user_profile',
        }, keys.receive_award: {
            'url': eve.server + '/user/' + eve.user_id + '/receive_award',
        },
    }


if __name__ == '__main__':
    t = VipData()
    print(t.data.get('register'))
