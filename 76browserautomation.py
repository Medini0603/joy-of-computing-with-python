# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # browser=webdriver.Chrome("C:/Users/Medini/Downloads/chromedriver_win32/chromedriver")
# # driver.get("C:/Users/Medini/Downloads/chromedriver_win32/chromedriver")
# driver.get("https://www.google.com")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/Medini/Downloads/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)
# url='https://www.google.com'
# browser.get(url)
browser.get("https://www.seleniumhq.org")
elem=browser.find_element("link text","Downloads")
elem.click()

browser.get("https://www.google.com")
idk=browser.find_element("id","input")
idk.send_keys("Downloads")