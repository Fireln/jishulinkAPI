#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from data.keys import home_keys
from data.data import eve
import random
import string

home_keys = home_keys.Home()


class HomeData(object):
    data = {
        home_keys.authenticate: {
            'url': eve.server + '/user/authenticate/name',
            'data': {
                "password": "123456",
                "name": "13783783183",
                "device": "App",
            }
        },
        home_keys.report_terminal_info: {
            'url': eve.server + '/user/' + eve.user_id + '/report_terminal_info?terminalType=IOS&version=' + eve.app_version,
        },
        home_keys.ordertask: {
            'url': eve.server + '/ordertask/' + eve.user_id,
        },
        home_keys.latest_version: {
            'url': eve.server + 'app_version/check/latest_version?type=1',
        }, home_keys.getUserGuideData: {
            'url': eve.server + '/newHome/getUserGuideData?userId=' + eve.user_id,
        }, home_keys.check_sign_status: {
            'url': eve.server + '/sign/check_sign_status?userId=' + eve.user_id + '&clientType=APP',
        }, home_keys.getAppHomeData: {
            'url': eve.server + '/newHome/getAppHomeData',
        }, home_keys.new_feeds: {
            'url': eve.server + '/user/' + eve.user_id + '/new_feeds?begin=0&length=20',
        }, home_keys.lottery: {
            'url': eve.server + '/lottery/gain/' + eve.lotteryId,
        }, home_keys.app_version: {
            'url': eve.server + '/app_version/check?versionId=' + eve.app_version + '&type=1',
        },
    }


if __name__ == '__main__':
    t = HomeData()
    print(t.data.get('register'))
