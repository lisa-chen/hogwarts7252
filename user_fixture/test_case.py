# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/20 10:48
# software: PyCharm
import logging

import pytest
from user_method.calculator import Calculator
from user_method.getyamldata import openyaml
import allure

logging.INFO

@allure.feature("测试计算类")
class TestCalculator:

    @allure.title("{getdata_add[0]}")
    def test_add(self, get_Calc_object, getdata_add):
        logging.info(f"预期结果  {getdata_add[0]}：{getdata_add[1]}+{getdata_add[2]}={getdata_add[3]}")

        result = get_Calc_object.add(getdata_add[1], getdata_add[2])
        logging.info(f"运行结果  {getdata_add[0]}：{getdata_add[1]}+{getdata_add[2]}={result}")
        if isinstance(result, (int, float)):
            assert result - getdata_add[3] < 0.00000001
        else:
            assert str(result) == str(getdata_add[3])

    @allure.title("{getdata_div[0]}")
    def test_div(self, get_Calc_object, getdata_div):
        logging.info(f"预期结果  {getdata_div[0]}：{getdata_div[1]}/{getdata_div[2]}={getdata_div[3]}")
        result = get_Calc_object.div(getdata_div[1], getdata_div[2])
        logging.info(f"运行结果  {getdata_div[0]}：{getdata_div[1]}/{getdata_div[2]}={result}")
        if isinstance(result, (int, float)):
            assert result - getdata_div[3] < 0.00000001
        else:
            assert str(result) == str(getdata_div[3])
