#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click()