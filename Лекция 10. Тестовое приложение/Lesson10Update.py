import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):

    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')

    def test_search_selenide(self):
        self.drv.get('http://google.com/ncr')
        assert 'Google' in self.drv.title
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        selenide_found = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div').text
        assert 'selenide.org' in selenide_found
        self.drv.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        image_found = self.drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text
        assert 'selenide.org' in image_found
        self.drv.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
        selenide2_found = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div').text
        assert 'selenide.org' in selenide2_found


    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()

