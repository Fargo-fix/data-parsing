import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ParseSite:

    def __init__(self):

        self.euro_list = []
        self.date_list = []
        self.time_list = []

    def run(self):

        self.option = webdriver.FirefoxOptions()
        self.option.headless = True

        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox(options=self.option)
        self.driver.get('https://bank.com.ua/ru')
        

        self.euro = float(self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/div[3]/span').text)
        self.euro_list.append(self.euro)

        self.driver.quit()
        