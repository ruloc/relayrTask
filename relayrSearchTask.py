import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\joser.sanchez\\PycharmProjects\\chromedriver')
        self.driver.get('https://www.amazon.com')
        self.driver.maximize_window()

    #Basic Amazon search
    def test_amazon(self):
        search_input = 'playstation 4'
        search_id = 'twotabsearchtextbox'

        search = self.driver.find_element_by_id(search_id)
        search.send_keys(search_input)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        assert search_input in self.driver.page_source
        print('Basic search successful.')

    #Search results with next and previous page(pagination)
    def test_pagination(self):
        search_input = 'Wonder Woman'
        search_id = 'twotabsearchtextbox'
        nextpage_id = 'pagnNextString'
        prevpage_id= 'pagnPrevString'

        search = self.driver.find_element_by_id(search_id)
        search.send_keys(search_input)
        search.send_keys(Keys.ENTER)
        time.sleep(3)

        #Search results page 1
        assert search_input in self.driver.page_source
        next_page = self.driver.find_element_by_tag_name('body')
        next_page.send_keys(Keys.END)
        time.sleep(3)

        # Search results page 2
        self.driver.find_element_by_id(nextpage_id).click()
        next_page2 = self.driver.find_element_by_tag_name('body')
        next_page2.send_keys(Keys.END)
        time.sleep(3)

        # Search results page 3 and validate they are still Wonder Woman results
        self.driver.find_element_by_id(nextpage_id).click()
        prev_page = self.driver.find_element_by_tag_name('body')
        prev_page.send_keys(Keys.END)
        time.sleep(3)
        assert search_input in self.driver.page_source

        # Previous search results (page 2) and validation for still Wonder Woman/Amazon
        self.driver.find_element_by_id(prevpage_id).click()
        assert search_input in self.driver.page_source
        assert 'Amazon' in self.driver.title

        print('Successful pagination search')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
