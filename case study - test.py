from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#Step 1 - Accessing weekend url sceranio
browser = webdriver.Chrome()
browser.get("https://weekend.trivago.co.uk/")
time.sleep(5)
#Step 2 - Set a country city or town scenario
destination = browser.find_element_by_class_name("DestinationControl_emptyState__30M-R")
destination.click()

#Step 3 - Select Accra from dropdown list scenario
dropdown = browser.find_element_by_class_name("DestinationItem_subline__M9FNQ")
dropdown.click()

#Step 4 - Scroll down page scenario
browser.find_element_by_xpath("//body").click()
browser.execute_script("window.scrollTo(0,1000);")
browser.find_element_by_xpath("//body").click()

#Step 5 - Select hotel scenario
browser.execute_script("window.scrollTo(0,1500);")
time.sleep(5)
hotel = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/ul/li[2]/div[2]/div/div/section/ul/li[5]/div/div[3]/div/div[2]/div[2]/button/span/span[1]")
hotel.click()







