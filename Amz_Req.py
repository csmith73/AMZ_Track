import requests

s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
r = requests.get("https://www.amazon.com", headers=headers, verify=False)
print(r.cookies)
res = requests.get("https://www.amazon.com/gp/aws/cart/add.html?OfferListingId.2=qqnFQsQW4%252BI30uAuPphatrcLH5gmjJ%252F3Vh45wHUbfdwshjDeGh7QDnmVdGnnqc73Oj5B0yEW1fTaqqos73dIsVpOn0gdnpSv77DOEzkivkycSjvJJRsh07fRHuphrmGIkGFH8Q4jkU8iYsSj3yK9umhmzQOWPqLm&Quantity.2=995&OfferListingId.5=cMLz0vweCd0CbAek8s%252Fx8i2%252B0fqs%252Bp2aYEcdR2xhc1bLhkpXpMU%252ByAtLv6FON0rYJxGNcO1qF73BxVsljj7NOzzbygexKJ8luSGTWf%252FOPeYNbFk5a0z%252Bf6GZfIa17jS4k%252BV9zIVgXPNSW43AVYnAVQ%253D%253D&Quantity.5=995&ASIN.4=B0002ZP3ZA&Quantity.4=995&AssociateTag=your%252Dtag%252Dhere%252D20&Quantity.1=995&Quantity.3=995&SessionId=131-9739670-2998723&confirmPage=confirm&add.x=50&add.y=10", headers=headers, verify=False)
print(res.text)