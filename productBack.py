# -*- coding:utf-8 -*-
# 退货模块
import time
class ProductBack:
    def __init__(self, driver, domain):
        print('ProductBack init ...')
        self.driver = driver
        self.domain = domain

    def addProductBack(self):
        driver = self.driver
        domain = self.domain

        driver.get(domain + "/admin/ttbProductBack/list.jhtml")

        time.sleep(2)
        driver.find_element_by_id("toFormPage").click()

        time.sleep(2)
        driver.execute_script('$("#productShow").find("a")[0].click();')

        time.sleep(2)
        driver.find_element_by_name("content").send_keys("test")
        driver.find_element_by_id("submitForm").click()

        time.sleep(2)
        driver.execute_script('$(".btn-warning").click();')






