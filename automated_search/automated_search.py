from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# set up webdriver and (1) open Wed page Ebay - Watch
driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

# Select option Brand / Roles in filter pane
try:
    rolex_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']"))
    )
    rolex_checkbox.click()

# First two items - price & title items
    results = driver.find_elements(By.XPATH, '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__wrapper clearfix"]')[:2]
    items = []
    for result in results:
        title_items = result.find_element(By.CLASS_NAME, 's-item__title')
        title = title_items.text
        price_items = result.find_element(By.CLASS_NAME, 's-item__price')
        price = price_items.text
        title_items.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])

# Store title and price of the first two results in a variable
        items.append({'title:', title, 'price:', price})

# Verify first two result items contain “rolex” in their title
        assert 'rolex' in title.lower(), f"Title does not contain 'rolex' {title}"

# Verify price and title new TAB

    new_title_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'x-item-title__mainTitle'))
    )
    new_title = new_title_item.text

    new_price_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'x-price-primary'))
    )
    new_price = new_price_item.text

# Compare with stored data
    for i in results:
        assert items[i]['title'] in new_title, f"Mismatch in title: {new_title}"
        assert items[i]['price'] == new_price, f"Mismatch in price: {new_price}"

    driver.close()

    for item in items:
        print(item)

finally:
    driver.quit()









