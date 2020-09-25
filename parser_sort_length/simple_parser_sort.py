import requests
from bs4 import BeautifulSoup

url = 'https://planetanauk.ru/blog/earth_distance/2010-07-14-7'

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

ul = soup.find_all('ul')

arr_data = []

for tag in ul:
    if 'Меркурий' in tag.text:
        data = tag.text.strip().replace(' ', '').split('\n')

for _ in data:
    temp = _.split('-')
    temp[1] = int(float(temp[1]) * 100000)
    arr_data.append(temp)

arr_data = sorted(arr_data, key=lambda x: x[1], reverse=True)

head = 'Distance from Earth to planets: \n'

for data in arr_data:
    head += '\t' + data[0] + ' - ' + str(data[1]) + ' kilometres \n'

with open('data_file.txt', 'w', encoding='UTF-8') as data_file:
    data_file.write(head)
