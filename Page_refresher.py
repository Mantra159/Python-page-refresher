from selenium import webdriver
import time
    
URL = input("Enter the URL: ")
refreshrate = int(input("Enter the number of seconds: "))
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get(URL)

while True:
    time.sleep(refreshrate)
    driver.refresh()