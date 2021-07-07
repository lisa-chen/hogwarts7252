# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 10:22
# software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from time import sleep

from study_appium.appium_po.page.bash_method import BaseMethod


class EditUser(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def edit_user(self, name, phone):
        '''

        :param name: 需要添加的用户名
        :param phone: 需要添加的电话号码
        :return: 返回到添加联系人页面
        '''
        from study_appium.appium_po.page.AddUsers import AddUser
        self.wait_element('//*[contains(@text,"姓名")]/../*[contains(@text,"必填")]')
        self.find_elemet_sendkey('//*[contains(@text,"姓名")]/../*[contains(@text,"必填")]', name)
        self.find_elemet_sendkey('//*[contains(@text,"手机")]/..//*[contains(@text,"必填")]', phone)
        self.find_elemet_click('//*[@text="保存后自动发送邀请通知"]')
        self.find_elemet_click('//*[@text="保存"]')


    def edit_user_success(self,name,phone):
        self.edit_user(name,phone)
        from study_appium.appium_po.page.AddUsers import AddUser
        return AddUser(self.driver)

    def edit_user_fail(self,name,phone):
        self.edit_user(name, phone)
        sleep(1)
        result = self.swipe_find("手机已存在于通讯录，无法添加", 1)
        if result:
            return "元素已存在"
        else:
            return "元素被添加"

