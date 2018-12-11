import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import time
import sqlite3


url_page = 'https://www.junglescout.com/estimator/'

browser = webdriver.Chrome()
browser.get(url_page)
rank = 1446
count = 64
results = []
sales_num = 101
category = 'Clothing, Shoes & Jewelry'
conn = sqlite3.connect("Estimator_Data_DB.db")
c = conn.cursor()


while sales_num >= 100:
    count = count + 1
    inputElement = browser.find_element_by_name("theRankInput")
    inputElement.send_keys(rank)

    inputElement = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Amazon Marketplace'])[1]/following::input[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Amazon Marketplace'])[1]/following::span[2]").click()
    time.sleep(1)
    browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Amazon Product Category Amazon Marketplace'])[1]/following::input[1]").click()
    time.sleep(1.5)
    #browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Amazon Product Category Amazon Marketplace'])[1]/following::li[5]").click()
    browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Clothing & Accessories'])[1]/following::span[1]").click()
    time.sleep(1)
    browser.find_element_by_link_text("Calculate sales!").click()
    time.sleep(3)
    text = browser.find_elements_by_class_name("js-magic-result")
    sales = text[0].text
    c.execute('''INSERT INTO Sales_Data(Category,Rank,Sales) VALUES(?,?,?)''',(category,rank,sales))
    conn.commit()
    print(sales)
    print(rank)
    print(category)
    print(type(sales))
    print(count)
    if sales != "N.A." or sales != "":
        sales_num = int(sales.replace(',', ''))

    browser.find_element_by_link_text("Clear selection").click()
    if count <= 20:
        rank = rank + 5
    if count > 20 and count <= 50:
        rank = rank + 20
    if count >50 and count <= 100:
        rank = rank + 50
    if count > 100:
        rank = rank + 100