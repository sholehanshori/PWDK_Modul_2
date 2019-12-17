#  ------------------------ Kamis, 14 November 2019 -----------------------------------

import requests         # pip install requests

# Materi tentang API
# Membuka website http://jsonplaceholder.typicode.com/
# Dan install aplikasi di dalam https://www.getpostman.com/downloads/

url  = 'http://jsonplaceholder.typicode.com/users'
data = requests.get(url)

# print(data)

# print(data.json())
# print(data.json()['address']['street'])
# print(data.json()['name'])
# print(type(data.json()))

# for i in data.json():
#     print(i['name'], 'di Jl.', i['address']['street'])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Menggunakan website https://thesportsdb.com/api.php
# input('Ketik klub : ')
# muncul list pemain

import requests
# klub = input('Nama klub : ')
# url  = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
# data = requests.get(url)
# Menggunakan 'postman' untuk cek konten

# Contoh tim, Arsenal, Real Madrid, Chelsea
# players = data.json()['player']

# for nama in players:
#     print(f"{nama['strPlayer']} ({nama['strPosition']})")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# mengambil quote dari website https://quotes.rest/#!/qod/get_qod
url = 'http://quotes.rest/qod'
data = requests.get(url)
data = data.json()
# print(data)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Menggunakan website forecast https://openweathermap.org/history
# API key 956faaa616385bccf9a137f7fe603065
# Menggunakan link api.openweathermap.org/data/2.5/weather?q= {NAMA KOTA} &appid= {API Key}
# Link dimasukkan ke dalam postman
# Menggunakan 'postman' untuk cek konten


appid = '956faaa616385bccf9a137f7fe603065'
kota = 'Jakarta'
url  = f'http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={appid}'
data = requests.get(url)
data = data.json()

sunrise = data['sys']['sunrise']
# sunset  = data['sys']['sunset']

from datetime import datetime
# waktu = datetime.utcfromtimestamp(int(sunrise))       # untuk meng-convert unictime di dalam url ke dalam waktu biasa
# print(waktu)


from dateutil import tz                 # py -m pip install python-dateutil
myzone = tz.gettz('Asia/Jakarta')
utc    = datetime.utcfromtimestamp(int(sunrise))
print(utc.astimezone(myzone))

print(utc.strftime('%d')+1)             # untuk tanggal hari
print(utc.strftime())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##### TUGAS #####
# 1. get .api sportdb, daftar pemain suatu klub
# 2. input: nama klub?
# 3. daftar pemain: nama, posisi, usia, negara
# 4. save ke dalam X.xlsx, X.json, X.csv
[
    {
        "nana":"", "usia":"", "posisi":"", "negara":""
    },
    {
        "nana":"", "usia":"", "posisi":"", "negara":""
    }
]