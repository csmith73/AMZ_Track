from selenium import webdriver
import time
import random
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup





amazon_link = 'https://www.amazon.com/Cuisinart-CPT-180-Classic-4-Slice-Stainless/dp/B0000A1ZN1/ref=sr_1_7?s=kitchen&ie=UTF8&qid=1544491669&sr=1-7&keywords=toaster'
asin = 'B0000A1ZN1'
o_id_list = ['lSWa8PQabbcaq0UON3B9fCAWpayidBhG59HeWfAwqjKCEDR4pzP6tUQnzUiFgJkwlCxWwzScmEEMdlw0IIRItUpCY8ri3lUJiH1Ap2G%2FLBZ05H8OO6HwPquRJv7kqSm%2FSOuR6QU3cMkEas9U08a0Xew0tQq16iMQ', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGtaRjuPonXdIATEutfQExVQIQi7BzfcYSka9ZVDhr9OZy4KHW%2FD1HsjlYDnMgunJnug6oj%2FYCfr0%3D', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGPPketZleGWYDkSy7iRoT5gjwlS48vUd%2FMa9fPfBgNc7w9djMnwhQR5X7F6E3xnn9Qu2QbRDgZ8YgJoh8VGv8sasiLk5FCeW3C%2FZWKulhcFo6aatSk32InenNzmqtW8k%2B', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGHGtd9UZ1Gxl8hORMJu4tx%2FJEC97d%2BIqYxUwmg0QJkxRMQGPYf41oLafQYVuQPhFaTFWFJr%2Fhn8BGHuhpvzBYPFk1Ne34qoO5WGFrAhI%2B0DfCARYZTAZ8K1GZVzsKeRhG', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGKtElA9ItH9xNo2xG1OZ5J7zRJNCTC9IVi8A61gAE0JpcA%2FAZBLqDEv7Ea8bIk2JFzM715cY2rWmP7hLJWffBQqrPa4kX10Ka8bYBtETeiF%2FDLqP2M%2FW72z7g6Jmaxp7k', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGxFfYciTzwIWwXYBdjagBmLcgTT%2FuZJdoQwRXGXnuJsoq8XRs2x%2BUAyut8O4%2FAYk7cdhwqY6zoi%2B5qLJ6g802szpijXH0bjIFzbA6D5sL8J2hJkw1udvnbw%3D%3D', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGf2v6fF3mNiiKX%2BP%2FsyuObQkNoSHY1ww2EJw0N7WfuUk23%2F3zCUYOXh%2FiSiC7Qeg%2FZpALD5VsZaVewnH4r8B978o2OilT%2FR55oo9USy4BqisfjS44YBijELmcZsBguA%2F6', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGK7Ytq%2FbLNdDQO2zfXLQ%2FayUwa6JBV0AuacQSI3CPzfRm3RWwHSIFmmKLlkWRq5zhPEcfQgp0TYf%2Bzfu8e4RwX6ri%2FCx82F82yNysLRr2nnXfJjn2WR4YMctyGnHhs3gu', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGqV3MY56DgR1Z3AOH3yJdvk1JsU%2BL77tJ4t9JW3ZJT9J2lRDNDdmCB%2FIpSgt%2FnukYtnmRpeRZVF3e8MTeg35%2BQM7vzNOCOpWZxTCG1I%2BD3FUcWgBb7CnN6J9WeA4MkctP', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGP%2FEw%2BzMcPkYLxrzn3ZaK7ntc%2Bt9XbXIzF7W5mUIR3j6VnVF40NGIVMAq6pkR76QLKepywpYrAaxQ9vnRnQr37eP9o7%2B1%2BcXN4uZwm2eY8vRiOiNsF5aB5JcIsGY8%2FHBD']



def get_asin_from_link(amz_link):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome()

    rand = random.random() + .4
    driver.get(amz_link)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source)
    # asin = soup.find('table', id="productDetails_detailBullets_sections1")
    asin = 'No ASIN Found'
    ths = soup.find_all('th')
    for th in ths:
        text = th.text
        text = text.strip()
        if text == 'ASIN':
            asin = th.find_next_sibling().text
            asin = asin.strip()
            print(asin)
    driver.close()
    return asin






