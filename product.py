# -*- coding:utf-8 -*-
# 商品模块
from selenium.webdriver.support.select import Select
import time
from random import choice
class Product:
    def __init__(self, driver, domain):
        print('Product init ...')
        self.driver = driver
        self.domain = domain

    def addProduct(self):
        driver = self.driver
        domain = self.domain

        timeStr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        randomStr = ''.join([choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789') for i in range(10)])

        driver.get(domain + "/admin/ttbProduct/list.jhtml")
        driver.find_element_by_id("toFormPage").click()

        time.sleep(2)
        driver.find_element_by_name("name").send_keys(u"商品" + timeStr)

        Select(driver.find_element_by_name("selBrand")).select_by_index(1)

        driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[2]/input').send_keys("test")
        driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[3]/input').send_keys("20")
        driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[4]/input').send_keys("30")
        driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[5]/input').send_keys("40")
        driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[6]/input').send_keys("10")
        driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[8]/input').send_keys(randomStr)

        driver.find_element_by_id("storeSubmitForm").click()
        time.sleep(2)

    # 库存调拨
    def stockMove(self):
        driver = self.driver
        domain = self.domain

        driver.get(domain + "/admin/ttbProduct/list.jhtml")
        driver.find_element_by_id("toStockMove").click()

        time.sleep(2)
        driver.execute_script('$("#productShow").find("a")[0].click();')

        driver.find_element_by_id("submitForm").click()
        time.sleep(1)

        driver.execute_script('$(".btn-warning").click();')




