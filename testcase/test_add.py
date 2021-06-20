# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/20 10:48
# software: PyCharm
import pytest
from user_method.calculator import Calculator
from user_method.getyamldata import openyaml


class TestCalculator:
    def setup_class(self):
        print("测试开始")

    def teardown_class(self):
        print("测试结束")

    @pytest.mark.parametrize("casename,num1,num2,exp", openyaml("add"))
    def test_add(self, casename, num1, num2, exp):
        result = Calculator.add(num1, num2)
        if isinstance(result,(int,float)):
            assert result - exp < 0.00000001
        else:

            assert str(result) == str(exp)



    @pytest.mark.parametrize("casename,num1,num2,exp", openyaml("div"))
    def test_div(self, casename, num1, num2, exp):
        result = Calculator.div(num1, num2)
        assert str(result) == str(exp)

    def teardown_class(self):
        print("测试结束")
