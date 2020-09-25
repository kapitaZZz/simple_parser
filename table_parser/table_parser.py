from bs4 import BeautifulSoup
import requests

url = 'https://basetop.ru/samyie-dlinnyie-reki-mira/'  # type here your URL

response = requests.get(url)

if response.status_code == 200:
    html = response.text

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')  # search for table

lines = table.find_all('tr')  # search for lines in table

result_parser = 'Length of rivers \n'

for e, tr in enumerate(lines):  # e - count of lines
    lines_td = tr.find_all('td')
    if len(lines_td) == 0 or e == 0:  # if line is empty or head of table
        continue
    else:
        name = lines_td[1].text.strip()  # use [num] for find desire field in table
        length = lines_td[2].text.strip()
        result_parser += '\t{} : {} - {} kilometres \n'.format(e, name, length)

with open('file_name', 'w', encoding='UTF-8') as data_file:
    data_file.write(result_parser)
