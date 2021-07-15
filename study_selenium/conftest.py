# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/29 15:38
# software: PyCharm
import pytest


def get_list_value(driver,xpath,num=5):
    # 获取通讯录列表所有值
    #eles = driver.find_elements_by_xpath('//*[@id="member_list"]/tr/td/span')
    eles = driver.find_elements_by_xpath(xpath)
    result = []
    index = 0
    temp_list = []
    for item in eles:
        name = item.get_attribute("textContent")
        temp_list.append(name)
        index = index + 1
        if index % num == 0:
            result.append(temp_list)
            temp_list = []
    return result