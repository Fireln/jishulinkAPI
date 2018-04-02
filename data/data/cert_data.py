#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Fireln on 2018/3/28
from data.keys.cert_Keys import CertKeys
from data.data import eve

keys = CertKeys()


class CertData(object):
    def __init__(self, user_id, tel):
        self.data = {
            keys.real_name: {
                "url": eve.server + "/member/cert/identity/{}".format(user_id),
                "data": [
                    ("telephone", (None, tel)),
                    ("identityNumber", (None, "330304199407213323")),
                    ("realname", (None, "周依依")),
                    ("allowPublic", (None, "true")),
                ]
            },
            keys.career: {
                "url": eve.server + "/member/cert/career/{}".format(user_id),
                "data": [
                    ("vocation", (None, "电子电器")),
                    ("workAge", (None, "10")),
                    ("workUnit", (None, "杭州前缀网络科技有限公司")),
                    ("allowPublic", (None, "false")),
                    ("duty", (None, "测试")),
                    ("socialTitles", (None, "")),
                ]
            },
            keys.review: {
                "url": eve.server + "/member/cert/approve/{}".format(user_id),
                "data": {"operator": "admin", "category": "CAREER", "certId": ""}
            },
            keys.education: {
                "url": eve.server + "/member/cert/education/{}".format(user_id),
                "data": [
                    ("institution", (None, "浙江大学")),
                    ("onStudy", (None, "true")),
                    ("degree", (None, "BACHELOR")),
                    ("major", (None, "计算机")),
                ]

            }
        }
