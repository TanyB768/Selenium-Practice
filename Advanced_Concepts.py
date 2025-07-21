import time

from Navigation import Navigation # import navigation class from navigation
from selenium import webdriver #importing selenium package and webdriver module
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_browser_alerts(my_driver):
    nav.goto_toolsqa_page("alerts")
    click_btn = nav.get_element((By.ID, "alertButton"))
    time.sleep(1)
    click_btn.click()
    time.sleep(3)  # Wait to observe the alert
    print(my_driver.switch_to.alert.text)
    my_driver.switch_to.alert.accept() # clicks on 'ok' on popup
    # my_driver.switch_to.alert.dismiss() clicks on 'cancel' on popup

def delayed_alert(mydriver, timeout=10):
    nav.goto_toolsqa_page("alerts")
    click_btn = nav.get_element((By.ID, "timerAlertButton"))
    click_btn.click()
    # Wait for the alert to appear
    WebDriverWait(mydriver, timeout).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    # Accept the alert once
    mydriver.switch_to.alert.accept()
    # Optional: wait to observe that it was accepted
    time.sleep(3)

def handle_cancel_or_ok_alerts(my_driver, timeout=10):
    nav.goto_toolsqa_page("alerts")
    click_btn = nav.get_element((By.ID, "confirmButton"))
    click_btn.click()
    WebDriverWait(my_driver, timeout).until(EC.alert_is_present())
    print(my_driver.switch_to.alert.text)
    time.sleep(3)
    # Accept the alert once
    my_driver.switch_to.alert.accept()
    confirm_res = nav.get_element((By.ID, "confirmResult"))
    print(confirm_res.text)
    time.sleep(3)
    # This time we click on cancel AKA dismiss()
    click_btn.click()
    WebDriverWait(my_driver, timeout).until(EC.alert_is_present())
    print(my_driver.switch_to.alert.text)
    time.sleep(3)
    my_driver.switch_to.alert.dismiss()
    print(confirm_res.text)

def handle_text_alerts(my_driver, timeout=10):
    nav.goto_toolsqa_page("alerts")
    click_btn = nav.get_element((By.ID, "promtButton"))
    click_btn.click()
    WebDriverWait(my_driver, timeout).until(EC.alert_is_present())
    print(my_driver.switch_to.alert.text)
    my_driver.switch_to.alert.send_keys("Tanishq Bodh")
    time.sleep(3)
    my_driver.switch_to.alert.accept()
    entered_txt = nav.get_element((By.ID, "promptResult"))
    print(entered_txt.text)

if __name__ == '__main__':
    try:
        nav = Navigation()
        driver = nav.get_driver()
        # passing driver as an argument to the functions makes selenium functions
        # available to my_driver object of above functions
        handle_browser_alerts(driver)
        delayed_alert(driver)
        handle_cancel_or_ok_alerts(driver)
        handle_text_alerts(driver)

    finally:
        nav.quit_driver()