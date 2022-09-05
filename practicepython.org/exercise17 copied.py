import requests
from bs4 import BeautifulSoup

url = 'http://www.cnn.com/'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text, 'html.parser')
title = soup.findAll('span', {'class': 'cd__deadline-text'})
for row in title:
     ttl_lst.append(row.text)

print (ttl_lst)
