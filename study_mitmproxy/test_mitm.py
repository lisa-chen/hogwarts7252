# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/14 18:00
# software: PyCharm
import json

import mitmproxy.http
from mitmproxy import http, ctx


class rewrite:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log(flow.request.pretty_url)
        if 'http://wttr.in/Dunedin' in flow.request.pretty_url:
            res = flow.response.text
            res=res.replace("Morning","hogwares").replace("Morning","Noon")
            #ctx.log(res)
            # json_data = json.loads(res)
            # ctx.log(str(json_data["msg"]["intern_info"][0]["minSalary"]))
            # ctx.log(str(json_data["msg"]["intern_info"][0]["maxSalary"]))
            # json_data["msg"]["intern_info"][0]["minSalary"] = json_data["msg"]["intern_info"][0]["minSalary"] * 2
            # json_data["msg"]["intern_info"][0]["maxSalary"] = json_data["msg"]["intern_info"][0]["maxSalary"] * 2
            # ctx.log(str(json_data["msg"]["intern_info"][0]["minSalary"]))
            # ctx.log(str(json_data["msg"]["intern_info"][0]["maxSalary"]))
            # ctx.log(res)
            flow.response.text = res
            # with open("data.txt","w",encoding='utf-8') as f:
            #     f.write(res)
            ctx.log(flow.response.text)


class Maplocal1:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if 'http://wttr.in/Dunedin' in \
                flow.request.pretty_url:
            with open("data.txt", "r", encoding='utf-8') as f:
                flow.response = http.HTTPResponse.make(
                    # 状态码响应
                    200,
                    # 数据体
                    f.read(),

                )


addons = [
    rewrite(), Maplocal1()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8888', '-s', __file__])
