import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def Website_Data_collector():
	'''
	Mixerget reads a text file of bech32 BTC addresses line by line and stores as list
	THe function then navigates to bitmix.biz, enters a btc address, clicks on start mix
	then scrapes the domain provided address and prints it to the screen
	input: user created text file with any amount of single line btc addresses
	'''
	list1 = [] #stores the docuement read data to be input for iteration
	f = open('file.txt', 'r')
	lines = f.readlines()
	n = len(lines)
	for i in range(n):
		lines[i] = lines[i].strip()
	for ele in lines:
		list1.append(ele)
	f.close()

#Most recent Chromedriver
	chrome_driver = webdriver.Chrome()
	chrome_driver.get('input_URL.com')
	chrome_driver.maximize_window()
 
	chrome_driver.find_element_by_name("Name built into source code").click()
    



	
     
	for items in (list1):
		input_slot = chrome_driver.find_element_by_name("Name built into source code")
		input_slot.click() 
		input_slot.send_keys(items)
		# Lines above clicks the desired input box and places a fake address in the box
		sleep(1)
		chrome_driver.find_element_by_id("button on page").click()
		#Line above navigates to next page of website by clicking the desired button
		sleep(3)
		g = chrome_driver.find_element_by_class_name("copy-to-clipboard").get_attribute("text")
		#Line above locates the site provided
		print(g)
		sleep(1)
		chrome_driver.back()
		#Above navigates back one page to restart process
 
   		
	chrome_driver.close()

Website_Data_collector()