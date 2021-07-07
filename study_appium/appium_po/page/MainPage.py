# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 10:13
# software: PyCharm
from study_appium.appium_po.page.AddressBook import AddressBook
from appium.webdriver.webdriver import WebDriver
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
import pytest
import allure
import os

from study_appium.appium_po.page.bash_method import BaseMethod


class MainPage(BaseMethod):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_addressbook(self):
        self.wait_element('//*[@text="通讯录"]')
        self.find_elemet_click('//*[@text="通讯录"]')
        return AddressBook(self.driver)
