# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/28 11:40
# software: PyCharm
import pytest
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from logging import info


class Testwechat:

    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def get_list_value(self):
        # 获取通讯录列表所有值
        eles = self.driver.find_elements_by_xpath('//*[@id="member_list"]/tr/td/span')
        result = []
        index = 0
        temp_list = []
        for item in eles:
            name = item.get_attribute("textContent")
            temp_list.append(name)
            index = index + 1
            if index % 5 == 0:
                result.append(temp_list)
                temp_list = []
        return result

    def test_adduser(self):
        name = "企业微信1"
        tel = "17300000000"
        email = "1111@qq.com"
        id = "100001"
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(5)
        # 添加成员
        add_before_list = self.get_list_value()
        info(add_before_list)
        self.driver.find_element_by_xpath(
            '//*[@class="ww_operationBar"]//*[@class="qui_btn ww_btn js_add_member"]').click()
        # 填写用户信息
        ele = self.driver.find_element_by_xpath('//*[@class="qui_btn ww_btn ww_btn_Blue js_btn_continue"]')
        isvisibale = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "username")))
        if not isvisibale:
            print("页面加载失败")
            pass
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(id)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(tel)
        self.driver.find_element_by_id("memberAdd_mail").send_keys(email)
        self.driver.find_element_by_xpath(
            '//*[@class="member_edit_joinCheckboxCnt member_edit_sec"]//input[@class="ww_checkbox"]').click()
        self.driver.find_elements_by_xpath('//a[@class="qui_btn ww_btn js_btn_save"]')[0].click()
        sleep(10)
        add_user_list = [name, "", "hogwarts", tel, email]
        add_affter_list = self.get_list_value()
        exp_list = add_before_list
        exp_list.append(add_user_list)
        info(add_affter_list)
        info(exp_list)
        assert exp_list == add_affter_list
