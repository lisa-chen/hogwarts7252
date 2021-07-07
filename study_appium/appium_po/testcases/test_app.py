# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/7/5 10:38
# software: PyCharm
from study_appium.appium_po.page.APP import App
from faker import Faker
import os
import allure

import pytest


@allure.feature("测试app")
class TestCase:

    def setup_class(self):
        self.faker = Faker('zh_CN')
        self.app = App()

    def teardown_class(self):
        self.app.close_app()

    def setup(self):
        appPackage = "com.tencent.wework"
        appActivity = ".launch.LaunchSplashActivity"
        self.main = self.app.start_app(appPackage, appActivity).goto_main()
        # self.name=self.faker.name()
        # self.phone = self.faker.phone_number()

    def teardown(self):
        self.app.back_xpath('//*[@text="通讯录"]')

    @allure.story("添加联系人成功")
    # @pytest.mark.parametrize('name,phone', get_userinfo(5))
    def test_adduser(self):
        # name = self.faker.name()
        # phone = self.faker.phone_number()
        # self.name = name
        name = "陈哈哈"
        phone = self.faker.phone_number()
        result = self.main.go_to_addressbook().go_to_adduser().goto_edituser().edit_user_success(name,
                                                                                                 phone).get_reslut()
        # self.main.go_to_addressbook()
        assert result == "添加成功"

    @allure.story("删除联系人")
    def test_Deleteuser(self):
        name = "陈哈哈"
        result = self.main.go_to_addressbook().goto_userinfo(
            name).goto_uersinfo_list().goto_edit_detaiinfo().delete_user().find_ele_exist(name)
        assert result == "元素不存在"

    # @allure.story("添加联系人成功")
    # # @pytest.mark.parametrize('name,phone', get_userinfo(5))
    # def test_adduser2(self):
    #     name = "晨欣"
    #     phone = self.faker.phone_number()
    #     result = self.main.go_to_addressbook().go_to_adduser().goto_edituser().edit_user_success(name,
    #                                                                                              phone).get_reslut()
    #     # self.main.go_to_addressbook()
    #     assert result == "添加成功"
    #
    # @allure.story("删除联系人")
    # def test_Deleteuser2(self):
    #     name = "晨欣"
    #     result = self.main.go_to_addressbook().goto_userinfo(
    #         name).goto_uersinfo_list().goto_edit_detaiinfo().delete_user().find_ele_exist(self.main)
    #     assert result == "元素不存在"

    @allure.story("添加联系人失败")
    # @pytest.mark.parametrize('name,phone', get_userinfo(5))
    def test_add_fail(self):
        name = "sha"
        phone = "17380120000"
        result = self.main.go_to_addressbook().go_to_adduser().goto_edituser().edit_user_fail(name,
                                                                                              phone)
        assert result == "元素已存在"


if __name__ == '__main__':
    pytest.main(["-s", "-v", "--alluredir=report", "test_app.py"])
    # os.system("allure serve "+report_dir_temp)
    # os.system("allure generate "+report_dir_temp+" --clean -o "+report_dir+" || true && allure report open -o "+report_dir)
    os.system("allure generate " + 'report' + " -o " + 'report_dir' + " --clean")
