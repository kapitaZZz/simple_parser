import requests
from bs4 import BeautifulSoup
import csv

url = 'http://sportunit.ru/velosipedy/gornye-26'

response = requests.get(url)

html = response.text

multi_class = 'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12'

soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all('div', {'class': multi_class})

all_prods = []

for product in products:
    name = product.find('div', {'class': 'product-name'}).text
    image = product.find('img')['src']
    description = product.find('div', {'class': 'product-description'}).text
    code = product.find('div', {'class': 'product-model'}).text
    price = product.find('p', {'class': 'price'}).text.strip()
    all_prods.append([name, code, description, price])

names = ['NAMES', 'CODE', 'DESCRIPTION', 'PRICE']

with open('data.csv', 'w', newline='') as data_file:
    writer = csv.writer(data_file, delimiter=', ')
    writer.writerow(names)

    for product in all_prods:
        writer.writerow(product)
