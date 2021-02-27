import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

search = input("enter the product")
start_char = search[0]
string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

A_to_G = string[0:7]
H_to_P = string[8:16]
Q_to_Z = string[16:25]

if start_char in A_to_G:
    web = 'https://www.midwayusa.com/'
    file = 'midwayusa.txt'
    f = open(file, 'r')
    products = []
    urls=[]
    for url in f:
        url = url.rstrip("\n")
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        div = soup.find("div", class_="product-block-status")
        button = div.find("div",class_="product-item-container")
        product_title = soup.find('h1', id='l-product-description').get_text()
        regex = re.compile(r'[\n\r\t]')
        product_title = regex.sub(" ", product_title)
        product_title=product_title.lstrip().rstrip()
        products.append(product_title)
        urls.append(url)
    product=pd.DataFrame(products,urls)
    product["web"] =web
    product.to_csv('midwayusa.csv')



elif start_char in H_to_P:
    web = 'https://palmettostatearmory.com/'
    file = 'palmettostatearmory.txt'
    f = open(file, 'r')
    title=[]
    urls=[]
    for url in f:
        url = url.rstrip("\n")
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_title = soup.find('span',class_="base").get_text()
        title.append(product_title)
        urls.append(url)
    product = pd.DataFrame(title,urls)
    product["web"] = web
    product.to_csv('palmettostatearmory.csv')


elif start_char in Q_to_Z:
    web = 'https://www.brownells.com/'
    file = 'brownells.txt'
    f = open(file, 'r')
    title=[]
    urls=[]
    for url in f:
        url = url.rstrip("\n")
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        products = soup.find('h1', class_='mbm')
        product_title1 = products.find_all('span')[0].get_text().lstrip().rstrip()
        product_title2 = products.find_all('span')[-1].get_text().lstrip().rstrip()
        product_title  = f'{product_title1}{product_title2}'
        title.append(product_title)
        urls.append(url)
    product = pd.DataFrame(title,urls)
    product["web"] = web
    product.to_csv('brownells.csv')


