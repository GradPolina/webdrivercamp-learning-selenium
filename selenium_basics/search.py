from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
print(driver.current_url)
try:
    search =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"gh-ac")))
finally:
    search.clear()
    search.send_keys("women watch")
    search.send_keys(Keys. RETURN)
    print(driver.current_url)
    print(driver.title)

time.sleep(5)
driver.quit()


