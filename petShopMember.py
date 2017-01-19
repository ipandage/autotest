# -*- coding:utf-8 -*-
# 会员模块
from selenium.webdriver.support.select import Select
import time
import random
class PetShopMember:
    def __init__(self, driver, domain, isChian):
        print('PetShopMember init ...')
        self.driver = driver
        self.domain = domain
        self.isChian = isChian

    def addPetShopMember(self, mobile):
        driver = self.driver
        domain = self.domain

        timeStr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        driver.get(domain + "/admin/petShopMember/list.jhtml")
        driver.find_element_by_id("toFormPage").click()

        time.sleep(3)
        driver.find_element_by_id("name").send_keys(u"客户"+timeStr)
        driver.find_element_by_id("mobile").send_keys(mobile)
        Select(driver.find_element_by_name("memberRankId")).select_by_visible_text('金牌会员')
        driver.find_element_by_id("submitForm").click()

        time.sleep(2)
        driver.execute_script('$(".btn-success").click();')

        time.sleep(2)
        driver.find_element_by_id("petName").send_keys(u"狗狗"+timeStr)
        driver.find_element_by_id("petBirthday").send_keys("2016-08-16")
        driver.execute_script('$("#addPetInfoButton").click();')

        time.sleep(2)
        driver.execute_script('$(".btn-success").click();')

        time.sleep(2)
        driver.find_element_by_name("RechargeAmount").send_keys("1000")
        driver.find_element_by_name("promotionalBalance").send_keys("200")
        driver.execute_script('$("#openCardButton").click();')

        time.sleep(2)
        driver.execute_script('$(".btn-info").click();')
        time.sleep(2)

    # 续费充值
    def recharge(self):
        driver = self.driver
        domain = self.domain

        driver.get(domain + "/admin/petShopMember/list.jhtml")

        if(self.isChian == 1):
            driver.find_element_by_xpath('//*[@id="simple-table"]/tbody/tr[1]/td[6]/a[1]').click()
        else:
            driver.find_element_by_xpath('//*[@id="simple-table"]/tbody/tr[1]/td[5]/a[1]').click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="rechargeAccountButton"]/span[1]/a').click()

        time.sleep(1)
        driver.find_element_by_name("RechargeAmount").send_keys("1000")
        driver.find_element_by_name("promotionalBalance").send_keys("200")
        driver.execute_script('$("#rechargeButton").click();')

    # 开次卡
    def openNumberCard(self):
        driver = self.driver
        domain = self.domain

        driver.get(domain + "/admin/petShopMember/list.jhtml")

        if (self.isChian == 1):
            driver.find_element_by_xpath('//*[@id="simple-table"]/tbody/tr[1]/td[6]/a[1]').click()
        else:
            driver.find_element_by_xpath('//*[@id="simple-table"]/tbody/tr[1]/td[5]/a[1]').click()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="rechargeAccountButton"]/span[2]/a').click()
        time.sleep(1)
        driver.find_element_by_name("RechargeAmount").send_keys("100")
        driver.find_element_by_name("accountBalance").send_keys("5")
        driver.find_element_by_id("openNumberCardButton").click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="rechargeAccountButton"]/span[2]/a').click()
        time.sleep(1)
        driver.execute_script('$("input[name=businessType]").eq(1).iCheck("check")')

        driver.find_element_by_name("RechargeAmount").send_keys("100")
        driver.find_element_by_name("accountBalance").send_keys("4")
        driver.find_element_by_id("openNumberCardButton").click()

        # 续次
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="faq-tab-1"]/div[2]/div[1]/div[2]/span/a').click()
        time.sleep(1)
        driver.find_element_by_name("rechargeAmount").send_keys("100")
        driver.find_element_by_name("rechargeCount").send_keys("4")
        driver.find_element_by_id("renewalsNumberCardButton").click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="faq-tab-1"]/div[3]/div[1]/div[2]/span/a').click()
        time.sleep(1)
        driver.find_element_by_name("rechargeAmount").send_keys("100")
        driver.find_element_by_name("rechargeCount").send_keys("5")
        driver.find_element_by_id("renewalsNumberCardButton").click()



