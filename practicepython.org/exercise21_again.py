from bs4 import BeautifulSoup
import requests

source = requests.get('http://theonion.com').text
soup = BeautifulSoup(source, 'lxml')


with open('onion_articles.txt', 'w') as open_file:
    for article in soup.find_all('article'):

        try:  
            headline = article.find('div', class_='sc-1pw4fyi-2 huquYN')
            headline = headline.find('a',class_='sc-1out364-0 hMndXN sc-1pw4fyi-4 hdsFUF js_link')
            headline = headline.h4.text
        except:
            headline = '!!!Error Loading!!!'
        finally:

            open_file.write(headline)
            open_file.write('\n\n')
