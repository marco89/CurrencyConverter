import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.x-rates.com/table/?from=GBP&amount=1')

soup = BeautifulSoup(page.content, 'html.parser')

tds = soup.find_all('td', attrs={'class': 'rtRates'})

print(tds[0])