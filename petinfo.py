# -*- coding:utf-8 -*-
# 宠物模块
import time
class PetInfo:

    def __init__(self, driver, domain, isChian):
        print('PetInfo init ...')
        self.driver = driver
        self.domain = domain
        self.isChian = isChian

    def addPetInfo(self):
        driver = self.driver
        domain = self.domain

        timeStr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        driver.get(domain + "/admin/petShopMember/list.jhtml")

        if(self.isChian == 1):
            driver.find_element_by_xpath('//*[@id="simple-table"]/tbody/tr[1]/td[6]/a[1]').click()
        else:
            driver.find_element_by_xpath('//*[@id="simple-table"]/tbody/tr[1]/td[5]/a[1]').click()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="myTab"]/li[2]').click()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="pets"]/a').click()

        time.sleep(2)
        driver.find_element_by_id("petName").send_keys(u"狗狗"+timeStr)
        driver.find_element_by_id("petBirthday").send_keys("2016-08-16")
        driver.execute_script('$("#addPetInfoButton").click();')
        time.sleep(2)