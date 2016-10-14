# -*- coding:utf-8 -*-
# 活体管理模块
import time
class LivingThing:

    def __init__(self, driver, domain):
        print('livingThing init ...')
        self.driver = driver
        self.domain = domain

    def addLivingThing(self):
        driver = self.driver
        domain = self.domain
        timeStr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        driver.get(domain + "/admin/ttbPetshopLivingThing/list.jhtml")

        driver.find_element_by_id('toFormPage').click()

        time.sleep(2)
        driver.find_element_by_id('petName').send_keys(u'活体' + timeStr)
        driver.find_element_by_id('petBirthday').send_keys('2016-8-24')
        driver.find_element_by_id('vaccine').send_keys(u'接种1次')
        driver.find_element_by_id('insect').send_keys(u'驱虫1次')
        driver.find_element_by_id('restock').send_keys('200')
        driver.find_element_by_id('price').send_keys('500')
        driver.execute_script('$("#ttbPetshopLivingThingButton").click();')
