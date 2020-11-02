
import requests
import webbrowser
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print(r.content[:100])

rows = soup.select('table')
row = rows[0]
name = row.select_one('tbody').text.strip()

print(name)
