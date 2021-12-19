import re
import time
from bs4 import BeautifulSoup
import requests

URL = "https://www.target.com/p/google-pixel-6-5g-unlocked-128gb/-/A-84683612"
# URL = "https://www.target.com/p/motorola-moto-g-power-2021-unlocked-64gb-gray/-/A-82058238"


def get_page_html(URL):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(URL, headers=headers)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    print(soup.prettify())
    #out_of_stock_divs = soup.find_all("div", {"class": "button-descriptor-container"})
    f = soup.find_all(text="This item isn't available")
    # print(f)
    #print(out_of_stock_divs)
    #return len(out_of_stock_divs) != 0


def check_inventory():
    page_html = get_page_html(URL)
    # print(page_html)
    if check_item_in_stock(page_html):
        print("Item is in stock!")
    else:
        print("Item is out of stock!")


while True:
    check_inventory()
    time.sleep(10)

