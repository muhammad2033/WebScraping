from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
webdriver_service = Service('path/to/https://www.sellyourmac.com/')
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Navigate to the website
driver.get("https://www.sellyourmac.com/")

# Select the options (example: selecting a MacBook Air model)
model_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'model')))
driver.find_element(By.XPATH, "//option[contains(text(), 'MacBook Air')]").click()
print(model_select)
# Wait for the prices to load (modify the CSS selector according to the website's structure)
price_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.price')))

# Extract the prices
prices = [price.text.strip() for price in price_elements]

# Print the prices
for price in prices:
    print(price)

# Close the WebDriver
driver.quit()
