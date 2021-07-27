# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/14 17:48
# software: PyCharm
import mitmproxy
from mitmproxy import ctx
from mitmproxy import http, ctx


class MitmSxs:
    def request(self, flows: mitmproxy.http.HTTPFlow):
        ctx.log(flows.request.url)
        if "http://sit1-sxs-web.mshare.cn/" in flows.request \
                .pretty_url:
            ctx.log(flows.request.url)
            ctx.log(flows.response)


# 插件
# 格式 list ，list中包我们需要使用的实例
addons = [
    MitmSxs()
]
if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8888', '-s', __file__])
