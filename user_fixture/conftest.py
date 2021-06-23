# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/22 15:14
# software: PyCharm
import logging

import yaml
from user_method.base_path import *
import pytest
from user_method.calculator import *


def openyaml(filename):
    file_path = os.path.join(TEST_DATA, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(params=openyaml("add"))
def getdata_add(request):
    print(request.param)
    print("获取数据" + str(request))
    return request.param


@pytest.fixture(params=openyaml("div"))
def getdata_div(request):
    print(request.param)
    print("获取数据" + str(request))
    return request.param


@pytest.fixture(scope="class")
def get_Calc_object():
    logging.info("开始计算")
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")
    logging.info("结束计算")
