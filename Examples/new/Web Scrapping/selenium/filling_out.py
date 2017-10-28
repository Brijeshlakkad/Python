#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

from selenium import webdriver
def sub():
	nxt=browser.find_element_by_tag_name("content").find_element_by_tag_name("span")
	nxt.click()

browser = webdriver.Firefox()
browser.get('https://mail.google.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('brijeshlakkad22@gmail.com')
sub()

#below will not run
#i=0
#while i<10:
#	i=+1
#passwordElem = browser.find_element_by_tag_name("div").find_element_by_name('password')
#passwordElem.send_keys('124567267b')
#sub()
print("done")