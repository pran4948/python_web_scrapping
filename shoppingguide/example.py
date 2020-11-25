import requests
from bs4 import BeautifulSoup

str = input('Enter Product Name: ')
url = 'https://www.flipkart.com/search?q='
str = str.replace(' ','+')
url+=str
print(url)

page = requests.get(url)
soup = BeautifulSoup(page.content)
content = soup.find_all(class_='E2-pcE')
