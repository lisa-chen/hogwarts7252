# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 15:57
# software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from logging import info


class BaseMethod:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_element(self, xpath):

        info(f"获取元素{xpath}")
        return self.driver.find_element(MobileBy.XPATH, xpath)

    def find_elemet_click(self, xpath):
        info(f"点击元素{xpath}")
        self.driver.find_element(MobileBy.XPATH, xpath).click()

    def find_elemet_sendkey(self, xpath, value):
        info(f"获取元素{xpath}并输入内容{value}")
        self.driver.find_element(MobileBy.XPATH, xpath).send_keys(value)

    def back_num(self, num):
        info(f"返回{num}次")
        for index in range(num):
            self.driver.implicitly_wait(1)
            self.driver.back()
        self.driver.implicitly_wait(15)

    def back_xpath(self, xpath):
        info(f"按返回按钮直到道{xpath}出现，最多返回10次")
        origin_page = True
        num = 10
        while num and origin_page:
            self.driver.implicitly_wait(5)
            try:
                ele = self.find_element(xpath)
                origin_page = False
            except:
                self.driver.back()
                info(f"按返回按钮直到道{xpath}出现，返回第{10 - num}次")
                num = num - 1
        self.driver.implicitly_wait(15)

    def wait_element(self, xpath):
        info(f"等待{xpath}出现")
        WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.XPATH, xpath))

    def swipe_find(self, text, num=5):
        info(f"查找{text}元素")
        self.driver.implicitly_wait(1)
        for item in range(num):
            try:

                # element = self.driver.find_element(MobileBy.XPATH, f"//*[contains(@text,{text})]")
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(15)
                return element
            except:
                info(f"下滑第{item + 1}次{text}包含该文案元素未出现")
                size = self.driver.get_window_size()
                x_len = size['width']
                y_len = size['height']
                start_x_len = x_len * 0.5
                start_y_len = y_len * 0.8
                end_x_len = start_x_len
                end_y_len = y_len * 0.3
                duration = 2000
                self.driver.swipe(start_x_len, start_y_len, end_x_len, end_y_len, duration)
        return "元素不存在"
