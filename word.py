# -*- coding:utf-8 -*-
class Word:
    def __init__(self, driver):
        print('Login init ...')
        self.driver = driver

    def getWords(self):
        for i in range(1, 232):
            self.dealSinglePage("http://dict.youdao.com/wordbook/wordlist?p="+str(i)+"&tags=")

    def dealSinglePage(self, url):
        driver = self.driver
        driver.get(url)

        for i in range(1, 15):
            self.dealSingleWord(i)

    def dealSingleWord(self, rowNum):

        driver = self.driver

        word = driver.find_element_by_xpath('//*[@id="wordlist"]/table/tbody/tr['+str(rowNum)+']/td[2]/div/a/strong').text

        if word is None or word == '' or ' ' in word or '+' in word or '-' in word:
            return

        print word







