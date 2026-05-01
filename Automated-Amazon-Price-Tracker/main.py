from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import os
from dotenv import load_dotenv
load_dotenv(".env")
EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
PRESET_PRICE = 110000
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.google.com/",
}
URL = "https://www.amazon.in/Apple-2026-MacBook-Laptop-chip/dp/B0GR1HPR1W/ref=sr_1_1_sspa?crid=1B9CRT3UMCLUZ&dib=eyJ2IjoiMSJ9.1jqmVqNoougeOurrua4slyeRI2GaOvN9bH0ORK5s99TDs9eVMUdo5mpDxrdLlW5z_QVGwvLI3UzNdu2Uy1g1xcx7QwZ2bSYepKPze-0jybGWvo6GUlJBCtmkIlLdl8Kp7f3OJ3h9mxQ3MFCDtiDPnsY8uTnpGVWZVi7XjOTzxN2G5KkD-zVzr2K_VZID89oT9cSMVJnGwMvtwHyenlxwBlnxUKEaF8qz_m3IuEdMU-I.F7lNNdV7yBwb3h4nx6Yehkx3TRVE1pwDA6WVZs0dU34&dib_tag=se&keywords=macbook&qid=1777272708&sprefix=macbook+ne%2Caps%2C408&sr=8-1-spons&aref=uknu7BMM8z&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
response = requests.get(url=URL,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
price_str = "".join(soup.find(name="span", class_="a-price-whole").getText().split(","))
price = eval(price_str)

if price < PRESET_PRICE:
    with SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                  to_addrs="itsakhilk@gmail.com",
                  from_addr=EMAIL,
                  msg=f"SUBJECT: Amazon-Price-Tracker\n\nProduct: MacBook AIR M5: {URL}\n PRICE: {price}."
            )
    print("Mail sent Successfully.")
else:
    print(f"Current Price: {price}\n")