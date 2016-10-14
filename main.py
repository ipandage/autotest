# -*- coding:utf-8 -*-
from selenium import webdriver

from cashRecord import CashRecord
from login import *
from petShopMember import *
from petinfo import *
from product import *
from productConsume import *
from productBack import *
from livingThing import *

domain = ''

username = ''
password = ''
mobile = ''
mobileMember = ''
# 默认简体
language = 'zh'
# language = 'tw'

# 是否是连锁店 0 不是  1 是
isChian = 1;

if(language == 'zh'):
    username = ''
    password = ''
    mobile = random.choice(['139', '188', '185', '136', '158', '151']) + "".join(random.choice("0123456789") for i in range(8))
    mobileMember = random.choice(['139', '188', '185', '136', '158', '151']) + "".join(random.choice("0123456789") for i in range(8))
else:
    username = ''
    password = ''
    mobile = random.choice(['09'])+"".join(random.choice("0123456789") for i in range(8))
    mobileMember = random.choice(['09'])+"".join(random.choice("0123456789") for i in range(8))

options = webdriver.ChromeOptions()
options.add_argument('test-type')
driver=webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get(domain + "/admin/login.jsp")

#登录
driver.implicitly_wait(10)
login = Login(driver, domain)

login.login(username, password)

livingThing = LivingThing(driver,domain)
livingThing.addLivingThing()
livingThing.addLivingThing()

petShopMember = PetShopMember(driver, domain, isChian)
petShopMember.addPetShopMember(mobile)
petShopMember.recharge()

petinfo = PetInfo(driver, domain, isChian)
petinfo.addPetInfo()

product = Product(driver, domain)
product.addProduct()

# product.stockMove()
# login.loginout()
# login.login("13657323379", "123456")
# product.stockMove()
# login.loginout()
# login.login("13488713179", "123456")

productConsume = ProductConsume(driver, domain)
productConsume.addProductConsume(mobileMember)
productConsume.addProductConsumeWithMember(mobile, mobileMember)

productBack = ProductBack(driver, domain)
productBack.addProductBack()

# cashRecord = CashRecord(driver,domain)
# cashRecord.withdrawals()

















