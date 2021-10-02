from selenium import webdriver
import time
from datetime import datetime
import pynput
from pynput.keyboard import Controller,Key
isStarted=True
import webbrowser
import sys
url="https://www.prepbytes.com/login"

while isStarted:
     if datetime.now().hour ==19 and  datetime.now().minute ==9: 
      driver=webdriver.Chrome("D:/C++Codes/chromedriver")
      driver.get(url)
      driver.find_element_by_name("email_input").send_keys("ksharma5_be20@thapar.edu")
      driver.find_element_by_name("password_input").send_keys("@Keshav5548")
      driver.find_element_by_xpath('//button[normalize-space()="Sign In"]').click()
      time.sleep(4)
      driver.close()
      isStarted=False
      