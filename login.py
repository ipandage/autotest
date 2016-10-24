# -*- coding:utf-8 -*-
# 登录模块
import time
class Login:
    def __init__(self, driver, domain):
        print('Login init ...')
        self.driver = driver
        self.domain = domain

    # 登录
    def login(self, user, password):
        driver = self.driver
        domain = self.domain

        time.sleep(1)
        driver.get(domain + "/admin/login.jsp")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("captcha").clear()
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("captcha").send_keys("")
        driver.find_element_by_class_name("loginBtn").click()
        time.sleep(1)

    def loginout(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="navbar-container"]/div[3]/ul/li[3]/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="navbar-container"]/div[3]/ul/li[3]/ul/li[3]/a').click()






