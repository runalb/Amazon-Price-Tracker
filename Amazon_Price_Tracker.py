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

    price_str = price_tag.text.strip()
    price_str = price_str.replace(",", "").replace("₹", "").strip()
    price = float(price_str)
    return price


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login(sender_email, sender_email_password)

    subject = 'Amazon-Price-Tracker: Price Fell Down For Your Product!'

    body = '''Price Fell Down For Your Product!
    \n\nProduct Name:
    {}
    \n\nCurrent Price: {}
    \n\nBuy link:
    {}
    '''.format(product_name.encode(),product_price,url)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(sender_email,receiver_email,msg)
    print("Email send")

    server.quit()


def check_product_price_with_your_price(product_p,your_p):
    if product_p < your_p:
        print("****")
        print("Price: {} - Less than your price: {}".format(product_p,your_p))
        send_mail()
        print("****")

    elif product_p <= your_p:
        print("Price: {} - Same as your price : {}".format(product_p,your_p))
    else:
        print("Price: {} - Higher than your price : {}".format(product_p,your_p))



# ENTER INT NO. HERE
your_price = 14499

url = "ENTER PRODUCT URL"

sender_email = "ENTER SENDER EMAIL-ID"
sender_email_password = "ENTER SENDER EMAIL-ID PASSWORD"
receiver_email = "ENTER RECEIVERS EMAIL-ID"



while(True):
    get_product_page(url)

    product_name = get_product_name()
    product_price = get_product_price()

    check_product_price_with_your_price(product_price,your_price)

    # sec x min x hours
    time.sleep(60 * 60 * 12) #12h sleep


