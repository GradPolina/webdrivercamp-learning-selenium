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
    time.sleep(5)

# First two items - price & title items
    results = driver.find_elements(By.XPATH, '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__wrapper clearfix"]')[:2]
    items = []
    for result in results:
        title_items = result.find_element(By.CLASS_NAME, 's-item__title')
        title = title_items.text
        price_items = result.find_element(By.CLASS_NAME, 's-item__price')
        price = price_items.text

# Verify first two result items contain “rolex” in their title
        assert 'rolex' in title.lower(), f"Title does not contain 'rolex': {title}"

# Story title and price (variable)
        items.append({'title:', title, 'price:', price})

# Print store (title, price)
    for item in items:
        print(item)

    original_window = driver.current_window_handle

# Switch first TAB
    for result in results[:1]:
        title_items = result.find_element(By.CLASS_NAME, 's-item__title')
        title_items.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])

    driver.switch_to.window(original_window)

# Switch second TAB
    for result in results[1:2]:
        title_items = result.find_element(By.CLASS_NAME, 's-item__title')
        title_items.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])

# Verify price and title new TAB
    new_title_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'x-item-title__mainTitle'))
    )
    new_title = new_title_item.text

    new_price_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ux-textspans'))
    )
    new_price = new_price_item.text

# Compare with stored data
    for i in items:
        assert items[i]['title'] in new_title, f"Mismatch in title: {new_title}"
        assert items[i]['price'] == new_price, f"Mismatch in price: {new_price}"


    driver.close()
    driver.switch_to.window(original_window)

# Uncheck Relex
    rolex_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']"))
    )
    rolex_checkbox.click()

# Checkbox casio
    casio_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Casio']"))
    )
    casio_checkbox.click()
    time.sleep(5)

    # Last two items - title items
    results_casio = driver.find_elements(By.XPATH,'//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__wrapper clearfix"]')[-2:]
    mismatches = []
    for result_casio in results_casio:
        title_items_casio = result_casio.find_element(By.CLASS_NAME, 's-item__title')
        title_casio = title_items_casio.text
        if 'Casio' not in title_casio:
            mismatches.append(title_casio)
    if mismatches:
        print("Found mismatches title:")
        for mismatch in mismatches:
            print(mismatch)
    else:
        print("All titles contain 'Casio'.")

finally:
    driver.quit()









