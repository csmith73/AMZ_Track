from selenium import webdriver
import time
import random
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup





amazon_link = 'https://www.amazon.com/Tinkering-Labs-Electric-Engineering-Experiments/dp/B01M5GJFQ1/ref=sr_1_11_sspa?ie=UTF8&qid=1549245703&sr=8-11-spons&keywords=robot+kit&psc=1#HLCXComparisonWidget_feature_div'
#asin = 'B0000A1ZN1'
#o_id_list = ['lSWa8PQabbcaq0UON3B9fCAWpayidBhG59HeWfAwqjKCEDR4pzP6tUQnzUiFgJkwlCxWwzScmEEMdlw0IIRItUpCY8ri3lUJiH1Ap2G%2FLBZ05H8OO6HwPquRJv7kqSm%2FSOuR6QU3cMkEas9U08a0Xew0tQq16iMQ', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGtaRjuPonXdIATEutfQExVQIQi7BzfcYSka9ZVDhr9OZy4KHW%2FD1HsjlYDnMgunJnug6oj%2FYCfr0%3D', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGPPketZleGWYDkSy7iRoT5gjwlS48vUd%2FMa9fPfBgNc7w9djMnwhQR5X7F6E3xnn9Qu2QbRDgZ8YgJoh8VGv8sasiLk5FCeW3C%2FZWKulhcFo6aatSk32InenNzmqtW8k%2B', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGHGtd9UZ1Gxl8hORMJu4tx%2FJEC97d%2BIqYxUwmg0QJkxRMQGPYf41oLafQYVuQPhFaTFWFJr%2Fhn8BGHuhpvzBYPFk1Ne34qoO5WGFrAhI%2B0DfCARYZTAZ8K1GZVzsKeRhG', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGKtElA9ItH9xNo2xG1OZ5J7zRJNCTC9IVi8A61gAE0JpcA%2FAZBLqDEv7Ea8bIk2JFzM715cY2rWmP7hLJWffBQqrPa4kX10Ka8bYBtETeiF%2FDLqP2M%2FW72z7g6Jmaxp7k', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGxFfYciTzwIWwXYBdjagBmLcgTT%2FuZJdoQwRXGXnuJsoq8XRs2x%2BUAyut8O4%2FAYk7cdhwqY6zoi%2B5qLJ6g802szpijXH0bjIFzbA6D5sL8J2hJkw1udvnbw%3D%3D', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGf2v6fF3mNiiKX%2BP%2FsyuObQkNoSHY1ww2EJw0N7WfuUk23%2F3zCUYOXh%2FiSiC7Qeg%2FZpALD5VsZaVewnH4r8B978o2OilT%2FR55oo9USy4BqisfjS44YBijELmcZsBguA%2F6', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGK7Ytq%2FbLNdDQO2zfXLQ%2FayUwa6JBV0AuacQSI3CPzfRm3RWwHSIFmmKLlkWRq5zhPEcfQgp0TYf%2Bzfu8e4RwX6ri%2FCx82F82yNysLRr2nnXfJjn2WR4YMctyGnHhs3gu', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGqV3MY56DgR1Z3AOH3yJdvk1JsU%2BL77tJ4t9JW3ZJT9J2lRDNDdmCB%2FIpSgt%2FnukYtnmRpeRZVF3e8MTeg35%2BQM7vzNOCOpWZxTCG1I%2BD3FUcWgBb7CnN6J9WeA4MkctP', 'lSWa8PQabbcaq0UON3B9fCAWpayidBhGP%2FEw%2BzMcPkYLxrzn3ZaK7ntc%2Bt9XbXIzF7W5mUIR3j6VnVF40NGIVMAq6pkR76QLKepywpYrAaxQ9vnRnQr37eP9o7%2B1%2BcXN4uZwm2eY8vRiOiNsF5aB5JcIsGY8%2FHBD']
#cart_url = 'https://www.amazon.com/gp/aws/cart/add.html?OfferListingId.1=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1%2BmONL1OWcZ7qkwNNEbvu%2BShUjrUpBdrp3FW7JIh5O2Rl5xomr7Hy2JS%2BKfP02gNLODX4d8NqH7w%3D&Quantity.1=10&OfferListingId.2=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1zzyJBWkoBKMSZ4C%2BL%2FVge2EWn7N0v1wbbPCifXWBdXV9JoACdXDE1PKXE80VQsa7aEdm92sSKnGpxt6bG9oUQWPmGahkJNnPeevVdJqAOADn17Xk2g6db1vR%2BJFmADom&Quantity.2=10&OfferListingId.3=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1wOorZvqABc1PTr8UeHnEO1%2B2hrIwdLgRXiAhpzYdWaJsMsU6pIF34JzoQREGgT6JxcxsEr5WWdciehY4Zz%2Fvw0E37SKVVgMsm5zJ83UllmFa%2F4p%2FnM6mWM5jTbivN51%2B&Quantity.3=10&OfferListingId.4=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1%2FiU%2BMYgh0Ms7eV7arwdMCOsR7sCjryG6GypxbGRAJxfmb8DGLSUnzf2xHhek4YkfnQPJJxM6MWksoUS1n7qYI4H35l2X3rXHzhs0c6Y5AYSvjAs3C1RJ6g%3D%3D&Quantity.4=10&OfferListingId.5=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1STGF65mplRkrJnfh0mjlDozFcClTfitcxBEZsVXUFR8cR%2BGZNrxSh2LLM6%2FQ3zW1HXXGH%2BN5ysucwchylg1prrJmZrj6oU2XqgXzI8PKyHAlsSVozmjShETywJjyxUWh&Quantity.5=10&OfferListingId.6=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1FnnRb%2F8nPVkMnZzu30qNKrKIsGfSYbabOcVZDdvWrMjDwLGKWT%2FZC2X1ZMbC56fAktjROdbx1EmeyAqPOCy%2BMTidPGVk%2BJCQnFZQU7awaG8Ymj1DfQquhGGhw30MJZnY&Quantity.6=10&OfferListingId.7=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB19va4JN9BdJaEdSwWLEp7okl3SWVbkukGq92sncuVTQMwNdDC8CKHjyZ5RsCIa%2BaCssThAfLmYcJMMB78uFRr5hSX5YS839IqlhrtgmA4YsV7OHdnFpbANF6Dq%2FS%2F%2BleF&Quantity.7=10&OfferListingId.8=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1yfEzzqwYlk%2BjwGtK3aLvHnwWvKzhhT9a2bPBVAKK%2BUC5dICawNnIJ9xpX16IYj6bjCqZC0GI9tzl4uhf%2FtNkHzV7PTNDvEpsovlT1Rwd2moHPnBsmyVvyZr0xYetGqVg&Quantity.8=10&OfferListingId.9=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1quFSPqA1qbH%2FMZyt5%2F%2FtnJGfiHU4qocGxkCQcAL7M8vWtUMEEsr5OlMZ4I2iKFGRJOVVE9bu80hgSOOJ4rE0bqo%2BpMQVqHbTCCzIXCa3yLc01yuN6y%2Bdpg%3D%3D&Quantity.9=10&OfferListingId.10=6RyFFTlJYaKF0zLeVHWpZhj%2F8F3mAmB1%2FSqWIIYc%2FcY7QvSG%2FCevXwfVjBzZ7qI8kxR2sZnX0OTv%2BaNnigiQEEE9cFpKDPe9bCDMSCRwKYu3oysCsiVDTSYqyMr8PQ%2FaVx3JQnexjHqvyFb4z0JUFdJf0hx94g1y&Quantity.10=10&'
#spat_cart_url = 'https://www.amazon.com/gp/aws/cart/add.html?OfferListingId.1=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQbxV%2Fa8yGTT1uNVGvZhQBYi8wZoAxHspB9%2Fpil6L1Vk7iO7oWOWecfA6qqRVRi9vRdQSZSFbg0Hc%3D&Quantity.1=10&OfferListingId.2=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQUXYjK%2BNZ%2FMsfHsxl4dZbAvC0DBGC9C7XnEl75GB7j8cHWYs4msEy5Bz%2ByEvhG0pe11YjFv1LJT4HENyEyy1a2BfvFuYL65nT0nBJY907Bytp0bc7Vy4bHQ%3D%3D&Quantity.2=10&OfferListingId.3=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQH1ym%2Bgp7aDR62ze%2BWDLe4eBfFw3B0kRU35I%2Bvrs6Ghz0mQktu4evzDds%2FzWKfk9kZP2kdYzZ%2FMhg3Qj83gCd7pk%2F9w6nsrjFDLoIzs5S6aUEuH9%2BgzbhuFtrmxTWfRcM&Quantity.3=10&OfferListingId.4=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQtDHjhxCaRIHFqorpn9tVrnvtlHXIaX1eC4hEAMXmj7Nz77cR6a%2BH8Eo%2FKUSNGi%2BNfQe0QnKgNExMdD3DqHkRMasdAqTbUkF0%2F7QTE9aIRmp0gXBIed8BQQ%3D%3D&Quantity.4=10&OfferListingId.5=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQgIRuScvnHqajflLHC%2F3cvpz8wRc1oOmQL3sBeFG0fzSGM8kOJEow8Or48p7panqpJvAuAvZ%2FMtKBBKFZJ7beF3iLxqojBfjbpWyA7OopW2WgFLnXjFXbWDP3l8v%2BK0aY&Quantity.5=10&OfferListingId.6=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQQ0M1C8R1TZHxCIrQJ4Mw0tbPBfHm7TcIZpeMv9ifsczf8C1VTNhIT88GSq9ak85YSun5SAIc8eNuH4AMr5SxCaMvKFtog3D2ewTtxls%2BIrZ7n9gBoWaBIY%2B4jRxDuabq&Quantity.6=10&OfferListingId.7=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQElCauPR7yJm71ZQuqJD6P8GMkZVyDUZ5xVIpdKptT1noLUx7ds7eEsqAEuFrwBe6mbizVgE9LDA8b8zzYWsDP8d%2BJF%2BLZTN0wNIs4wEZABdMpldTUOa0fJ6eCAGESQik&Quantity.7=10&OfferListingId.8=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQ01kVhkjwjqt%2FxdwB8hQsykleX31aHYCSijH4s0m7WuCjjO8Jlbw2H89uttqfc6dSKcFnMlJGU0MCm%2Bhdd3BNEf%2Fi94hrng8gVz0msCzkASuZb96vXjdf2Q%3D%3D&Quantity.8=10&OfferListingId.9=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQzDIkJRoEAsyimnTFKRCJtE%2BYhBjMzsXRm2mX3pAuf4jPa4VhaiSFSKAG%2BqEs0k3wYmc6eFR9%2Btfp%2BG6GRROCSXTRvypzQCTKTU%2BXltE%2B%2F6etCKdStzhrl27IrZcatZbx&Quantity.9=10&OfferListingId.10=mWGiHtopr5zvHt67NEPVKqBuDs3JkELQzhIFsOI2RHSqZIoQ0RWvg6gZbAlMideA434hjjlBTO9bmzvsE8H%2FbTJ9CV33%2FUdcen%2FOoMlDHuAnH6FR6oUo7ZmddnuSfTrc8NdOgN9MEx5KtTii7%2FqKW2dYRLmLSeCv&Quantity.10=10&OfferListingId.11=Do5LULQcifc94hWLdcjFz9%2BDPYf8WRrUY5NlrmUKZ6hksfRoi5ZVEQSntGBRWJ3Zz%2F00kvmxB6%2FHMnFcwOp7Nw2uNbHhs9zZW6UrIbgaWnZchj%2BYe%2BSJHSzNWQ2S2I6nL01SEaBd3Lw3polLWMIcUg%3D%3D&Quantity.11=10&OfferListingId.12=Do5LULQcifc94hWLdcjFz9%2BDPYf8WRrUq4fVoxwrRlCqXmxC1P3CmYErSWgy4DpZGmj8IiMs0sAZXqTgZUIgm75y%2BZKwJPyqSuwJjhO4xATXAot%2Fv6yBrKyBB2blfyZhbn0R4eijzzQpLNatiuvAs9MXS%2BIfFaW4&Quantity.12=10&OfferListingId.13=Do5LULQcifc94hWLdcjFz9%2BDPYf8WRrU7%2F0SCDkEQ2IOMO2W6y9nwKOwkGvRBIwhTZXusNZ4R15Cq%2B8%2F0keDRh9Ncc3Tum5B7mm9HuaqqcMswHLh1ElbqvB5P98Kwec3sLwMueekmsyklNKx%2BSxSf5dZwWyKOR1z&Quantity.13=10&'
one_page_cart_url = 'https://www.amazon.com/gp/aws/cart/add.html?OfferListingId.1=MOqgOV%2Fjpmm9STDjmEusEu%2F1CoLXgwGZRHKyVU6rcGIMWsSiBNXWCZ7PGg02vi46h6pPoihDVNJxqW8731II4P6ibNItq5I9CEvyX4%2BSraMl6fCmqHcbclcmaKwkGFFwf2qY8sPXni4ieSF8kwl7SfSE1l1VzMcU&Quantity.1=10&OfferListingId.2=MOqgOV%2Fjpmm9STDjmEusEu%2F1CoLXgwGZRHKyVU6rcGIMWsSiBNXWCZ7PGg02vi46h6pPoihDVNJzAjMLYK%2Fi7C%2BQtituibWw5uFXk7Yyn5MMqni0artPqAqMsyzvKE%2FM%2BGVDTD%2FUx7JWzylMZRfz7KbkS95AULt7&Quantity.2=10&OfferListingId.3=MOqgOV%2Fjpmm9STDjmEusEu%2F1CoLXgwGZhLhNKm9FN294wq1t2B0NexKz8wB0wa2yu4ceBgJZJNqpaSH0WRY4%2BeciONs%2BYySBwmD68szIfxdqbjZzgOn%2FiSs3Ocd7joVMlg6s3kzu3xUh00U%2FWBaIikI3Q39ruOHq&Quantity.3=10&'
def get_asin_from_link(amz_link):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument(
    #     '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
    # driver = webdriver.Chrome(executable_path='/dev/chromedriver', chrome_options=chrome_options,
    #                           service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
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
    print(asin)
    return asin






def get_offer_id_list(asin):
    is_multiple_pages = True
    rand = random.random() + .4
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument(
    #     '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
    # driver = webdriver.Chrome(executable_path='/dev/chromedriver', chrome_options=chrome_options,
    #                           service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    driver = webdriver.Chrome()
    offer_link = 'https://www.amazon.com/gp/offer-listing/' + asin + '/'
    #chrome_options=options
    driver.get(offer_link)
    print(offer_link)


    #Detect pagination and call get_offerids_on_single_page() for each page.
    try:
        driver.find_element_by_class_name('a-pagination')
    except:
        is_multiple_pages = False

    offer_id_list = []
    if is_multiple_pages == True:
        pages = driver.find_element_by_class_name('a-pagination')
        pages = pages.find_elements_by_css_selector('li')
        pages = len(pages) - 2
        total_pages = pages
        print(pages)

        for page in range(pages):
            time.sleep(rand)
            print("Current Page: ")
            print(page+1)
            page_id = page + 1
            start_index = (page_id * 10)-10
            offer_listing_url = 'https://www.amazon.com/gp/offer-listing/' + asin + '/ref=olp_page_'+ str(page_id) +'?ie=UTF8&f_new=true&startIndex=' + str(start_index)
            driver.get(offer_listing_url)
            page_source = driver.page_source
            single_page_offer_id_list = get_offerids_on_single_page(page_source)
            offer_id_list = offer_id_list + single_page_offer_id_list
            time.sleep(rand)
            print(offer_id_list)
    else:
        total_pages = 1
        offer_listing_url = 'https://www.amazon.com/gp/offer-listing/' + asin + '/ref=dp_olp_all_mbc?ie=UTF8&condition=all'
        driver.get(offer_listing_url)
        page_source = driver.page_source
        single_page_offer_id_list = get_offerids_on_single_page(page_source)
        offer_id_list = offer_id_list + single_page_offer_id_list
        time.sleep(rand)
        print(offer_id_list)

    return [offer_id_list,total_pages]


def get_offerids_on_single_page(page_source):
    soup = BeautifulSoup(page_source)
    offering_ids = soup.find_all('input', attrs={'name': 'offeringID.1', 'type': 'hidden'})
    offer_id_list = []

    for offer in offering_ids:
        offer_id = offer['value']
        offer_id_list.append(offer_id)
        #print(offer_id_list)
    return offer_id_list

def get_cart_url(offer_id_list):
    cart_url = 'https://www.amazon.com/gp/aws/cart/add.html?'
    i = 0
    for offer in offer_id_list[0]:
        i = i+1
        cart_url = cart_url + 'OfferListingId.' + str(i) + '=' + offer + '&Quantity.' + str(i) + '=10&'
        print(cart_url)
    return cart_url

def scan_cart(cart_url):
    driver = webdriver.Chrome()
    start_time = datetime.now()

    rand = random.random() + .4

    driver.get(cart_url)
    time.sleep(rand)
    driver.find_element_by_name('add').click()
    time.sleep(rand)
    html = driver.page_source

    soup = BeautifulSoup(html)

    qty_box = soup.findAll(True, {'name': 'quantityBox'})
    qty_list = []
    for qty in qty_box:
        qty_value = qty['value']
        print(qty)
        print(qty['value'])
        qty_list.append(qty_value)
        print(qty_list)

    sellers = soup.findAll(True, {'class': 'sc-seller'})
    seller_list = []
    for seller in sellers:
        seller_name = seller.findAll('a')[0].string
        seller_name = seller_name.strip()
        print(seller_name)
        seller_list.append(seller_name)
        print(seller_list)
    seller_qty_dict = dict(zip(seller_list, qty_list))
    print(seller_qty_dict)

    offer_ids = soup.findAll(True, {'class': 'sc-list-item'})
    data_encoded_offering_list = []
    for offer_id in offer_ids:
        data_encoded_offering = offer_id['data-encoded-offering'].strip()
        print(data_encoded_offering)
        data_encoded_offering_list.append(data_encoded_offering)

    data_offering_qty_dict = dict(zip(data_encoded_offering_list, qty_list))
    print(data_offering_qty_dict)

def get_current_stock(cart_url):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument(
    #     '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
    # driver = webdriver.Chrome(executable_path='/dev/chromedriver', chrome_options=chrome_options,
    #                           service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    driver = webdriver.Chrome()
    start_time = datetime.now()

    rand = random.random() + .4

    driver.get(cart_url)
    time.sleep(rand)
    driver.find_element_by_name('add').click()
    time.sleep(rand)
    html = driver.page_source

    soup = BeautifulSoup(html)

    qty_box = soup.findAll(True, {'name': 'quantityBox'})
    qty_list = []
    for qty in qty_box:
        qty_value = qty['value']
        print(qty)
        print(qty['value'])
        qty_list.append(qty_value)
        print(qty_list)

    sellers = soup.findAll(True, {'class': 'sc-seller'})
    seller_list = []
    for seller in sellers:
        seller_name = seller.findAll('a')[0].string
        seller_name = seller_name.strip()
        print(seller_name)
        seller_list.append(seller_name)
        print(seller_list)
    seller_qty_dict = dict(zip(seller_list, qty_list))
    print(seller_qty_dict)

    offer_ids = soup.findAll(True, {'class': 'sc-list-item'})
    data_encoded_offering_list = []
    for offer_id in offer_ids:
        data_encoded_offering = offer_id['data-encoded-offering'].strip()
        print(data_encoded_offering)
        data_encoded_offering_list.append(data_encoded_offering)

    data_offering_qty_dict = dict(zip(data_encoded_offering_list, qty_list))
    print(data_offering_qty_dict)


    num_list = []
    i = 0
    text = ' '
    for qty in qty_box:
        i = i + 1
        print('i value:')
        print(i)

        num = int(qty.get('value'))
        print(num)
        css_selector_one = "[data-item-count='" + str(i) + "']"
        print(css_selector_one)
        css_selector_two = "[data-item-count='1.1." + str(i) + "']"
        print(css_selector_two)

        try:
            element2 = driver.find_element_by_css_selector(css_selector_one)

        except:
            element2 = driver.find_element_by_css_selector(css_selector_two)



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
                element2.find_element_by_css_selector("input[value='Delete']").click()
                print(offer_id)
                i = i - 1
                print('i value changed:')
                print(i)
                time.sleep(2)
            if "limit" in text:
                print("Limited Quantity " + str(string_num))
                exc_time = datetime.now() - start_time
                print(exc_time.seconds)

            #else:
                #print(string_num)
                #exc_time = datetime.now() - start_time
                #print('Time to Execute: ')
                #print(exc_time.seconds)
        if num < 10:
             offer_id = element2.get_attribute('data-encoded-offering')
             exceeded_offer_ids.append(offer_id)
             element2.find_element_by_css_selector("input[value='Delete']").click()

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
    print(total_qty)
    #driver.close()
    return data_offering_qty_dict




#asin_test = get_asin_from_link(amazon_link)
#offer_id_list_test = get_offer_id_list(asin_test)
#cart_url_test = get_cart_url(offer_id_list_test)
cur_stock_test = get_current_stock(one_page_cart_url)

#print('Final ASIN')
#print(asin_test)
#print('Final offer_id_list_test')
#print(offer_id_list_test)
#print(cart_url_test)
