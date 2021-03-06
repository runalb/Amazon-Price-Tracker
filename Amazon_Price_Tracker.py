from bs4 import BeautifulSoup
import requests
import smtplib
import time

class Product():

    __sender_email = ""
    __sender_email_password = ""

    __headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


    def __init__(self,url,your_price,email_send_to):
        self.url = url
        self.your_price = your_price
        self.email_send_to = email_send_to



    def get_product_page(self):
        self.req = requests.get(self.url, headers=Product.__headers)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')



    def get_product_name(self):
        self.product_name_tag = self.soup.find("span", class_="product-title-word-break")
        self.name = self.product_name_tag.text.strip()
        return self.name



    def get_product_price(self):
        self.price_tag = self.soup.find('span', id ='priceblock_ourprice')
        if self.price_tag is None:
            self.price_tag = self.soup.find('span', id ='priceblock_dealprice')

        self.price_str = self.price_tag.text.strip()
        self.price_str = self.price_str.replace(",", "").replace("₹", "").strip()
        self.price = float(self.price_str)
        return self.price



    def check_product_price_with_your_price(self):

        if self.price < self.your_price:
            print("****")
            print("Current Price: {} - Less than your price: {}".format(self.price,self.your_price))
            self.send_mail()
            print("****")

        elif self.price <= self.your_price:
            print("Current Price: {} - Same as your price: {}".format(self.price,self.your_price))
        else:
            print("Current Price: {} - Higher than your price: {}".format(self.price,self.your_price))



    def send_mail(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.ehlo()
        self.server.login(Product.__sender_email, Product.__sender_email_password)

        self.subject = 'Amazon-Price-Tracker: Price Fell Down For Your Product!'

        self.body = '''Price Fell Down For Your Product!
        \n\nProduct Name:
        {}
        \n\nCurrent Price:  {}
        \n\nBuy link:
        {}
            
        \n\nDeveloper - Runal Banarse (https://runalb.com) \n\nThis email was automatically generated by \nAmazon-Price-Tracker created by Runal Banarse
        '''.format(self.name.encode(), self.price, self.url)

        self.msg = f"Subject: {self.subject}\n\n{self.body}"

        self.server.sendmail(Product.__sender_email, self.email_send_to, self.msg)
        print("Email sent to",self.email_send_to)

        self.server.quit()
            


if __name__ == '__main__':

    # object format:
    # obj = Product(url,your_price,email_send_to)

    P1 = Product("https://www.amazon.in/Amazfit-AMOLED-Display-Monitor-Bluetooth-Storage/dp/B08XW3TKYR/",
                 13499,
                 "hello.runalb@gmail.com")

    P2 = Product("https://www.amazon.in/dp/B089MTW733/",
                 54999,
                 "hello.runalb@gmail.com")


    def amazon_price_tracker(*args):
        for product in args:
            try:
                product.get_product_page()
                print(product.get_product_name())
                product.get_product_price()
                product.check_product_price_with_your_price()
                print()
            except:
                continue

    while(True):
        amazon_price_tracker(P1,P2)
        # sec x min x hours
        time.sleep(60 * 60 * 12)  # 12h sleep
