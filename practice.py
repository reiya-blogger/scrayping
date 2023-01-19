import requests
from bs4 import BeautifulSoup

url = 'https://www.mizuhobank.co.jp/rate_fee/rate_interest.html'
res = requests.get(url)

print(res)

print(res.text)