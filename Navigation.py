import time

from selenium import webdriver #importing selenium package and webdriver module
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navigation:
    def __init__(self):
        chrome_service = Service("C:/Webdrivers/chromedriver-win64/chromedriver.exe")
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=chrome_service)

    def get_driver(self):
        return self.driver

    def goto_toolsqa_page(self, page_name):
        url = "https://demoqa.com/"
        self.driver.get(url+page_name)

    def get_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def quit_driver(self):
        self.driver.quit()