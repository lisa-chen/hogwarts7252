# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/7 10:02
# software: PyCharm
from study_appium.appium_po.page.bash_method import BaseMethod
from appium.webdriver.webdriver import WebDriver


class UserSetting(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto_edit_detaiinfo(self):
        from study_appium.appium_po.page.EditUserDetail import EditUserDetail

        self.find_elemet_click("//*[@text='编辑成员']")
        return EditUserDetail(self.driver)
