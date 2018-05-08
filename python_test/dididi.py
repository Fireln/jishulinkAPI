#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/4/19


def test(func):
    def waper(*args, **krgs):
        print("test")
        return func(*args, **krgs)

    return waper


class Test(object):

    @test
    def tsfa(self, x, y):
        print("666")


if __name__ == '__main__':
    t = Test()
    t.tsfa()
