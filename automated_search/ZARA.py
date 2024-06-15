from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.zara.com/us/")

try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'LOG IN'))
    )
    login.click()
    time.sleep(5)

    forgot_password = (driver.find_element(By.LINK_TEXT, 'Forgot your password?'))
    forgot_password.click()

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'zds-input-base__input'))
    )
    email.send_keys("polinaskypestudy@gmail.com")
    email.send_keys(Keys.RETURN)

    continue_click = driver.find_element(By.CLASS_NAME, 'zds-button__lines-wrapper')
    continue_click.click()
    time.sleep(5)



    #email = driver.find_element(By.NAME, 'logonId')
    #email.clear()
    #email.send_keys("polinadubina14@gmail.com")
    #email.send_keys(Keys.RETURN)

    #password = driver.find_element(By.NAME, 'password')
    #password.clear()
    #password.send_keys("Ivapol1984")
    #password.send_keys(Keys.RETURN)

    #login_click = driver.find_element(By.CLASS_NAME, 'zds-button__lines-wrapper')
    #login_click.click()

except:
    driver.quit()


