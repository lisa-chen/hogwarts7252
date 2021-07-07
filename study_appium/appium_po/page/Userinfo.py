# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/7 10:00
# software: PyCharm
from study_appium.appium_po.page.bash_method import BaseMethod
from appium.webdriver.webdriver import WebDriver

class UserInfo(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def goto_uersinfo_list(self):
        from study_appium.appium_po.page.UserSetting import UserSetting

        self.find_elemet_click("//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout")
        return UserSetting(self.driver)