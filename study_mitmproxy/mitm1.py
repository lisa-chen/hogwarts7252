# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/14 17:48
# software: PyCharm

from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

class Counter_1:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("哈哈哈 %d flows" % self.num)

# 插件
# 格式 list ，list中包我们需要使用的实例
addons = [
    Counter(),Counter_1()
]