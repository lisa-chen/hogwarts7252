# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/6 14:30
# software: PyCharm
from faker import Faker
from logging import info


def get_userinfo(num=3):
    faker = Faker('zh_CN')
    result = []
    for item in range(num):
        username = faker.name()
        phone = faker.phone_number()
        info(f"添加的用户名为：{username},用户电话为{phone}")
        result.append((username, phone))
    return result


if __name__ == '__main__':
    cc = get_userinfo(5)
