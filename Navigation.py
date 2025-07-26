import os
import time

from selenium import webdriver #importing selenium package and webdriver module
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navigation:
    def __init__(self):
        # Define download path. Can be custom download path too like in the end of code's commented __init__ class
        self.download_dir = os.path.join(os.getcwd(), "downloads")
        # This is a check if the downloads folder in the above location doesn't exist
        # it can be created through os.makedirs and if already exist then no need to create again.
        os.makedirs(self.download_dir, exist_ok=True)

        # Locate the webdriver. Can cause errors if not located in venv because of filepath errors.
        driver_path = os.path.join(os.getcwd(), "webdrivers", "chromedriver.exe")
        # Make sure chromedriver is in place in virtual env.
        if not os.path.isfile(driver_path):
            raise FileNotFoundError(f"ChromeDriver not found at {driver_path}. Make sure it's placed correctly.")
        # Pass the driver path to service class to create chrome service.
        chrome_service = Service(driver_path)
        # The options object is used to customize how Chrome behaves when it opens.
        # You can disable popups, set download directories, run in headless mode, or add experimental features.
        # Basically, it's how you configure Chrome's behavior before it's launched.
        options = webdriver.ChromeOptions()

        # Set Chrome preferences for automatic downloads
        prefs = {
            "download.default_directory": self.download_dir,
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        # Add prefs to options object to make chrome behave how we like
        options.add_experimental_option("prefs", prefs)
        # Lastly, add both service and options object to driver to complete the initialization.
        self.driver = webdriver.Chrome(service=chrome_service, options=options)

    def get_driver(self):
        return self.driver

    def goto_toolsqa_page(self, page_name):
        url = "https://demoqa.com/"
        self.driver.get(url+page_name)

    def get_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.location_once_scrolled_into_view  # ensure visibility
        return element

    def get_download_dir(self):
        return self.download_dir

    def quit_driver(self):
        self.driver.quit()

    # def __init__(self):
    #     # Define download path
    #     """ USING forward slash '/' in download path makes chrome download only in default directory i.e. C:/Users/gamer/Downloads/ """
    #     # self.download_dir = os.path.join(os.getcwd(), "C:/Users/gamer/Downloads/DemoQA Downloads")
    #
    #     """ THIS IS WHY ME MUST USE DOUBLE BACKWARD SLASHES TO DOWNLOAD TO CUSTOM DIRECTORY"""
    #     self.download_dir = os.path.join(os.getcwd(), "C:\\Users\\gamer\\Downloads\\DemoQA Downloads")
    #
    #     # This is a check if the downloads folder in the above location doesn't exist
    #     # it can be created through os.makedirs and if already exist then no need to create again.
    #     os.makedirs(self.download_dir, exist_ok=True)
    #
    #     chrome_service = Service("C:/Webdrivers/chromedriver-win64/chromedriver.exe")
    #     options = webdriver.ChromeOptions()
    #
    #     # Set Chrome preferences for automatic downloads
    #     prefs = {
    #         "download.default_directory": self.download_dir,
    #         "download.prompt_for_download": False,
    #         "download.directory_upgrade": True,
    #         "safebrowsing.enabled": True
    #     }
    #     # Adding preferences is an experimental feature
    #     options.add_experimental_option("prefs", prefs)
    #     # add options to driver to change default chrome prefs
    #     self.driver = webdriver.Chrome(service=chrome_service, options=options)