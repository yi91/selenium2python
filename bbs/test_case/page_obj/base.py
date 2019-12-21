# coding:utf-8
from time import sleep
from selenium import webdriver


class Page(object):
    """ 页面基拙类，用于所有页面的继承 """

    def __init__(self, selenium_driver, base_url='https://bbs.meizu.cn', parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        # assert self.on_page(url), ' Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self, url):
        self._open(url)

    def on_page(self, url):
        return self.driver.current_url == (self.base_url + url)

    def script(self, src):
        return self.driver.execute_script(src)

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    Page(driver).open('/')
    sleep(3)
    Page(driver).close()

