from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/Medini/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
# to get emojis windowskey plus (.)
# print("😊")
# target='"Gouthami"'
# target='"Nisha"'
target='"Amma"'
string="Hi amma how are you"
x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()

# driver.get("https://www.seleniumhq.org")
# elem=driver.find_element("link text","Downloads")
# elem.click()


input_box=driver.find_element('class name','p3_M1')

for i in range(10):
    input_box.send_keys(string+Keys.ENTER)