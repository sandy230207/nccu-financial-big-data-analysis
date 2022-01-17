from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
import time
#等待by XPATH    
def wait_by_xpath(driver , xpath):   
    locator = (By.XPATH, xpath)
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))
        return driver;
    except TimeoutException:
        wait_by_xpath(driver, xpath)
