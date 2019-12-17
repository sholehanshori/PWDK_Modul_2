#  ------------------------ Selasa, 19 November 2019 -----------------------------------

# install extension live-server
# untuk bentuk baku html, ketik html:5

# Install berikut dengan ketik di terminal
# pip install beatifulsoup4
# pip3 install beatifulsoup4
# py -m pip install beatifulsoup4

from bs4 import BeautifulSoup
# web scraping from html file
data = BeautifulSoup(
    open('digi.html', 'r'), 'html.parser'
    )

# print(data.prettify())
# print(data.title)
# print(data.title.name)
# print(data.title.text)
# print(data.title.string)

# print(data.h1)
# print(data.h1.name)
# print(data.h1.text)
# print(data.h1.string)

# print(data.find_all('li'))
# print(type(data.find_all('li')))
# print(data.find('li'))          # untuk mencari data pertama saja, perbedaan dengan "find_all"

# Teknik web scrapping
# ul = data.ul
# print(ul)

# for i in ul.find_all('li'):
#     print(i)       # coding ikut terprint

# for i in ul.find_all('li'):
#     print(i.text)  # Hanya konten saja yg diprint

# print(data.find(class_ = 'orang'))
# ul = data.ul
# for i in ul.find_all('li', class_ = 'orang'):
#     print(i.text)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Web scrapping dari "url"

import requests
web   = requests.get('http://127.0.0.1:5500/Day%2019/digi.html')
# print(web.status_code)      # Untuk melihat status apakah dapat di akses
data2 = BeautifulSoup(web.content, 'html.parser')
# print(data)

# ul = data2.ul
# for i in ul.find_all('li', class_ = 'orang'):
#     print(i.text)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Latihan me-extract informasi dari website
# Hanya nama-nama Ultraman

import requests
from bs4 import BeautifulSoup
link  = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data3 = BeautifulSoup(link.content, 'html.parser')
# print(data3.find_all('strong'))     # Me-locate posisi 01 Ultraman

strong = data3.find_all('strong')

out  = []
for i in strong:
    out.append(i.text)

# Mensortir konten nama 'Ultraman' dan nama 'Monster'
ultra   = out[2:36]
monster = out[37:110]

print(ultra)
print(monster)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# scrapping website http://digidb.io/digimon-list/
# Diambil data tabel dan ditaro di .xlsx atau .csv

