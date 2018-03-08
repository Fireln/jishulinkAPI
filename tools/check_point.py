#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/6


class CheckPoint(object):
    def check_rc(self, obj):
        """检查RC码，返回list类型，第一位用作判断接口调用正确性，第二位是请求结果"""
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
    print(test.check_rc('asd'))
