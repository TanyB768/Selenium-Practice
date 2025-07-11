import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""
    Application commands (for web driver)
"""
# get() - opens a URL
# driver.title - gets page title
# driver.page_source - capture the HTML code of the page
# driver.find_element() - finds a single element. Throws error if an XPATH leads to multiple elements.
#                         also throws error if no such element is found.
# driver.find_elements() - finds multiple elements and returns them as a list. If no element is found,
#                          an empty list is returned.

"""
    Conditional commands (for web elements)
"""
# element.is_displayed() - self explanatory
# element.is_enabled() - if an action can be performed
#                        on an element or not like passing a value/boolean.
# element.is_selected() - Ex: For radio buttons and check boxes.
# element.text - returns inner text of an element (the one already present in HTML/CSS code.
# element.get_attribute('value') - returns the entered text of an element. Ex: email in an email box.

"""
    Browser commands (for navigation control of the browser)
"""
# | Command                           | Description                                           |
# | --------------------------------- | ----------------------------------------------------- |
# | `driver.back()`                   | Simulates pressing the back button in browser         |
# | `driver.forward()`                | Simulates pressing the forward button                 |
# | `driver.refresh()`                | Reloads the current page                              |
# | `driver.quit()`                   | Closes all browser windows and ends WebDriver session |
# | `driver.close()`                  | Closes only the current browser window (where driver  |
# |  is focused. Ex: from parent window, if a 2nd tab is opened then driver.close() will close|
# |  only the parent tab as we haven't made it to switch to the 2nd tab.                      |
# | `driver.maximize_window()`        | Maximizes the browser window                          |
# | `driver.minimize_window()`        | Minimizes the window (useful before capturing alerts) |
# | `driver.fullscreen_window()`      | Sets window to fullscreen mode                        |
# | `driver.get_window_size()`        | Returns the browser window size (width & height)      |
# | `driver.set_window_size(w, h)`    | Sets the window size                                  |
# | `driver.get_window_position()`    | Returns the x, y position of the window               |
# | `driver.set_window_position(x,y)` | Moves the window to screen position (x, y)            |

"""
    Waits
"""
# | Command                                 | Description                        |
# | --------------------------------------- | ---------------------------------- |
# | `driver.implicitly_wait(10)`            | Applies a default wait time for all|
# |  elements. The wait time is applied to all the lines after implicit wait is  |
# |  is written.                                                                 |
# | `WebDriverWait(driver, 10)`             | Explicit wait for up to 10 seconds |
# | explicit wait works based on condition, not timing.                          |
# | ``                                      | Fluent wait.                       |
# | `EC.presence_of_element_located(...)`   | Wait until element is in DOM       |
# | `EC.visibility_of_element_located(...)` | Wait until element is visible      |
