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
        }
    }
