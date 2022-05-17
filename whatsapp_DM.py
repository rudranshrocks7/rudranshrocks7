from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.keys import Keys
os.environ['PATH'] += r"D:\Selenium\chromedriver_win32"
currentPath = __file__.split("main.py")[0]
driverPath = r"D:\Selenium\chromedriver_win32"
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(options=chromeOptions)
driver.get("http://web.whatsapp.com")
print("Loading Page")
elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME ,"_1lPgH"))
)
print("Page Loaded")
name = input("Enter the contact's name : ")
msg = input("Enter the message : ")
try:
    user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[1]')
    time.sleep(2)
    div = driver.find_elements(By.CLASS_NAME, "_13NKt.copyable-text.selectable-text");
    div[1].send_keys(msg)
    but = driver.find_element(By.CLASS_NAME, "_3HQNh._1Ae7k")
    but.click()
    print("Message Sent!")
    driver.quit()
except:
    print()
    driver.quit()

