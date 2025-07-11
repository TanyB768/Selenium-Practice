"""
    This is just a small script for basic automation and verification of name and email.
"""
import time

from selenium import webdriver #importing selenium package and webdriver module
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
    then Inside the webdriver module, there are browser-specific submodules.
    Of which "service" module helps manage the ChromeDriver service.
    The Service class here lets you define settings for launching it (like giving a path to chromedriver.exe).
    
    The "Service" is a Class inside the "service" module used to start and manage the 
    ChromeDriver process behind the scenes.
"""
driver = webdriver.Chrome()
driver.implicitly_wait(10) # If any element which we find by find_element/s() is not loaded in 10 seconds then the
                           # the test will crash. So for this we should use try catch block.
# driver variable holds the instance of webdriver module's Chrome() class which needs
# chrome service as an argument, if the webdriver isn't put in PATH variables otherwise we need to
# specify the location of the chromedriver.exe to start the chrome service.
"""
    If chromedriver.exe isn't in your system PATH, you must manually specify its location like:
    
    chrome_service = Service(executable_path="C:/path/to/chromedriver.exe")
    driver = webdriver.Chrome(service = chrome_service)
"""
WebDriverWait(driver, 10) # Explicit Wait declaration

driver.get("https://demoqa.com/") #get() function opens a URL
print(driver.title) #prints the header
print(driver.current_url) #prints the current URL
time.sleep(1)
# driver.minimize_window()
# time.sleep(1)
driver.maximize_window()
driver.refresh() # refreshes the page
driver.get("https://demoqa.com/elements") #goes on a page which has this valid URL
# driver.back() # goes back to https://demoqa.com/
# driver.forward() # goes back to https://demoqa.com/elements
time.sleep(2)
"""
    Text and input verification by finding text elements
"""
text_box = driver.find_element(By.XPATH,"//div[contains(@class,'element-list collapse show')]//li[@id='item-0']")
text_box.click()
text_box_Fullname = driver.find_element(By.XPATH,"//input[@id='userName']")
name = "Tanishq Bodh"
text_box_Fullname.send_keys(name)

text_box_Email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email = "xyz@gmail.com"
text_box_Email.send_keys(email)
text_box_SubmitButton = driver.find_element(By.XPATH, "//button[@id='submit']")
text_box_SubmitButton.click()
output_name = driver.find_element(By.XPATH,"//div[@class='border col-md-12 col-sm-12']").text.split(":")[1].strip("\n").splitlines()[0]
output_email = driver.find_element(By.XPATH,"//p[@id='email']").text.split(":")[1].strip("\n").splitlines()[0]

"""
    #lines = output_name.text.split(":")[1].strip("\n").splitlines()[0]
    OKAY ! so the above lines object gets a text/paragraph element from output_name and splits it after the colon (:)
    found in the paragraph 1 (coz there are 2 paras - 1) "Name:" 2)"Email:") which was in a dynamic div which becomes 
    visible when name and text is entered in the text box and submit button is clicked.
    So using split() which takes a string/char as an input to split the string from that found char/string, it splits
    the para 1 from ":" as in "Name:" and returns "Tanishq Bodh\n Email". After that we use splitlines() funciton to 
    split the first line from the rest of the output and hence the index value[0]. Then we finally get our entered name
    that we can verify in the if block
"""
if((output_name == name) and (output_email == email)):
    print("Name and Email Found")
driver.minimize_window()

input("Press Enter to exit...")


# driver.close() #closes the browser and URL
'''
    LOCATORS
'''
# below we use Relative and absolute XPaths to certain elements to interact with them
#relative //input[@id='user-name']
#relative //input[@id='password']

