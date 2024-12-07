from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://webscraper.io/test-sites/e-commerce/static/computers/{query}?page=1")
elem=driver.find_element(By.CLASS_NAME,"caption")
print(elem.text)
time.sleep(2)
driver.close()