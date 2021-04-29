from bs4 import BeautifulSoup
import requests
import smtplib
import time

class Product():
    def __init__(self,url,your_price,email_send_to):
        self.url = url
        self.your_price = your_price
        #self.email = email
        #self.email_pwd = email_pwd
        self.email_send_to = email_send_to

        #same for all check this later to make common - class variable
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


    def get_product_page(self):
        self.req = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')



    def get_product_name(self):
        self.product_name_tag = self.soup.find("span", class_="product-title-word-break")
        self.name = self.product_name_tag.text.strip()
        return self.name


'''
    def get_product_price():
        price_tag = soup.find('span', id ='priceblock_ourprice')
        if price_tag is None:
            price_tag = soup.find('span', id ='priceblock_dealprice')

        price_str = price_tag.text.strip()
        price_str = price_str.replace(",", "").replace("₹", "").strip()
        price = float(price_str)
        return price


    

    def check_product_price_with_your_price(product_p,your_p):
        if product_p < your_p:
            print("****")
            print("Price: {} - Less than your price: {}".format(product_p,your_p))
            #send_mail()
            print("****")

        elif product_p <= your_p:
            print("Price: {} - Same as your price : {}".format(product_p,your_p))
        else:
            print("Price: {} - Higher than your price : {}".format(product_p,your_p))
            
        



   


'''

sender_email = "ENTER SENDER EMAIL-ID"
sender_email_password = "ENTER SENDER EMAIL-ID PASSWORD"

'''
def
    get_product_page(url)

    product_name = get_product_name()
    product_price = get_product_price()

    check_product_price_with_your_price(product_price,your_price)

    # sec x min x hours
    time.sleep(60 * 60 * 12) #12h sleep


'''

#obj = Product(url,your_price,email_send_to)

obj1 = Product("https://www.amazon.in/Amazfit-AMOLED-Display-Monitor-Bluetooth-Storage/dp/B08XW3TKYR/",
               13499,
               "hello.runalb@gmail.com")



print(obj1.url)
print(obj1.your_price)
print(obj1.email_send_to)

print()

obj1.get_product_page()
print(obj1.get_product_name())