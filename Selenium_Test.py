import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

# 1) Visit site link and see if it matches with what the client wants
link = driver.current_url
assert (link == "https://demoqa.com/"), "Link doesn't match"
print(link)

# 2) See if site title is same as DEMOQA
title = driver.title
assert (title == "DEMOQA"), "Title Doesn't match"
print(title)

#Smoke testing to see if homepage is working and that all links and elements are
#clickable and goes to a valid page.

# 3) Verifying that logo is displayed
logo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
assert logo.is_displayed(), "Logo not displayed"

# 3.1)
"""Below code compares logo images by their name on webpage versus on local system"""
image = driver.find_element(By.XPATH, "//img[contains(@src,'Toolsqa.jpg')]")
image_url = image.get_attribute("src")
assert image_url.endswith("Toolsqa.jpg"), "Logo image src doesn't match expected"

# 4) Verifying that Selenium training banner is clickable and takes us to toolsqa website
toolsQA_banner = driver.find_element(By.XPATH,"//body")
toolsQA_banner.click()
time.sleep(2)
# Get window handles
tabs = driver.window_handles
driver.switch_to.window(tabs[1])  # Switch to the second tab
toolsQA_link = driver.current_url
assert (toolsQA_link == "https://www.toolsqa.com/selenium-training/"), "Banner not working"
print(toolsQA_link)

input("Press enter to exit")
time.sleep(3)