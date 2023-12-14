from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Create A Driver 
driver = webdriver.Chrome(options=chrome_options)
# Open a Website
driver.get("https://linkedin.com")
time.sleep(2)

# Let's login!
username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

# Please replace "my_username" and "my_password" with your own information
username.send_keys("zufirajpoot@gmail.com")
password.send_keys("Hassan5110")

time.sleep(2)

submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
#***************** ADD CONTACTS ***********************

driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=10")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME,"button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)


