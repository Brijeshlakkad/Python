#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def sub():
	nxt=browser.find_element_by_xpath("//content/span")
	nxt.click()
user=input("Enter Email Adress : ")
password=input("Enter Password : ")
print("calling firefox...")
browser = webdriver.Firefox()
print("connecting.... ")
browser.get('https://mail.google.com')
print("server connected :)")
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys(user)
sub()
browser.implicitly_wait(100)
passwordElem = browser.find_element_by_tag_name("div").find_element_by_name('password')
browser.implicitly_wait(100)

for i in password:
	passwordElem.send_keys(i)
	browser.implicitly_wait(10)

passwordElem.send_keys(Keys.RETURN)

print("done")
