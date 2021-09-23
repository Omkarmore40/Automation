import time

from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

os.path.basename("C:\\chromedriver.exe")
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("python")
time.sleep(0.5)
driver.find_element_by_name("btnK").click()
fhbcfhbchbdb
fhdfh
dfhd
dfhd
dfhd
fh
