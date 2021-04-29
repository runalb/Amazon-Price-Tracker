from bs4 import BeautifulSoup
import requests
#import lxml

def get_product_price(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    req = requests.get(url, headers = headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    price_tag = soup.find('span', id ='priceblock_ourprice')
    if price_tag is None:
        price_tag = soup.find('span', id ='priceblock_dealprice')


    #print((price_tag.text))
    price_str = price_tag.text.strip()
    #print(price_str)

    price_str = price_str.replace(",", "").replace("₹", "").strip()

    price = float(price_str)

    return price


def check_product_price_with_your_price(p_product,p_your):
    if p_product < p_your:
        print("Less")
    elif p_product <= p_your:
        print("same")
    else:
        print("high")




your_price = 13499
url = "https://www.amazon.in/Amazfit-AMOLED-Display-Monitor-Bluetooth-Storage/dp/B08XW3TKYR/ref=sr_1_2"

product_price = get_product_price(url)

check_product_price_with_your_price(product_price,your_price)



