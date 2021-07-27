# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/20 20:45
# software: PyCharm
import requests


class Base:
    corpid = 'ww2beeaa57277026f0'
    provider_secret = 'xRSsQC4dDq-GUig0Wo3b0m9sJJ0607yCvuC-9Aaj0Tc'

    def get_token(self):
        data = {
            "corpid": self.corpid,
            "corpsecret": self.provider_secret
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=data)
        return res.json().get("access_token")
