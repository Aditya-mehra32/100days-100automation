from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

title = driver.title

assert title != "", "Website title is missing"

print(" Website test passed")

driver.quit()
