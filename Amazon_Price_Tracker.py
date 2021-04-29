from bs4 import BeautifulSoup
import requests
import smtplib
import time


def get_product_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    req = requests.get(url, headers=headers)
    global soup
    soup = BeautifulSoup(req.content, 'html.parser')



def get_product_name():
    product_name_tag = soup.find("span", class_="product-title-word-break")
    name = product_name_tag.text.strip()
    return name



def get_product_price():
    price_tag = soup.find('span', id ='priceblock_ourprice')
    if price_tag is None:
        price_tag = soup.find('span', id ='priceblock_dealprice')


    #print((price_tag.text))
    price_str = price_tag.text.strip()
    #print(price_str)

    price_str = price_str.replace(",", "").replace("₹", "").strip()

    price = float(price_str)

    return price




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_email_password)

    #-------- WOrk on mail content------

    subject = 'Amazon-Price-Tracker: Price Fell Down!'
    #body reaming
    body = "Price Fell Down!\n\nYour amazon product link:\n\n {}".format(url)

    msg = f"Subject: {subject}\n\n{body}"



    server.sendmail(sender_email,receiver_email,msg)
    print("Email send")

    server.quit()




def check_product_price_with_your_price(product_p,your_p):
    if product_p < your_p:
        print("Less")
        #send_mail()
    elif product_p <= your_p:
        print("same")
    else:
        print("high")






your_price = 14499
url = "https://www.amazon.in/Amazfit-AMOLED-Display-Monitor-Bluetooth-Storage/dp/B08XW3TKYR/ref=sr_1_2"

'''
sender_email =
sender_email_password =
receiver_email =
'''


while(True):
    get_product_page(url)

    product_name = get_product_name()
    #print(product_name)

    product_price = get_product_price()

    check_product_price_with_your_price(product_price,your_price)


    time.sleep(50000)


