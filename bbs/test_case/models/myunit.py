# coding:utf-8
from selenium import webdriver
from .driver import browser
import unittest
import os


class MyTest(unittest.TestCase):

    driver = browser()

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
