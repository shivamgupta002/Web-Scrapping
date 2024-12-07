from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("http://www.google.com")

# Find the search box and enter a query
box = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
box.send_keys("House of dragons")
box.send_keys(Keys.ENTER)

# Wait for search results to load (adjust sleep time if needed)
time.sleep(2)

# Attempt to click a link (update the XPath as required for your target link)
try:
    link = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/div[1]/div/div/span/a")
    link.send_keys(Keys.ENTER)
    driver.save_screenshot("HouseOfDragonScreenshot1.png")

except Exception as e:
    print("Error clicking the link:", e)



# Keep the browser open for 2 minutes (120 seconds)
time.sleep(120)

# Close the browser
driver.quit()
