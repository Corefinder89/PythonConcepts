from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def spawn_driver():
    try:
        driver = webdriver.Chrome("../python-basics/chromedriver")
        driver.get("https://computer-database.gatling.io/computers")
        driver.implicitly_wait(10)
        driver.maximize_window()
        xpath_button = "//*[@id='add']"
        xpath_computer_name = "//input[@id='name']"
        xpath_introduced = "//input[@id='introduced']"
        xpath_discontinued = "//input[@id='discontinued']"
        xpath_company = "//*[@id='company']/option[@value='3']"
        xpath_create_computer = "//input[@type='submit']"
        driver.find_element(By.XPATH, xpath_button).click()
        driver.find_element(By.XPATH, xpath_computer_name).send_keys("corefinder's_macbook")
        driver.find_element(By.XPATH, xpath_introduced).send_keys("2021-05-23")
        driver.find_element(By.XPATH, xpath_discontinued).send_keys("2021-05-30")
        driver.find_element(By.XPATH, xpath_company).click()
        driver.find_element(By.XPATH, xpath_create_computer).click()

        sleep(4)
    except WebDriverException as e:
        print(e)

spawn_driver()
