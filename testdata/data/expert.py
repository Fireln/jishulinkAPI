#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from ..keys import expert
from . import eve
import random
import string

keys = expert.ExpertGuidKeys()


class ExpertGuid(object):
    data = {
        keys.expert_label: {
            'url': eve.server + '/tpoint/aspect/expertChannel/flat',
        },
        keys.create_label: {
            'url': eve.server + '/tpoint/createOrUpdate/name',
            'data': {
                'userId': eve.user_id,
                'name': '测试' + ''.join(random.sample(string.ascii_letters, 4)),
                'aspect': random.choice(['Production', 'Application', 'Simulation', 'Craft', 'Software']),
            }
        },
        keys.modify_label: {
            'url': eve.server + '/user/' + eve.user_id + '/capability/add_with_name',
            'data': {'clearAll': 1, 'technicalPoint': '复合材料'}
        },
        keys.commit: {
            'url': eve.server + '/member/cert/expert/' + eve.user_id,
        },
        keys.expert_true: {
            'url': eve.server + '/member/cert/expert4M/' + eve.user_id,
            'data': {'speciality': '测试数据',
                     'operator': 'admin',
                     'asExpert': True,
                     }
        },
        keys.expert_false: {
            'url': eve.server + '/member/cert/expert4M/' + eve.user_id,
            'data': {'speciality': '测试数据',
                     'operator': 'admin',
                     'asExpert': False,
                     }
        },
        keys.expert_recommend: {
            'url': eve.server + '/user/expertRecommend2',
        }
    }
