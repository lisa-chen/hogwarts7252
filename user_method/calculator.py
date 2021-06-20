# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/20 10:29
# software: PyCharm

import string
from decimal import Decimal

class Calculator:

    def add(self, num1, num2):
        """

        :param num1: 相加数1
        :param num2: 相加数2
        :return: 返回两个数之和
        """
        if not (isinstance(num1,(float,int)) and isinstance(num2,(float,int))):
            return "数据类型不对请重新输入"

        return num1 + num2

    def div(self, num1, num2):
        """

        :param num1: 除数
        :param num2: 被除数
        :return: 被除数/除数
        """
        if not (isinstance(num1,(float,int)) and isinstance(num2,(float,int))):
            return "数据类型不对请重新输入"
        if num2 == 0:
            return "除数不能为0"
        return num1 / num2


Calculator = Calculator()
