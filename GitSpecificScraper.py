import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def Website_Data_collector():
	'''
	Website_Data_collector reads a text file of items line by line and stores as list
	The function then navigates to a website, enters an item, clicks on a required location
	then scrapes the domain provided address and prints it to the screen
	input: user created text file with website input data
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
