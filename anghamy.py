from bs4 import BeautifulSoup
import os
path = r"anghamy.html"
soup = BeautifulSoup(open(path), 'html5lib')


data = soup.find_all('div', attrs={'class':'cell cell-title'})

for item in data:
    feld = item.text
    print(feld)
