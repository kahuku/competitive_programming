import requests
from bs4 import BeautifulSoup
url = 'https://floridageorgialine.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="container")
print(results)
