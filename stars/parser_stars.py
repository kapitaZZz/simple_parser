import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url = 'http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html'  # url for parse

user_agent = UserAgent()  # user fake_useragent to access the server

header = {'User-Agent': user_agent.opera}  # use any browser you want

response = requests.get(url, headers=header)

html = response.text  # get html code from site

soup = BeautifulSoup(html, 'html.parser')

container = soup.find('div', {'class': 'td-post-content'})  # looking for the desired content
elements = container.find_all('p')

data_parser_name = 'Top the largest stars: \n'  # header for output file

for element in elements:
    if element.find('strong'):
        data_parser_name += '\t' + element.strong.text + '\n'  # looking for the desired element

with open('data_file.txt', 'w', encoding='UTF-8') as data_file:
    data_file.write(data_parser_name)  # write desired information in file
