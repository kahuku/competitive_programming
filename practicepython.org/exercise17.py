import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.cnn.com')
soup = BeautifulSoup(page.content, 'html.parser')

for heading in soup.find_all(class_="cd__headline-text"):
    if heading.a:
        print(heading.a.text.replace("\n"," ").strip())
    else:
        print(heading.contents[0].strip())
