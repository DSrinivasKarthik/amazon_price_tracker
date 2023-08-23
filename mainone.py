import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import csv
import time
import datetime
import os
import re
from datetime import datetime
import pandas as pd 
import graph_work
now = datetime.now()

def get_converted_price(price):
    converted_price = float(re.sub(r"[^\d.]", "", price))
    
    return converted_price


def extract_url(url):

    if url.find("www.amazon.in") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.in" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.in" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url


def get_product_details(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    details = {"name": "", "price": 0, "deal": True, "url": ""}
    _url = extract_url(url)
    if _url is None:
        details = None
    else:
        page = requests.get(_url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = get_converted_price(price.get_text())
            details["url"] = _url
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y")
            details["date"]=dt_string
        else:
            details = None
    return details

def send_email(email):
    msg = EmailMessage()
    msg.set_content("Your product :"+L[0] +" is now available at "+ str(L[1])+ "\n"+"Go and order now at "+z)

    msg['Subject'] = "Hey! The prices are affordable"
    msg['From'] = "srinivaskarthikdsk@gmail.com"
    msg['To'] = email
    #"achalbharadwaj038@gmail.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("srinivaskarthikdsk@gmail.com","SrinivasKarthikDSK123$")
    server.send_message(msg)
    print("email sent")
    server.quit()
def work(email):
    global z
    global L
    global file_name
    global linkz
    linkz=[]
    file_exists = True

    choice1=input("Do u want to add a new link?(y/n):")
    if choice1=='y':
        z=input("Enter URL:")
        budget=int(input("Enter your budget:"))

        a=get_product_details(z)
        print(a)
        c=a['name'].split()
        file_name=''
        for i in c:
            if i[0] in ['|','(',')']:
                pass
            else:
                file_name+=i[0]
        
        print(file_name)
        if not os.path.exists("./"+file_name):
            file_exists = False
        with open(file_name,"a") as file:
            writer = csv.writer(file,lineterminator ="\n")
            fields = ["Name","price","Deal","url","Timestamp"]
            
            if not file_exists:
                writer.writerow(fields)

            timestamp = now.strftime("%d-%m-%Y")
            L=list(a.values())
            writer.writerow([L[0],L[1],L[2],L[3],L[4]])
            print("wrote csv data")
        choice=input("Do you want to see the graph of rate change?(y/n)")
        if choice=='y':
            graph_work.graph(file_name)
        else:
            pass
        
    else:
        z="https://www.amazon.in/dp/B08HV83HL3"
        budget=int(input("Enter your budget:"))
        a=get_product_details(z)
        print(a)
        choice=input("Do you want to see the graph of rate change?(y/n)")
        if choice=='y':
            graph_work.graph("mi_rate.csv")
        else:
            pass
            
    try:        
        L=list(a.values())
    except AttributeError:
            print("Currently Unavailable")

    file_exists = True
        
    if not os.path.exists("./rate.csv"):
            file_exists = False
    with open("rate.csv","a") as file:
            writer = csv.writer(file,lineterminator ="\n")
            fields = ["Name","price","Deal","url","Timestamp"]
            
            if not file_exists:
                writer.writerow(fields)

            timestamp = now.strftime("%d-%m-%Y")
            L=list(a.values())
            writer.writerow([L[0],L[1],L[2],L[3],L[4]])
            print("wrote csv data")

    while True:
        price = L[1]
        
        if(price <= budget):
            print("YES! It's within ur budget")
            send_email(email)
            break
        else:
            print("It's currently not within ur budget")
        time.sleep(70)



