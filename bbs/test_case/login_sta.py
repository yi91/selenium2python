# coding:utf-8

import random
import unittest
from mztestpro.bbs.test_case.models import myunit, function
from mztestpro.bbs.test_case.page_obj.loginPage import Login


class LoginTest(myunit.MyTest):
    """ 社区登录测试 """

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_loginl(self):
        """ 用户名、密码为空登录 """
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), "账号不能为空")
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver, "user_pawd_empty.jpg")

    def test_login2(self):
        """ 用户名正确，密码为空登录 """
        self.user_login_verify(username="pytest")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver, "pawd_empty.jpg")

    def test_login3(self):
        """ 用户名为空 ，密码正确 """
        self.user_login_verify(password="abcl23456")
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), "账号不能为空")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        """ 用户名与密码不匹配 """
        character = random.choice('zyxwvutisrqponmlkjihgfedcba')
        username = "zhangsan" + character
        self.user_login_verify(username=username, password="123456")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码与账号不匹配")
        function.insert_img(self.driver, "user_pawd_error.jpg")

    def test_login5(self):
        """ 用户名、密码正确 """
        self.user_login_verify(username="zhangsan", password="123456")
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), '张三')
        function.insert_img(self.driver, "user_pawd_ture.jpg")


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(LoginTest('user_login_verify'))

    runner = unittest.TextTestRunner()
    runner.run(suit)
