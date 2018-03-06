#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/6


class CheckPoint(object):
    def check_rc(self, obj):
        try:
            response = obj.json()
            rc = response.get('rc')
            if rc == 0:
                return True, response
            else:
                return False, response
        except AttributeError:
            return False, obj


if __name__ == '__main__':
    test = CheckPoint()
    print(test.check_rc({'rc': 0, 'ret': ['asd']}))
