from selenium import webdriver
import time
import random
import sqlite3
from datetime import datetime


start_time = datetime.now()
asin = 'B076FWF28T'
url_page = "https://www.amazon.com/gp/offer-listing/" + asin


driver = webdriver.Chrome()
rand = random.random() + .4

driver.get(url_page)
driver.find_element_by_id("add-to-cart-button").click()
print("Added item to cart...")
time.sleep(rand)

try:
    driver.find_element_by_name("submit.addToCart").click()
    time.sleep(2)
    driver.find_element_by_id("attach-close_sideSheet-link").click()
except:
    pass
time.sleep(rand)
driver.find_element_by_id("nav-cart").click()
print("Clicked the cart button...")
#driver.find_element_by_id("hlb-view-cart-announce").click()
time.sleep(rand)
driver.find_element_by_id("a-autoid-0-announce").click()
print("Clicked the dropdown for quantity in cart...")
time.sleep(rand)
driver.find_element_by_id("dropdown1_9").click()
print('Clicked 10+ in dropdown...')
time.sleep(rand)
driver.find_element_by_name("quantityBox").clear()
time.sleep(rand)
driver.find_element_by_name("quantityBox").send_keys("\b")
print("Cleared quantity box...")
time.sleep(rand)
driver.find_element_by_name("quantityBox").send_keys("999")
print("Typed 999 in quantity box...")
time.sleep(rand)
driver.find_element_by_id("a-autoid-1-announce").click()
print('Clicked update quantity...')
time.sleep(rand)
text = driver.find_element_by_class_name('sc-quantity-update-message').text
print('Got alert message text...')
string_num = [int(s) for s in text.split() if s.isdigit()]
if "limit" in text:
   print("Limited Quantity "+str(string_num))
   exc_time = datetime.now() - start_time
   print(exc_time.seconds)
else:
    print(string_num)
    exc_time = datetime.now() - start_time
    print(exc_time.seconds)

