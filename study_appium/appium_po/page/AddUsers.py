# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 10:19
# software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from study_appium.appium_po.page.bash_method import BaseMethod


class AddUser(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto_edituser(self):
        from study_appium.appium_po.page.EditUser import EditUser
        self.wait_element('//*[@text="手动输入添加"]')
        self.find_elemet_click('//*[@text="手动输入添加"]')
        return EditUser(self.driver)

    def get_reslut(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

