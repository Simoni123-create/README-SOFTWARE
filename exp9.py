from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open local HTML page
driver.get("file:///C:/Users/Simoni Raghatate/OneDrive/Desktop/Sqat/index.html")

time.sleep(2)

# Count all objects
all_objects = driver.find_elements(By.TAG_NAME, "*")
print("Total Objects on Page:", len(all_objects))

# Count specific tags
tags = ["div", "p", "span", "a", "button", "input", "img"]

for tag in tags:
    elements = driver.find_elements(By.TAG_NAME, tag)
    print(tag.upper(), ":", len(elements))

time.sleep(2)

# Close browser
driver.quit()