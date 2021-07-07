# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 10:19
# software: PyCharm
from appium.webdriver.webdriver import WebDriver

from study_appium.appium_po.page.Userinfo import UserInfo
from study_appium.appium_po.page.bash_method import BaseMethod


class AddressBook(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_adduser(self):
        from study_appium.appium_po.page.AddUsers import AddUser
        ele = self.swipe_find("添加成员")
        ele.click()
        # self.find_elemet_click('//*[@text="添加成员"]')
        return AddUser(self.driver)

    def goto_userinfo(self, name):
        ele = self.swipe_find(name, 5)
        ele.click()
        return UserInfo(self.driver)

    def find_ele_exist(self, name):
        result = self.swipe_find(name, 3)
        return result
