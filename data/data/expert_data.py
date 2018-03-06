#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/1

from ..keys import expert_keys
from . import eve
import random
import string


class ExpertGuid(object):
    keys = expert_keys.ExpertGuidKeys()

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
                     'asExpert': 'true',
                     }
        },
        keys.expert_false: {
            'url': eve.server + '/member/cert/expert4M/' + eve.user_id,
            'data': {'speciality': '测试数据',
                     'operator': 'admin',
                     'asExpert': 'false',
                     }
        },

    }


class ExpertContent(object):
    keys = expert_keys.ExpertContentKeys()
    data = {
        keys.cert_progress: {
            'url': eve.server + '/user/getCertProgress',
            'data': {'userId': eve.user_id, 'forOneself': 'false'}
        },
        keys.expert_recommend: {
            'url': eve.server + '/user/expertRecommend2',
        },
        keys.app_home_expert: {
            'url': eve.server + '/newHome/getAppHomeExperts',
            'data': {'userId': eve.user_id}
        },
        keys.expert_channel: {
            'url': eve.server + '/tpoint/aspect/expertChannel?aspect=APPLICATION&forApp=1&singleAlphabet=1&expertSelect=HIDDEN_TAGS',
        },
        keys.expert_popular_cities: {
            'url': eve.server + '/site/search/expertPopularCities',
        },
        keys.vocation_list: {
            'url': eve.server + '/expert_channel/getVocationList?begin=0&length=100',
        },
        keys.expert_search: {
            'url': eve.server + '/site/search/expert',
            'data': {
                'userId': eve.user_id,
                'begin': 0,
                'length': 30,
                'aspect': 'APPLICATION'
            }
        },
        keys.fuzzy: {
            'url': eve.server + '/tpoint/fuzzy?name=c',
        },
    }
