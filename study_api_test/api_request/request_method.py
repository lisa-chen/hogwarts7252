# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/20 20:46
# software: PyCharm
import requests

from study_api_test.api_request.base import Base


class wechartTag(Base):
    def __init__(self):
        self.access_token=self.get_token()

    def get_tags(self):
        ACCESS_TOKEN = self.access_token
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={ACCESS_TOKEN}")
        print(res.text)

    def create_tag(self):
        ACCESS_TOKEN = self.access_token
        data = {
            "tagname": "test003",
            "tagid": 1003
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={ACCESS_TOKEN}", json=data)
        print(res.text)
        return res

    def updata_tag(self):
        ACCESS_TOKEN = self.access_token
        data = {
            "tagname": "test1",
            "tagid": 13
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={ACCESS_TOKEN}", json=data)
        print(res.text)
        return res


if __name__ == "__main__":
    aa = wechartTag()
    print(aa.get_tags())
    print(aa.create_tag())
    # print(aa.updata_tag())
