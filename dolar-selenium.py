from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

browser=webdriver.Chrome('C:/Users/ATA/chromedriver_win32/chromedriver.exe')

browser.get('https://www.google.com/')
time.sleep(3)

  
input_part=browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_part.send_keys('1 Dolar kaç TL')
input_part.send_keys(Keys.RETURN)
time.sleep(4)

tl_part=browser.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]')
print(tl_part.text)

file = open("dolar-data.txt","a",encoding="utf-8")
file.write('1 Dolar: ' +tl_part.text + "\n")
file.write('Tarih : '+time.strftime('%c') + '\n')
file.write('---------------\n')
