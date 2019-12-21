# coding:utf-8

from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器驱动
def browser():

    """
    # 运行主机：端口号（木机默认：127.0.0.1:4444)
    host = '127.0.0.1:4444'
    # 指定浏览器 chrome firefox ...
    dc = {'browserName': 'chrome'}
    driver = Remote(command_executor='http://' + host + '/wd/hub1', desired_capabilities=dc)
    """

    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("https://www.baidu.com")
    dr.quit()
