from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Set up webdriver and open the eBay page for watches
driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

# Select the Rolex checkbox in the filter pane
try:
    rolex_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']"))
    )
    rolex_checkbox.click()
    time.sleep(5)

    # Get the first two items - price & title
    results = driver.find_elements(By.XPATH, '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__wrapper clearfix"]')[:2]
    items = []

    for result in results:
        title_items = result.find_element(By.CLASS_NAME, 's-item__title').text
        price_items = result.find_element(By.CLASS_NAME, 's-item__price').text

        # Verify the first two result items contain “rolex” in their title
        assert 'rolex' in title_items.lower(), f"Title does not contain 'rolex': {title_items}"

        # Store title and price in a variable
        items.append({'title': title_items, 'price': price_items})

    # Print the stored title and price
    for item in items:
        print(item)

    mistakes = []
    original_window = driver.current_window_handle

    # Switch to each item tab
    for i, result in enumerate(results):
        title_items = result.find_element(By.CLASS_NAME, 's-item__title')
        title_items.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])

        # Verify price and title in the new tab
        new_title_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'x-item-title__mainTitle'))
        ).text
        new_price_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'x-price-primary'))
        ).text

        if items[i]['title'].lower() != new_title_item.lower():
            mistakes.append(new_title_item)
        if items[i]['price'] != new_price_item.strip("US "):
            mistakes.append(new_price_item)

        driver.close()
        driver.switch_to.window(original_window)

    if mistakes:
        print("Mistakes in title/price:")
        for mistake in mistakes:
            print(mistake)
    else:
        print("All titles and prices are correct")

    # Uncheck the Rolex checkbox

    rolex_uncheck = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']"))
    )
    rolex_uncheck.click()
    time.sleep(5)

    # Select the Casio checkbox
    casio_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Casio']"))
    )
    casio_checkbox.click()
    time.sleep(5)

    # Get the last two items - title
    results_casio = driver.find_elements(By.XPATH, '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__wrapper clearfix"]')[-2:]
    mismatches = []

    for result_casio in results_casio:
        title_items_casio = result_casio.find_element(By.CLASS_NAME, 's-item__title').text
        if 'casio' not in title_items_casio.lower():
            mismatches.append(title_items_casio)

    if mismatches:
        print("Found mismatched titles:")
        for mismatch in mismatches:
            print(mismatch)
    else:
        print("All titles contain 'Casio'.")

finally:
    driver.quit()







