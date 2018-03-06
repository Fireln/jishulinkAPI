#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from ..keys import user_keys
from . import eve
import random
import string

keys = user_keys.Vip()


class VipData(object):
    data = {
        keys.vip_info: {
            'url': eve.server + '/user/vip_info',
            'data': {'userId': eve.user_id}
        },
    }
