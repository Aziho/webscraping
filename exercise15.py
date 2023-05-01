import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

Driver_path="C:/Users/surface/PycharmProjects/ChromeDriver/chromedriver"
URL="https://www.bcit.ca/study/programs/5512cert#courses"
browser=webdriver.Chrome(Driver_path)
browser.get(URL)
time.sleep(3)
content=browser.find_elements(By.CSS_SELECTOR,".clicktoshow")
for e in content:
    start=e.get_attribute('innerHTML')
    soup=BeautifulSoup(start, features='lxml')
    print(soup.get_text())
    print('****')