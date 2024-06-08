import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# set up webdriver and (1) open Wed page Ebay - Watch
driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

# (2) Select option Brand / Roles in filter pane
try:
    rolex_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']"))
    )
    rolex_checkbox.click()

#3 Verify the first two result items contain “rolex” in their title
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 's-item__title'))
    )
    item_titles = driver.find_elements(By.CLASS_NAME, 's-item__title')
    for title in item_titles[2:4]:
        print(title.text)
        assert 'rolex' in title.text.lower(), f"Title does not contain 'rolex' {title.text}"
finally:
    driver.quit()








