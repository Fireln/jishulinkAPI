#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/2


class ExpertTpoint(object):
    """专家频道分类"""
    def get_tpoint(self, response):
        return response.get('ret')[0]

