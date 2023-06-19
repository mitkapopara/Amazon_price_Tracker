import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                               "like Gecko) Chrome/114.0.0.0 Safari/537.36",
                                 "Accept-Language": "en-US,en;q=0.5"})
product_web_page = response.text

soup = BeautifulSoup(product_web_page, 'lxml')
product_price = float(soup.find(name="span", class_="a-price-whole").getText())


if product_price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"The price of the product is ${product_price}"
        )
