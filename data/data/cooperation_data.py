#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/14


from ..keys import cooperation_keys
from . import eve
import random
import string


class CooperationData(object):
    keys = cooperation_keys.CooperationKeys()

    data = {
        keys.publish: {
            "name": "申请开通协作",
            "url": eve.server + "/answer/publish/new",
            "data": {
                "available": True,
                "publish": True,
                "price": 500,
                "description": "测试测试测试测试测试测试测试测试测试测试测试",
                "authorId": eve.user_id
            }
        }
    }
