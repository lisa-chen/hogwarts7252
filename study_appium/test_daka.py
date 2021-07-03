# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/1 16:10
# software: PyCharm
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
import allure


class TestDaka:
    def setup(self):
        # 初始化被测软件
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps["noReset"] = "true"
        self.driver = webdriver.Remote('http://localhost:4722/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def teardowm(self):
        self.driver.quit()

    def test_daka(self):
        with allure.step("等待页面加载完成，出现指定文案"):
            WebDriverWait(self.driver, 15).until(
                lambda x: x.find_element(MobileBy.XPATH, "//*[@text='工作台']"))
        self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
        self.driver.find_element_by_xpath('//*[@text="打卡"]').click()
        with allure.step("外出打卡"):
            WebDriverWait(self.driver, 15).until(
                lambda x: x.find_element(MobileBy.XPATH, "//*[@text='外出打卡']"))
            self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")


