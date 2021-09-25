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
        selenide_found = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite').text
        assert 'selenide.org' in selenide_found
        self.drv.get('https://www.google.ru/search?q=selenide&newwindow=1&bih=696&biw=782&hl=ru&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiI54-WoZrzAhVhposKHQkCBSsQ_AUoAnoECAEQBA')
        image_found = self.drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text
        assert 'selenide.org' in image_found
        self.drv.get('https://www.google.ru/search?q=selenide&source=lmns&bih=696&biw=782&hl=ru&sa=X&ved=2ahUKEwjprdPioprzAhWIyyoKHbusA7EQ_AUoAHoECAEQAA')
        selenide2_found = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite').text
        assert 'selenide.org' in selenide2_found


    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()

