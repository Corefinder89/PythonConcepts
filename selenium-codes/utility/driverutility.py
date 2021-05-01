from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/macos/chromedriver")
driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.implicitly_wait(4)
title = driver.title
print(title)
assert title == "Google", "Title does not match"
driver.quit()