# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/7 10:04
# software: PyCharm
from study_appium.appium_po.page.Userinfo import UserInfo
from study_appium.appium_po.page.bash_method import BaseMethod
from appium.webdriver.webdriver import WebDriver
from time import sleep

class EditUserDetail(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def delete_user(self):
        from study_appium.appium_po.page.AddressBook import AddressBook

        ele = self.swipe_find("删除成员")
        ele.click()
        self.find_elemet_click("//*[@text='确定']")
        sleep(1)
        return AddressBook(self.driver)
