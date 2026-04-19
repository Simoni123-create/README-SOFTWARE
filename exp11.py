from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open local HTML page
driver.get("file:///C:/Users/Simoni Raghatate/OneDrive/Desktop/Sqat/index11.html")

time.sleep(2)

# Find all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

checked = 0
unchecked = 0

# Check status
for box in checkboxes:
    if box.is_selected():
        checked += 1
    else:
        unchecked += 1

# Print result
print("Checked Checkboxes:", checked)
print("Unchecked Checkboxes:", unchecked)
print("Total Checkboxes:", len(checkboxes))

time.sleep(2)

# Close browser
driver.quit()