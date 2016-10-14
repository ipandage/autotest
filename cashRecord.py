# -*- coding:utf-8 -*-
# 收银记录撤单模块
import time

class CashRecord:
    def __init__(self, driver, domain):
        print('cashRecord init ...')
        self.driver = driver
        self.domain = domain

    def withdrawals(self):
        driver = self.driver
        domain = self.domain

        driver.get(domain + "/admin/cashRecord/list.jhtml?pageSize=5")
        driver.find_element_by_xpath('//*[@id="simple-table-0"]/thead/tr/td/span[3]/span[5]/a').click()
        time.sleep(1)

        driver.execute_script('$(".btn-warning").click();')

        time.sleep(2)
        driver.get(domain + "/admin/common/main.jhtml")




