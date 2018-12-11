from bs4 import BeautifulSoup

soup = BeautifulSoup(open("example_offer_listing.html"), "lxml")
offering_ids = soup.find_all('input', attrs={'name':'offeringID.1', 'type':'hidden'})
offer_id_list = []

for offer in offering_ids:
    offer_id = offer['value']
    offer_id_list.append(offer_id)
    print(offer_id_list)




# qty_dropdown = soup.findAll(True, {"class": "a-dropdown-prompt"})
# num_list = []
# for qty in qty_dropdown:
#     num = int(qty.text)
#     num_list.append(num)
# print(sum(num_list))
# print(num_list)

# num_list = []
# qty_box = soup.findAll(True, {'name': 'quantityBox'})
# for qty in qty_box:
#     num = int(qty.get('value'))
#     #print(num)
#     num_list.append(num)
# total_qty =  sum(num_list)
# print(total_qty)

#asin = soup.find('table', id="productDetails_detailBullets_sections1")
# ths = soup.find_all('th')
# for th in ths:
#     text = th.text
#     text = text.strip()
#     if text == 'ASIN':
#         asin = th.find_next_sibling().text
#         asin = asin.strip()
#         print(asin)