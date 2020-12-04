from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("https://10fastfingers.com/advanced-typing-test/english")
delay = 10
WebDriverWait(driver, delay).until(expected_conditions.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").send_keys(Keys.ENTER)
sleep(2)
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")
for word in words :
    driver.find_element_by_id("inputfield").send_keys(word+" ")
    sleep(0.2)
