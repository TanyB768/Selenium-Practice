import os
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

    # Wait for the alert to appear and then switch to it.
    WebDriverWait(my_driver, timeout).until(EC.alert_is_present())
    print(my_driver.switch_to.alert.text)
    my_driver.switch_to.alert.send_keys("Tanishq Bodh")
    time.sleep(3)

    # Accept the alert by clicking ok on it.
    my_driver.switch_to.alert.accept()
    entered_txt = nav.get_element((By.ID, "promptResult"))
    print(entered_txt.text)

def handle_new_window(my_driver, timeout=10):
    nav.goto_toolsqa_page("browser-windows")
    click_btn = nav.get_element((By.ID, "tabButton"))
    click_btn.click()
    time.sleep(2)

    # Get the current handle of parent tab and wait till the new window opens
    parent_tab = my_driver.current_window_handle
    WebDriverWait(my_driver, timeout).until(EC.number_of_windows_to_be(2))

    # Get the child tab window handle and switch to it.
    child_tab = my_driver.window_handles[1] # 0th window is parent.
    my_driver.switch_to.window(child_tab)
    time.sleep(3)

    # Printing any content on it to check if this is child tab
    child_tab_heading = nav.get_element((By.ID, "sampleHeading"))
    print(child_tab_heading.text)

    # Switch back to parent tab
    my_driver.switch_to.window(parent_tab)
    print(my_driver.title)

def handle_iFrames(my_driver, timeout=10):
    nav.goto_toolsqa_page("nestedframes")

    # Switch to the parent iframe
    parent_frame = my_driver.find_element(By.ID, "frame1")
    my_driver.switch_to.frame(parent_frame)

    # Get the body text of the parent iframe
    parent_body = my_driver.find_element(By.TAG_NAME, "body")
    print(parent_body.text)
    time.sleep(3)

    # Now switch to the child iframe inside parent iframe
    child_frame = my_driver.find_element(By.TAG_NAME, "iframe")  # only one iframe inside
    my_driver.switch_to.frame(child_frame)

    # Get the body text of the child iframe
    child_body = my_driver.find_element(By.TAG_NAME, "body")
    print(child_body.text)

    # Switch back to the main content (outside all iframes)
    my_driver.switch_to.default_content()
    time.sleep(3)

def handle_download(my_driver):
    download_dir = nav.download_dir  # use the subfolder from Navigation
    expected_file = "sampleFile.jpeg"
    expected_path = os.path.join(download_dir, expected_file)
    temp_path = expected_path + ".crdownload"

    # Delete only the target file, leave everything else untouched
    if os.path.exists(expected_path):
        print(f"Deleting old file: {expected_file}")
        os.remove(expected_path)

    nav.goto_toolsqa_page("upload-download")
    download_btn = nav.get_element((By.ID, "downloadButton"))
    download_btn.click()
    print("Waiting for file to download...")
    time.sleep(1)

    # Check if the file has finishe downloading or took too long to download
    timeout = 10  # seconds
    poll_interval = 0.5
    elapsed = 0
    while elapsed < timeout:
        if os.path.exists(expected_path) and not os.path.exists(temp_path):
            print(f"File downloaded successfully at {expected_path}")
            return
        time.sleep(poll_interval)
        elapsed += poll_interval

    # If we reach here, download likely failed
    raise TimeoutError("Download took too long or failed.")


def handle_upload(my_driver):
    nav.goto_toolsqa_page("upload-download")

    # Locate the file input field
    upload_input = nav.get_element((By.ID, "uploadFile"))
    # Provide full path of the file you want to upload
    file_to_upload = "C:\\Users\\gamer\\Downloads\\DemoQA Downloads\\sampleFile.jpeg"
    upload_input.send_keys(file_to_upload)
    # Confirm upload message
    uploaded_msg = nav.get_element((By.ID, "uploadedFilePath")).text
    time.sleep(3)
    if uploaded_msg:
        print(f"Upload successful: {uploaded_msg}")
    else:
        print("Upload may have failed or no file path displayed.")

if __name__ == '__main__':
    try:
        nav = Navigation()
        driver = nav.get_driver()
        # passing driver as an argument to the functions makes selenium functions
        # available to my_driver object of above functions
        # handle_browser_alerts(driver)
        # delayed_alert(driver)
        # handle_cancel_or_ok_alerts(driver)
        # handle_text_alerts(driver)
        # handle_new_window(driver)
        # handle_iFrames(driver)
        # handle_download(driver)
        handle_upload(driver)

    finally:
        nav.quit_driver()