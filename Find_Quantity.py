from selenium import webdriver
import time
import random
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
import sshtunnel
import MySQLdb

server = sshtunnel.SSHTunnelForwarder(
            ('206.189.190.150', 22),
            ssh_username= 'root',
            ssh_password= 'Summer201889$',
            remote_bind_address=('127.0.0.1', 3306))

server.start()
print(server.local_bind_port)

conn = MySQLdb.connect(host="127.0.0.1",port=server.local_bind_port,user="root",passwd="Summer201889$",db="amz_track", charset='utf8')
x = conn.cursor()


amazon_link = 'https://www.amazon.com/Tinkering-Labs-Electric-Engineering-Experiments/dp/B01M5GJFQ1/ref=sr_1_11_sspa?ie=UTF8&qid=1549245703&sr=8-11-spons&keywords=robot+kit&psc=1#HLCXComparisonWidget_feature_div'
asin = 'B00KSMBL26'
#B0000A1ZN1
offer_id_list_ex = [['qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdLqvsWlBaTJxy5fElMIdS3EDdFnPZMI737XFPDc%2Bp2OZgHt%2FC%2F9ifnqGpvCLn9Obi2%2BstUrjhjCI%3D', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdhWfJVJcy5SLIZsALaNHp5fcshR2IhutpSPhRWvBQsVGHYsQrqDT8Nf1yyVqdkZVHNOrfcIxeYaD6EIgi%2Fh518Rq21iHjVlFMwaN5fWQs19Sf60%2BwjLGYYpM%2BVY3SU2a9', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdaKCwXesmXZDSOSv3J%2BsOxDVnS5q4f0HPgsSX%2FhF4siRvUpo%2FC7emr9te1961Pn4OoLCUafC2TC2REvowzjLWn8wiXyOo5AXJthWcIxbh%2BcjuxKsU1jBnif%2BIoIdHuGxJ', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdV0c60ksBZUjhMUt%2Ftbnhi%2F6VOZpMUi11usJi0UN8UIjKgMYy1qNaZTSjk9CI6eWrFv%2FDdYJt%2F%2BmjDoDYj7z6eDBDZBW%2B%2FBNMH3V4z9qeNlBQ%2F0SjBDPwthqUGUpBIWFP', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUd9n8223kBbqanDP7FH0QvWpY%2FT0gGJZZDk5zV0MEPMKIV2b3e0BvCv40FJ7nBaqVELFlOKpOYzfqWhbbaezYyDnDsKjgDeHFbk6um0CoSfiPDT8YKSC3ZYQ%3D%3D', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdJ7zF7MlyicD%2FXMx6v5eBXTgSVRjsBeEw5j%2FOpeurmcXOHkw8Rf9NP5hbBnC9PBny2hAWpsCWPLkRTBxM8SH1GJL4aRK2mK607b1oa66A5DQnZYDV8dMUXooPO6V0Kb0F', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdm0s1VvJvkBU6PNQk2cIZ5xFKjWS0o%2BcSk9MgrG%2BtuAGWPVmyJGjBtsqKKTQ9TZ8xrGvBdNSNyJ2NdF53ljIht8zus3OKSoC0cqWEOzBkSJVO0k7oqnjOkQ%3D%3D', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdgxk3B037zypVl0SiOXfz5IoFloUMaG00FM8cowvgfJoNT9jzQe%2BxvIYmVofCzrFcfj4MZXal48LnAQ71eBY2xP09On%2BP7%2Fb1CvBiaQbU%2BcauH8X07vXEvo7Ws%2FJgZ0eX', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUdbEHxqrBAEqfqabp1knDgFZQunFu1NLYiPXTwkgl2zmvPlGkRgi3CWvB5ilewnTJn7SamhjQ46qcsCZz1gVOc7rA6YevLLuEo1YK9E1UfBMLbIKDOzm4PiUTFlGNLoFXH', 'qqclpLJ9La3%2BX03SNZ4BuG%2BFF3%2FGZEUd80RVwCCoIP8fcZVrvKb7%2BNgcNpHyGJI9aPuetp%2BifcmOL4DcaH7yFVOMb1kR9gFBgQTKe46q19m0mb5AiJTnj9BlxKEovO729gnwsvQ3GniNDQj0Om8PdF9Tsf1upE4N', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSNn9ERGIwWcAiClMzRHwYf5EfOQWOIHtaAVyxnkWSpZ5YOi2uPo50QKM2mEON3qT5Ux3CIpQXNz0Js4ZmU4h7Pk%2B%2FWY2i24fn8863DE8WAckpmGhVaZgarp6b1zDcMeTB', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSu0t48VTNcPaIIbHBfjXAkng4bpBGnkTvSKpI0wQE3W4ngthKeYDVlY6C08Om2%2BSrtLOyQePBbYX58f57GBy2jy%2FifM8Rkf391z%2BgEz3rDbe1zU%2B4YvyBpw%3D%3D', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSSKjzhkXBDxEWzsolKvW8RSBnPDhMhROMOUpz1Px7pyxy1CD%2Flz7uzM1eZb0YkLS2yCw2q6G3f6tKbwVtyVBcaRY%2BelxOS40d52hG4cdZEh9VMQd5xXPReEm3blOLSmw1', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSqG9P1zmZNSfYuN8KKF%2FYlVh2UrjWt9Q%2Fc91eUjYP0GgoFM8hOZJ0zvYIfVO5Gi2aWJOhxNqvr07VSAHARHznSYyIyml36ceVkj722H5BNuvQRbD%2Fqi5vuMcYidcatubG', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uS7hGJ8zcIsxBo0WQ%2B%2F9VkTlPXEVTitIqokhM%2F3k%2FbIMcV28hJnWKKMEK6LDVRAgi7MWz8xfVi9QkZIY7gaNNZLuLaMTuzwuAOFcnQmuOHs2ZewT7po93yNo09qcdNEQnx', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uStBusK4CVOZGfdpGNNnqbXxjIFjmFgI3OfaIResI2xznxUiqfQnm1zQzACFbEJ2DoVE%2B5WXo0d0BC8TQD%2Fu1kI8ZunOs%2FCgM3BKpHRF33F4PlaaFIOHAdWTI8kS0YtSob', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSVS8quOil4Fhtwwp9ytKoOh2%2Bjw9f5iyeie6M%2FT5NR%2FUN%2BvBSFztbR1Rf9bnHnXJInJwalvA1LGbsgzsHr55UfyTUcR03XPvrCwQvlJSIo90J797jE3hXTWLKjI0rFEYe', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSb%2FrC%2BPytFhLNn7Pgpj6DM16ORGGT7cIPHjNaxckl7PaSwsw70jOCI3YeEhaHMPUyMAHpmduJXssxiyKrHNNzF%2Ftza%2BjFoROwxN3xFwIYkaJBcTGged5wyg%3D%3D', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uSYiX2AHgHSKyL2xHA2P1pKWB63qt15dpStLeiWr52USR0Rv7JW5gCLtoHA7z3YhlYIDh7UpcbYqfpST9o4UGm%2FCcYwX%2Far53OkbMd%2FoGgf%2FJQ15TXHzYp%2F0QmClOMW2ii', '8oOmeCpaohryPX8zVEw8C1I8FJhsc5uS6J33aR8C1jZxBeVJcdXzLuVZdGXLA15zsllziHTYAeSDq4xLIsebsSclizUGrTYH7AGLpMSQkxhwTp4giFM6k3sc%2B6XWsWWlzu1ppPeiT%2FDewMu8oaat%2FA%3D%3D', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzH%2Brn8y9DTL9HTKpO8U8ERz8RkiVAS%2BfxIR2YMx7iB1pug35sGVsEG7U9L6fx6XbvfTPankr49%2BfTmLYad9cOCfOKPqy1CAcyYsiI9L40eDqVRLKeUdyqKaZBrkhYHYVv', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzklxDGmJoTr6hkiWNyLR2b7c9a2FA2FbYZdMuWNhBbui%2Fwr5uu4MAs66U6XjkgTfKSRaiT74OJQpWE4L5SK1H3uQgvdmYY7hzGGN56l9e2vhP2A1P%2FcpiGzUQxhiteixJ', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzHO4TGfYIC7UDheFah8MO0QGfQv4XruJ3JD2PO6TProJ6E2%2F0vtQWu%2FMlSmpqkA6ZJvaaY2qRv2Obn%2BbB8PuMDMdVBrFe3IABIURJRZR9pzBhFpsCp0ZWaw%3D%3D', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDztGs8Mnn9Dm%2FcIH8rFT8fVTSOs3BlaU5RWtL8pT4w%2F4g4Deaik4wb1LOcvI7DcOX1%2BIJt3V4hnO%2B2xEzUuNGRyZEiIxdTh3YBHRTeuTI1ajV1jjGsZ5Fgg9lEwCFl0RNe', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzjEHmj2z4cKrlZA0mmUTmyu1dyv7bXt41YlwejZnPRotC3B1ilmiOQbHr%2B1Nqs%2FPXT%2F41D2OarKNkq8DIlQvcG4fC8dxZl%2BqC1Y0SPsu1y382F1%2Fe4UY2W5XXoPPYCABe', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzcubbSL0UOouhT63a24Dk3NQtnFnfUXYgAOd5y%2B%2BRc4XDkN1xD6TZcw5AWV49GZZj0Ei0zeGaHP73JZ5gys7SmUhSbhcxH%2FhHj9DbVeVh9DCuqjJ5quPxwg%3D%3D', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzKefc8nsmfQ7U1UG2o%2F8S8oXqAAVygqdYaW64VSkgw5hCxQkhB3d72taRXOt7gKyUlyIUFR1LOMj%2BZ%2BbBAQVqz%2F9FRPDTstIBWxdhioj0Sk9yRJuMGQs0lohdHQM8keTu', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzwLuWXuNkQlaT9utBA6eyOG4%2FiF6U4wlf7yl0RILsP3WZyfbf6TfKOTv%2BFI5f%2B6docIDWZUMYJ4BVasEMLH8liV58RzPc3McEGGnEbnOtaRnc2QeTOFTGopNIbzWduQPM', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDz%2B2mZTznuI5FBbCriyh%2F222SZ7VGVBZntz0OKHQKvVGTfqGB3f0Rnt9IzjBr%2FIUjWIC5wcNbxwn%2Fji%2BwsBNSV6Ha77sTm9mVrJJV8%2F51Z5zq%2B9YsZzpWjN%2B6KgFU3hjVC', 'Ul15ng%2F18dBRMueJMKwgg10D3jgkQaDzOel0RiOY42olLcRDdj4S8uq%2BP9Z8iMWgMpH3upCgbEU6Cs9Q%2Fcbn8wP2BtqyspzX78XDfLQMgp4D5U5zJ%2FEQACvp6i%2FIwIUoeOkcCWsY%2BUDhOq9bOIQXgWuXdndT1iTM', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanOpB9NlxVgwmaIJvA73Cx91pYC8ZYHK01HPLI1mFDcNJLyfjH983LiYB8U1YQ8WbLZLJEOCsSQN6hJBU2NFpNm8BgGn%2BTQYGwwYePYH7ABEiouJLiSKyIyXtoxBd9K62tq', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanOhIYAvmwCFE3bnjYBEgQN7wRCHU4IDI8vbWs1LOUbJkKkM66BcSuoQmZH2qkIQwnrjv76Jbs1TcfZky97ERhwstKnjcWPGO0nDWgh8etrI1OYX34hzBreY2Izz9zScRRb', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanOuJ0VLK6bcuoVyb71jfMVK%2BQohiE9zBNH5ZwcSb78HKzhr9TX2YcaoUdSNfBhSeSeKs3rTnSHnTKXvTfdH0XR3aTlOkEgno37jRodP9xrTVZ%2FKARSv%2B9Y9Q%3D%3D', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanOoDaLNtWKagaKOwbydZWmhb%2BlsC3p%2BtFJKpng2KitfdBwI%2BoIweexcRnNtqsKLZqtfwXTdehU1cqjwoa0X0uq%2BMKq7wrnE6kvHTa1Qf9ndaXyrKwXXD1y%2Fg%3D%3D', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanOPGKzU5bN1wueCsW4AV0%2BsRJcjimQR88QxGP9fPQzGF3r%2FPwYO4GTO46vgETuJpM8eGsluFxwNUeqBY%2B3jeH0XlODTWwh8lvpetoMwg3W%2FupwfZ6TWUtVHqgRIdTzAS8w', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanO6c18sJ8Qe69M1tnelmBtXzBNlMFEOSAKHXMvd7%2BtwZPtxM%2BfX0LCiGGQ2a3immd%2F4z16hqe2rz3XY%2BUUG2sZTfIYIQK5x4jujm7p%2FufGT90HsuND6A6cxEbZvSkVKt%2Bi', 'HY0uDUrz0iLDU4G8PJ2ZdU%2FJo0BtHanOYLPCgIV7Ko7Rxt367h3Ta7Z7A%2FiDg%2FsbdOr%2BHJt0dzIlBK7qUx%2BSm8xZdu3Wu20STAWJ19OWypZQfMeUKJkZN70Eyq5ZzO7foY2kG5AhwWtp8ozUrj0ciKplrn6T1iij'], 4, {'Amazon.com': 'ATVPDKIKX0DER', 'MichaelVictoriosus': 'A18FV179QADRTL', 'SpaceBound': 'A1XBPHGHAXLHDG', 'Bargain Ben': 'A30Y99I01TOXRG', 'Gourmet Kitchen Gallery': 'A2HITL9SNBEQ85', 'Electronic Express': 'ASH1H6YCFH4EF', 'TheFactoryDepot': 'A29PHU0KPCGV8S', "Ryan's Store 2": 'A31KX9BMDPQ3ZM', 'Deals Depot LLC': 'A1E9DLI8FU0IMK', 'DigitalShopper': 'A1NAVOX3XE5VZM', 'Kitchen Connection': 'A3L8686AKXMRUN', 'FastMarketPro': 'A14NA3XYNZWQC5', 'Life and Home': 'A1SV1BYDTUK2Z5', 'Greatest Bargains': 'A2FM6E40NLWDBY', 'Kitchen Kapers': 'AIIPVFX3AG363', 'Limolin LLC': 'A24JJ3ISG1I3Q2', 'PROSPERNIA': 'A1PGC38WMXZGT6', 'toolboxsupply': 'A281ICWJBRZ31L', 'Master Suppliers': 'A32JIJVD18NA57', 'IPC-Store  ✅': 'A284PRV19Y1MTF', 'Supply Cart': 'A1TWFV9331WNG0', "Golda's Kitchen Canada": 'A13HTXU7N5QMMA', 'OneCall': 'AHF4SYKP09WBH', 'Champion Values': 'A1HGNMNEKOYPYQ', 'HalfandHalf': 'A29UJOT1B8RZFR', "Ron's Home and Hardware": 'A27BUQSY3E84IP', 'Factory Hardware Store': 'A3EQJ16CEAAUOF', 'Beyond Home Improvement': 'A2BFL7LRZPRRNF', 'iguaranteeit': 'A3GVG1BNCINM2L', 'QUICK ONLINE': 'A1BBEKKND9EC89', 'Happy Happy Shops': 'A1RUAQ7C085JZ3', 'Online Supply Center': 'A2C4EMWO80SHUW', 'Aim To Find': 'A5RB321HREH64', 'superior sales': 'ADJ3LLQFDHE8C', 'T̲H̲D̲': 'AV7NPUQ79O1X0', '3ELM': 'A4V0ATM4SIKP4', 'GoodBerries': 'ADSP4MFXAL04G'}]
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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(
         '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
    driver = webdriver.Chrome(executable_path='/dev/chromedriver', chrome_options=chrome_options,
                               service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    #driver = webdriver.Chrome()
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
    seller_name_id_dict = {}
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
            single_page_offer_id_return = get_offerids_on_single_page(page_source)
            single_page_offer_id_list = single_page_offer_id_return[0]
            single_page_dict = single_page_offer_id_return[1]
            seller_name_id_dict = {**seller_name_id_dict,**single_page_dict}
            offer_id_list = offer_id_list + single_page_offer_id_list
            time.sleep(rand)
            print(offer_id_list)
    else:
        total_pages = 1
        offer_listing_url = 'https://www.amazon.com/gp/offer-listing/' + asin + '/ref=dp_olp_all_mbc?ie=UTF8&condition=all'
        driver.get(offer_listing_url)
        page_source = driver.page_source
        single_page_offer_id_return = get_offerids_on_single_page(page_source)
        single_page_offer_id_list = single_page_offer_id_return[0]
        single_page_dict = single_page_offer_id_return[1]
        seller_name_id_dict = {**seller_name_id_dict, **single_page_dict}
        offer_id_list = offer_id_list + single_page_offer_id_list
        time.sleep(rand)
        print(offer_id_list)
    driver.close()
    return [offer_id_list,total_pages,seller_name_id_dict,asin]


def get_offerids_on_single_page(page_source):
    soup = BeautifulSoup(page_source)
    offering_ids = soup.find_all('input', attrs={'name': 'offeringID.1', 'type': 'hidden'})
    offer_id_list = []

    for offer in offering_ids:
        offer_id = offer['value']
        offer_id_list.append(offer_id)
        #print(offer_id_list)

    sellers = soup.findAll(True, {'class': 'olpSellerName'})
    seller_names_list = []
    seller_id_list = []
    for seller in sellers:
        print(seller)

        img = seller.find_all('img')

        if len(img) == 1:
            seller_name = img[0]['alt']
            print(seller_name)
            seller_names_list.append(seller_name)
            if seller_name == 'Amazon.com':
                seller_id = 'ATVPDKIKX0DER'
            if seller_name == 'Amazon Warehouse':
                seller_id = 'A2L77EE7U53NWQ'
            seller_id_list.append(seller_id)
        else:
            seller_name = seller.findAll('a')
            seller_name = seller_name[0].string
            seller_names_list.append(seller_name)

            seller_id = seller.findAll('a')[0]['href']
            seller_id = seller_id.split('seller=', 1)[1]
            seller_id = seller_id.strip()
            seller_id_list.append(seller_id)
            print(seller_id)

    print(seller_names_list)
    seller_names_id_dict = dict(zip(seller_names_list, seller_id_list))
    print(seller_names_id_dict)


    return [offer_id_list,seller_names_id_dict]

def get_cart_url(offer_id_list):
    print('Offer id list')
    print(offer_id_list)
    cart_url = 'https://www.amazon.com/gp/aws/cart/add.html?'
    i = 0
    for offer in offer_id_list:
        print(offer)
        i = i+1
        cart_url = cart_url + 'OfferListingId.' + str(i) + '=' + offer + '&Quantity.' + str(i) + '=10&'
        print(cart_url)
    return cart_url




def scan_cart(asin,seller_names_id, cart_url):
    print(seller_names_id)
    seller_names_id = inv_map = {v: k for k, v in seller_names_id.items()}
    print(seller_names_id)
    print('........................................................................................')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(
         '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
    driver = webdriver.Chrome(executable_path='/dev/chromedriver', chrome_options=chrome_options,
                               service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome()
    start_time = datetime.now()

    rand = random.random() + .4

    driver.get(cart_url)
    time.sleep(rand)
    driver.find_element_by_name('add').click()
    time.sleep(rand)

    for back_count in list(range(0,2)):
         driver.execute_script("window.history.go(-1)")
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

    sellers = soup.findAll(True, {'class': 'sc-list-item'})
    print(len(sellers))
    seller_id_list = []
    for seller in sellers:
        #print(seller)
        seller_id = seller.findAll('a')[0]['href']
        seller_id = seller_id.split('mid=', 1)[1]
        seller_id = seller_id.split('&', 1)[0]
        seller_id = seller_id.strip()
        seller_id_list.append(seller_id)
        #print(seller_id)


    print(len(seller_names_id))
    print(len(seller_id_list))
    seller_names = []
    for id in seller_id_list:
        seller_name = seller_names_id[id]
        seller_names.append(seller_name)
    print(seller_names)

    data_offering_qty_dict = dict(zip(seller_names, qty_list))

    for seller in seller_names:
        inventory = data_offering_qty_dict[seller]
        date = datetime.now()
        print(date)
        print('Inventory')
        print(inventory)
        print('Seller Name:')
        print(seller.encode('ascii','ignore'))
        seller = seller.encode('ascii','ignore')
        x.execute("INSERT INTO productinventory (asin,seller,date,inventory) VALUES (%s,%s,%s,%s)",(asin, seller, date, inventory))
        conn.commit()

    #conn.close()
    driver.close()
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

asin_state = ['B07BM9LHRB','B00MV017AO','B01FIML2KQ',]
#asin_state = ['B007D3V00Q']
seller_names_id_list_state = {'Amazon Warehouse': 'A2L77EE7U53NWQ', 'DI ORO': 'A8ZXRV4PB0V5P', 'GetShredded': 'A36UDZCMGW1FH9'}
cart_url_state = 'https://www.amazon.com/gp/aws/cart/add.html?OfferListingId.1=5BpQx7NU41Cs2FjDms%252B8cIH9ZYCZNEgOI6O8%252BI4f4XKMBv8xXCubgyD3qiAd4oXQHKngpQh%252FtIv0cf%252B5nmfG2v7OCjDPnPXOvJ46vEETdz1M9lsGNO7Q0gmS1yqNfsmsbbap%252Fm6FnGBeWFUub7xU1MGpWsd9s5%252Bq&Quantity.1=10&OfferListingId.2=cyX223n31C%252BbkTIUDhPpJ6uNvwrIkq7stAPnofAKYaq1FiDiDJGIaggNecy9vBP9YnDiKluFb2IALIDR95%252BBqmgMQuWEg9%252B85O31%252FiLGg7BYBHG5d9jJkS%252Fsu31JSNCJuwteCBpBdXODT3F5CZIcDLw4P0WbarUA&Quantity.2=10&OfferListingId.3=aAezmqnLz8IyO%252B5ZK9uQUozy%252BNsyD1z150Z744bSFYopKz%252BcyYgnRrdnvhhpK%252FCTrTs13oa2OG40v%252FrSKi8UCbCdJ4p7bUO2GxdPI5GzIPyISfq02AIQmuGCWK49BdDziClGZam1AgY%252BTjnz6eedmyrgTiOyRLd8&Quantity.3=10&SessionId=135-5321892-6026264&confirmPage=confirm&add.x=47&add.y=11'

for cur_asin in asin_state:
    offer_id_list_test = get_offer_id_list(cur_asin)
    cart_url_test = get_cart_url(offer_id_list_test[0])
    print('Offeridlist 3....................................................')
    print(offer_id_list_test[3])
    print('Offeridlist 2....................................................')
    print(offer_id_list_test[2])
    iventory_test = scan_cart(offer_id_list_test[3],offer_id_list_test[2],cart_url_test)
    #iventory_test = scan_cart(asin_state,seller_names_id_list_state,cart_url_state)
    #cur_stock_test = get_current_stock(one_page_cart_url)

    #print('Final ASIN')
    #print(asin_test)
    #print('Final offer_id_list_test')
    #print(offer_id_list_test)


    print(iventory_test)

print('Server Stopped.........................')
server.stop();