from bs4 import BeautifulSoup

id_list_ex = [['Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn65WtNjD%2BuCXt%2BWCbqSZAD5kfSbb19r7M9XzY7LEExUdMuY07ndV5G1DrXvbdQMldvpjCGGMHU1h4%3D', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6JacXErd8rAj%2Bf8RwnI0i6ov%2B3Tc6PbzuQ0w9eyYEKLRfQlKuNubUnB9uMRet3hK72Rjt0XPwm1QHJ8k3H8FNuMvnt%2BsfI5YKWSqbZqpHDaiXujMfhjnITsDQYHJ3DCin', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6h%2BlFjGZ5GVoYQLBuqs1nEkGACps87H5aXPkbBhKERtpi33VKvRuwD2%2BMLtNM1G4uJCXPao2VkJgT8Ng7YlW%2FAxGOHpDWSdCfHZWMMQBcpRXi6ql076y3XAvT4pxZCjLc', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6shrmZubVdMP6zyzuY5uzWiqaSh4xuCusy%2B4WRCEIhxcPr0CE8BJU%2BDMtr0Sb%2Fh6ooeVt5BdO5a2VOkoMPRXI2bEuQ2Ddygbc0tsgBXLrUf88KZj1%2BSAfUw%3D%3D', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn65GaNdk2l5Mdt3BDjLgxh3YJdZ5yhWUK6nxBhZqv24aVVztttrtqipD1lDpXyOc9GcS0VAi%2F7TzFpAvvFDKgUv2t1UFHfNsvz4skhI%2FEHpSGcB%2BUeIZU2J4GI3sozlT0f', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6tMg%2BHAFXTJGw3ZOQcN1m%2BsuR%2BqSetYCz43IjUdIHT4PiVZ0upBzhL6rjyfoV5TAmc5k7BIuCeYgX%2BmeurqARgzy2d3jae1PP8S5t1kAXrugOhUZQc%2BxaEDPclj1hPVnN', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn66Si4AYdoygepbcB%2Fom7WvLCsFl8ASjXjSwmhkmM2Zn%2BIpC4pqQdBhio%2FIvOTYuqphmfp2iPSywyPkw5nt3Bh6nulVOCKSFwPasV3M65MQVErcn8LQ8t3TOx4RkwAaeW4', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6qusZ64JdppnfEdxQIltlrC6HqUlOMAn5AwIAtirWB9Yw%2BK%2BqplcAE%2F4QgbMiQotcGiPNr7uUHxDfCwjMHCGt7abeVJkuHN3n5hIloxUOBrZSZrozIlDToh7SEP6AwpSO', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6eHWbmrFKC578GG9MMq9M3d3K3pJaQ%2F0E0fNEVQubJW1jBWihXqtiCBapkfTgu7aRC17R8LmpzmIBv04iI33ve%2F7iskTbSCNebK11qVhCawYqsWpDjcEQWsdAP8uQTQmH', 'Q045Ox3eIOBoEYJw0AmeOT9tOb0zsWn6Y1cwxmauBqiQemwXJizCNVT280lesxeRFkkl3wx%2F43pnGing2TKteUNyCAhUv%2FzTa8pMxlhi8BcWGssWvT4U%2FQC2gi0UoKLrEUF2LWArwaVLPZ9d7W55UA%3D%3D'], ['j9u6WhbqWmjihRIU7uKDebVafzOEiZw709iVL%2FCk15Vgscc1B2bPklZijkjt45urQXPKbKHjOE0rbLYyrzbO5ES1RcK27EzyxHOVD9rcRUtUfVq5gRmb20670quDvdmWN1Y2r%2FeVjqKYtPWn3nmL1Q%3D%3D', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw75%2Fg1xQiycjPy5%2BoaSwWzQkZl%2F8Z4cNsH%2FLRs38mofZ3IEX4j7xJZi0i%2B%2Fxd6obrmIXh6KKYCzCqTPmRkrzOG1Gc8eE1N%2Bv5kZCPWcr3UJfMrVHHekPjmuTPDZkDt5pr5', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7f0eFw7Vt2kpJUbdhotne8gwYnlQScaljpelKhEKIKQu0la%2FvAnhTT6DcRWCjQTbWpksImT8jUyPFRWgImcj9GS3DhRE1MYGKVLmXI2MYHRtqDtfYRr37JEFpoSYyd7%2Bh', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7EKtccZvnwm70iSCGDHrFfUM4%2Fm4S3QV7rl8i3IA0zW3016jSFwBC1rvA%2FWaZ%2BjIupOFINgfC1KqgE3SDbWRmWNZmvXsMQzAqpALj4p1ExDYQwl5y2Pyrq8CAC2gSQVI%2B', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7vhnQCX4qUOEVYcnrpXc4L80VPJRttAZjFCr8PiU%2B9HoZ5x11KiZPydBMbgW68X4r%2BDE8s0Amo%2BtfGVPlKq6svBfDggGB90gxJsIeIg8WG1GQOUzj1i7n7w%3D%3D', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7WC6i9zMNKRlD2kIxUB1RP6%2BRaYG7auEb%2FUGtZOP8qXvz0O3wNx3%2BbSjtHTPI8uAbO%2F4qpnsCa93R1AFOhWWR5DT3MRd6cGQ1FcyV0R7Bozz46LTHtPcy5GLTpxlktE%2Bx', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7j7vvd1%2B%2Bl1kXy81hWDRyrBH8tp28wuWqlbqnlsWXzDiN96hb07Ulf4WBndClY0TV6wG%2B2uJL4EjaaW4MwPCegsTJlX4zcqXgZDk7mxhIJ1VMnjI2z0A5HAv2OTKtGnHV', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7Om8CAnz9DajXbjXFYh4zZtBDM9RCLhV9eeAo7suDF8cC99vvHwia1QljBqOj7ktLPPp3KsY35nP28vpEZExi986XuG2YAS5%2FmMvqdXDhszJK2qpSriQi68e9Sn2ckh3i', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw7mq3%2Bh1cloOgRFmifZJobxk88sdq69VefDgwoSdzrNCX%2FL%2F4%2BS4T%2FqnnZHSsH2SkWSvKlG%2BWkF7h%2FMOFmynl5rwWiPDR%2BbUz%2BDKB7DDfVyLqTSu58%2FJyLAfeHxv2emvPO', 'j9u6WhbqWmjihRIU7uKDebVafzOEiZw73lO%2BtWzU%2FYDmQp53elmrRKhJcy8XgIz8NOG53%2BBXQdZsfyYPUlRVqMzBQfV67tY3mFPP9ztaW3m1YPAUSefn81Y4zxxuiTdEzLY%2FoDA7f%2Bsndce4lM9lXEltdhPVtH5i'], ['%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPC5MRVuLmhuk59kbItjZaGpUU4%2F4DU9YOZkZp3mutVjD%2BS0taYozo7arL%2B4k0Ggbl4G9t88Y0FELL0mXWRXEMr5vJKSc2DwLYi%2F80nAsEDMmVSZ8WBTn%2F%2Bzd6R3%2Bw1rnW', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaP4HQ17qpj3Ppcs4hkT%2Bxi02IH9UEy1HFmEzZFmhOu9KoHV7IuaXFI2f7wpb2uM4VZr2nTgpRiarpXiFl1v0l6cVc%2BHluGh1ga8nqILkyudx9WYDd8vr3er3NR6S5vfZoR', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPt4uNyvMF8pJvep0m73FlZZYTbsaxkJerZxm1H4fUxhKkqaS4gNLMoxWPawHiU6nb1ZZWipxzec8oh9cBIPb7xjLDvaju%2FdBok1nfU9zWLl0RlaQ97MJmkA%3D%3D', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPYzTvuIheZ%2FHcEndOiKrLRaK0SASFZ5%2FFbJByVdm4UDY0HZUqGYSXx%2FcbqfvN0nAiT%2BvKFqiRtGsxDI%2BjqVFONwgok%2BIOgmd3a5QpG1XKf50O4%2Fb%2F09n7XRWiZOHSow8y', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPDi0E3oY5lZtzHo8zSdU1MxXoPdcoawgrcx47Dpa%2Bs8hiZrbeGc60z26elEftaBbEbsldp3V6YOkthumozYyvdBud6dsR8JMIopMlVxF2639PA12RMc3nEETNCZnD%2FaIk', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaP0ndwwxyQ1tVPyfLTkbfVu8JwkvbK2abxKYRTyjbD2pFlAJCxz2LAzRAstyfYIDYUpGtfnBhzREDYh3a7RkSBz9Q2iarKaf4LLQ7XG8wBRSbUxPuv5abA7A%3D%3D', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaP1clhzv%2BgzPLblYd%2BAr243oTTJXHgV6EdM9C7XSPjsGy2sDe%2BX4d%2B91i3lCqVBXcfFWX0NU1EFntCB3%2BjlrwEWvF0EtaKO%2FGG6%2Bl6PyGQBiD%2BWGEbbeyzxg%3D%3D', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPYH%2FU8%2BfATm3KJrn7KJXvMPgKHFf7X0iUzY5W1W%2FUhtM1NqnSJkh%2BrksWYRYCsKgMYsqkpHBoJK7kxpn0SqeA%2BTidWRUMOdx1usmODbsIh0ZtR8uMuoTpk9igxpLnjy1N', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPgklsKsF5Ml2nZh9YwkPeJvNGBPe%2FOxkD3GVk6ZdcnHMb08GKKabXj2Qi0TdFvPg38la%2Fxhk5pd7GKGw0gIU%2Bg5n6ERG1C%2FWB0vSb7T06sUhqRtHc2OAzHA%3D%3D', '%2BnhTa0FAiqfvBE7cmp3hCL175n2ZqNaPNw31IG9Vyqg0GOQmi9UCu9Uc2l9swCGfec6HQ1wYyK7de6zfT7xaMWM1R1XKv9Icy4P4rKlqRhSgz4p0tLyZbd2LrDx8UoyiksKPRPOcWWd3KAH%2BRfaeFQ%3D%3D']]

print(len(id_list_ex[3]))
# soup = BeautifulSoup(open("example_offer_listing.html"), "lxml")
# offering_ids = soup.find_all('input', attrs={'name':'offeringID.1', 'type':'hidden'})
# offer_id_list = []
#
# for offer in offering_ids:
#     offer_id = offer['value']
#     offer_id_list.append(offer_id)
#     print(offer_id_list)




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