def get_offer_id_list(asin):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    offer_link = 'https://www.amazon.com/gp/offer-listing/' + asin + '/'
    #chrome_options=options
    driver = webdriver.Chrome()
    driver.get(offer_link)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source)
    offering_ids = soup.find_all('input', attrs={'name': 'offeringID.1', 'type': 'hidden'})
    offer_id_list = []

    for offer in offering_ids:
        offer_id = offer['value']
        offer_id_list.append(offer_id)
        print(offer_id_list)
    driver.close()
    return offer_id_list

def get_cart_url(offer_id_list):
    cart_url = 'https://www.amazon.com/gp/aws/cart/add.html?'
    i = 0
    for offer in offer_id_list:
        i = i+1
        cart_url = cart_url + 'OfferListingId.' + str(i) + '=' + offer + '&Quantity.' + str(i) + '=10&'
        print(cart_url)
    return cart_url


def get_current_stock(cart_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')


    start_time = datetime.now()
    driver = webdriver.Chrome()
    rand = random.random() + .4

    driver.get(cart_url)
    time.sleep(rand)
    driver.find_element_by_name('add').click()
    time.sleep(rand)
    html = driver.page_source


    soup = BeautifulSoup(html)
    num_list = []
    qty_box = soup.findAll(True, {'name': 'quantityBox'})
    i = 0
    text = ' '
    for qty in qty_box:
        i = i + 1
        num = int(qty.get('value'))
        print(num)
        css_selector_one = "[data-item-count='" + str(i) + "']"
        print(css_selector_one)
        css_selector_two = "[data-item-count='1.1." + str(i) + "']"
        print(css_selector_two)
        exceeded_offer_ids = []
        if num == 10:
            try:
                element2 = driver.find_element_by_css_selector(css_selector_one)
                element2.find_element_by_name("quantityBox").clear()
            except:
                element2 = driver.find_element_by_css_selector(css_selector_two)
                element2.find_element_by_name("quantityBox").clear()
            time.sleep(rand)
            element2.find_element_by_name("quantityBox").send_keys("\b")
            time.sleep(rand)
            element2.find_element_by_name("quantityBox").send_keys("\b")
            print("Cleared quantity box...")
            time.sleep(rand)
            element2.find_element_by_name("quantityBox").send_keys("999")
            print("Typed 999 in quantity box...")
            time.sleep(rand)
            element2.find_element_by_class_name("a-button-text").click()
            print('Clicked update quantity...')
            time.sleep(1)
            try:
                element2 = driver.find_element_by_css_selector(css_selector_one)
            except:
                element2 = driver.find_element_by_css_selector(css_selector_two)
            text = element2.find_element_by_class_name('sc-quantity-update-message').text
            text = element2.find_element_by_class_name('a-alert-content').text

            print('Got alert message text...')
            print(text)
            string_num = [int(s) for s in text.split() if s.isdigit()]
            if "exceeded" in text:
                offer_id = element2.get_attribute('data-encoded-offering')
                exceeded_offer_ids.append(offer_id)
                print(offer_id)
            if "limit" in text:
                print("Limited Quantity " + str(string_num))
                exc_time = datetime.now() - start_time
                print(exc_time.seconds)
            else:
                print(string_num)
                exc_time = datetime.now() - start_time
                print('Time to Execute: ')
                print(exc_time.seconds)
        num_list.append(num)
    #total_qty =  sum(num_list)
    #print(total_qty)


    html_final = driver.page_source
    soup_final = BeautifulSoup(html_final)
    num_list_final = []
    qty_box = soup_final.findAll(True, {'name': 'quantityBox'})
    for qty in qty_box:
        num = int(qty.get('value'))
        print(num)
        num_list_final.append(num)
    total_qty =  sum(num_list_final)
    exceeded_subtraction_offset = 10*len(exceeded_offer_ids)
    total_qty = total_qty-exceeded_subtraction_offset
    print(total_qty)
    driver.close()
    return [total_qty,exceeded_offer_ids]




asin_test = get_asin_from_link(amazon_link)
offer_id_list_test = get_offer_id_list(asin_test)
cart_url_test = get_cart_url(offer_id_list_test)
cur_stock_test = get_current_stock(cart_url_test)

print(asin_test)
print(offer_id_list_test)
print(cart_url_test)
print(cur_stock_test[0])
print(cur_stock_test[1])