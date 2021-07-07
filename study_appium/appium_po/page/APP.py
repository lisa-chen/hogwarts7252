# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 10:13
# software: PyCharm
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from study_appium.appium_po.page.MainPage import MainPage
from study_appium.appium_po.page.bash_method import BaseMethod
from logging import info


class App(BaseMethod):
    # def __init__(self):
    #     self.desired_caps = {}
    #     self.desired_caps['platformName'] = 'Android'
    #     self.desired_caps['platformVersion'] = '6.0'
    #     self.desired_caps['deviceName'] = 'emulator-5554'
    #     self.desired_caps['skipDeviceInitialization'] = 'true'
    #     self.desired_caps['dontStopAppOnReset'] = 'true'
    #     self.desired_caps["noReset"] = "true"
    #     # self.desired_caps['appPackage'] = 'com.tencent.wework'
    #     # self.desired_caps['appActivity'] = '.launch.LaunchSplashActivity'

    def start_app(self, appPackage, appActivity):
        if self.driver == None:
            info("启动新的driver")
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '6.0'
            self.desired_caps['deviceName'] = 'emulator-5554'
            self.desired_caps['skipDeviceInitialization'] = 'true'
            self.desired_caps['dontStopAppOnReset'] = 'true'
            self.desired_caps["noReset"] = "true"
            self.desired_caps['appPackage'] = appPackage
            self.desired_caps['appActivity'] = appActivity
            self.driver = webdriver.Remote('http://localhost:4722/wd/hub', self.desired_caps)
            self.driver.implicitly_wait(15)
        else:
            info("复用driver")
            self.driver.launch_app()
        return self

    def close_app(self):
        self.driver.quit()

    def restar_app(self):
        self.driver.quit()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)
