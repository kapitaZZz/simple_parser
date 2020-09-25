import requests
from bs4 import BeautifulSoup


url = 'https://www.worldfootball.net/teams/arsenal-fc/2013/3/'

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'standard_tabelle'})

lines = table.find_all('tr')

goal = 0
matches = 0

for line in lines:
    elements = line.find_all('td')
    if len(elements) == 8:
        goal += int(elements[-2].text.strip().split(':')[0])
        matches += 1

print(goal / 2, matches)