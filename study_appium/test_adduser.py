# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/3 19:16
# software: PyCharm
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
import pytest
import allure
import os

@allure.feature("企业微信")
class TestWechat:
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

    def teardown(self):
        pass
        # self.driver.quit()

    @allure.story("添加联系人")
    def test_adduser(self):
        with allure.step("等待页面加载完成，出现指定文案"):
            WebDriverWait(self.driver, 15).until(
                lambda x: x.find_element(MobileBy.XPATH, "//*[@text='通讯录']"))
            allure.attach(self.driver.get_screenshot_as_png(), "通讯录页面", allure.attachment_type.PNG)  # 保存截图为allure的附件

        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        # 手动输入添加
        with allure.step("添加用户"):
            self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
            self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b09"]').send_keys("sha")
            self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/f7y"]').send_keys(
                '17380120003')
            self.driver.find_element_by_xpath('//*[@text="保存后自动发送邀请通知"]').click()
            self.driver.find_element_by_xpath('//*[@text="保存"]').click()
            allure.attach(self.driver.get_screenshot_as_png(), "点击保存后页面截图", allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
            allure.attach(self.driver.get_screenshot_as_png(), "点击保存后页面截图", allure.attachment_type.PNG)  # 保存截图为allure的附件

        # self.driver.start_activity(".launch.LaunchSplashActivity")

if __name__ == '__main__':
    pytest.main(["-s", "-v", "--alluredir=report", "test_adduser.py"])
    # os.system("allure serve "+report_dir_temp)
    # os.system("allure generate "+report_dir_temp+" --clean -o "+report_dir+" || true && allure report open -o "+report_dir)
    os.system("allure generate " + 'report' + " -o " + 'report_dir' + " --clean")


