#  ------------------------ Selasa, 19 November 2019 -----------------------------------

# scrapping website http://digidb.io/digimon-list/
# Diambil data tabel dan dimasukkan ke .xlsx atau .csv

import requests
from bs4 import BeautifulSoup
import xlsxwriter

link = 'http://digidb.io/digimon-list/'
url  = requests.get(link)
data = BeautifulSoup(url.content, 'html.parser')

digimon = xlsxwriter.Workbook('digi.xlsx')
sheet   = digimon.add_worksheet('Digimon')

digi = data.tbody
namedigi    = digi.find_all('a')
contentdigi = digi.find_all('center')
imagedigi   = digi.find_all('img')

digi2 = data.tr
headlist    = digi2.find_all('th')

isi1 = []
for i in namedigi:
    isi1.append(i.text)

isi2 = []
for j in contentdigi:
    isi2.append(j.text)

isi3 = []
for k in imagedigi:
    image = k.get('src')
    isi3.append(image)

top = []
for l in headlist:
    top.append(l.text)

x   = 'Image'
top.append(x)
top = top[1:]
print(top)

# for y in isi1:
    




# for i in range(len(list_header)):
#     y = dict(zip(list_header, list_content[0:][i]))
#     dataDiri.append(y)

import csv
# with open('digimon.csv', 'w', newline='') as isi:
#     kolom = ['nama', 'umur', 'pendidikan']
#     abc = csv.DictWriter(isi, fieldnames=kolom)
#     abc.writeheader()
#     abc.writerows(data)









# g = 0
# total = []
# for h in range(int(len(isi)/11)):
#     count = 0
#     konten = []
#     for i in range(12):
#         if count != 11:
#             konten.append(isi[g])
#             count += 1
#         else:
#             count = 0
#             break
#         g += 1
#     total.append(konten)

# print(isi)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# apa = data.tbody
# abc = apa.find_all('center')

# isi2 = []
# for j in abc:
#     isi2.append(j.teks)
# print(isi2)



# url  = requests.get(link)
# data = BeautifulSoup(url.content, 'html.parser')


# g = 0
# for h in range(int(len(isi)/11)):
#     count = 0
#     for i in range(12):
#         if count != 11:
#             sheet.write(h,i,isi[g])
#             count += 1
#         else:
#             count = 0
#             break
#         g += 1

# digimon.close()