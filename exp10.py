from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Open browser
driver = webdriver.Chrome()

# Open local HTML file
driver.get("file:///C:/Users/Simoni Raghatate/OneDrive/Desktop/Sqat/index10.html")

time.sleep(2)

# Find dropdown
dropdown = driver.find_element(By.ID, "city")

# Use Select
select = Select(dropdown)

# Count items
count = len(select.options)

print("Total items in list:", count)

time.sleep(2)

# Close browser
driver.quit()