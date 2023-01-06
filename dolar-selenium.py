from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


browser=webdriver.Chrome('C:/Users/ATA/chromedriver_win32/chromedriver.exe')

browser.get('https://www.google.com/')
time.sleep(3)
