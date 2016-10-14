# -*- coding:utf-8 -*-
# 结算模块
import time
class ProductConsume:
    def __init__(self, driver, domain):
        print('ProductConsume init ...')
        self.driver = driver
        self.domain = domain

    def addProductConsume(self, mobileMember):
        driver = self.driver
        domain = self.domain
        driver.get(domain + "/admin/ttbProductConsume/list.jhtml")
        self.productConsume(mobileMember, 0)

    def addProductConsumeWithMember(self, mobile, mobileMember):
        driver = self.driver
        domain = self.domain
        driver.get(domain + "/admin/ttbProductConsume/list.jhtml")
        time.sleep(2)
        driver.find_element_by_id("mobile").send_keys(mobile)
        driver.find_element_by_id("searchMember").click()
        time.sleep(2)
        self.productConsume(mobileMember, 1)

    def productConsume(self, mobileMember, isMember):
        driver = self.driver
        domain = self.domain
        timeStr = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        time.sleep(2)
        driver.execute_script('$("#productShow").find("a")[0].click();')

        # 改价格
        # 赠送
        if (isMember == 1) :
            driver.execute_script('$("#productShow").find("a")[1].click();')
            driver.find_element_by_id("discountPrice").click()
            driver.find_element_by_xpath('//*[@id="Spec_body"]/tr/td[6]/a[2]').click()
            time.sleep(1)
            driver.find_element_by_id('modifyPrice').clear()
            driver.find_element_by_id('modifyPrice').send_keys('20')
            driver.find_element_by_id('modifyPriceButton').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="Spec_body"]/tr[2]/td[5]/input').click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="myTab4"]/li[2]').click()

        time.sleep(2)
        driver.find_element_by_id("petBeautyType").send_keys(u"美容")
        driver.find_element_by_id("beautyTime").send_keys(timeStr)
        driver.find_element_by_id("consumeMoney").send_keys("100")

        driver.find_element_by_id("beautySubmit").click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="myTab4"]/li[3]').click()

        time.sleep(2)
        driver.find_element_by_id("startDate").send_keys(timeStr)
        driver.find_element_by_id("endDate").send_keys(timeStr)
        driver.find_element_by_name("price").send_keys("50")

        driver.find_element_by_id("houseSubmit").click()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="livingTab"]').click()
        time.sleep(2)
        driver.find_element_by_id('masterName').send_keys('test')
        driver.find_element_by_id('masterMobile').send_keys(mobileMember)
        driver.execute_script('$("#livingSubmit").click();')

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="cashier"]/div[3]').click()
        time.sleep(2)

        driver.find_element_by_id("confirmSettlement").click()
        time.sleep(2)

