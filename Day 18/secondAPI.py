#  ------------------------ Senin, 18 November 2019 -----------------------------------

import requests
# bank   = input('Ketik bank: ')
# dollar = int(input('Ketika nominal USD : '))
# # bank   = bank.lower()

# url = f'https://kurs.web.id/api/v1/{bank}'

# data = requests.get(url)
# kurs = data.json()["jual"]
# kurs = int(kurs)

# print(f'Nilai {dollar} USD = Rp {dollar*kurs},-')

# --------------------------------------------------
# Website untuk 'kurs' dan 'bitcoin'
# https://kurs.web.id/api
# https://www.blockchain.com/api/exchange_rates_api

def konversi(x):
    x = int(x)
    if x == 1 or x == 2:
        bank   = input('Ketik bank: ')
        url  = f'https://kurs.web.id/api/v1/{bank}'
        data = requests.get(url)
        kurs1  = int(data.json()['beli'])
        kurs2  = int(data.json()['jual'])
        abc = f'Dengan nilai jual Rp. {kurs2},- dan beli Rp. {kurs1},-'
        if x == 1:
            rupiah = int(input('Ketik nominal yang akan dikonversi : '))
            konver = round(rupiah/kurs1, 2)
            print(f'Hasil konversi Rp. {rupiah},- adalah USD {konver}')
        elif x == 2:
            dollar = int(input('Ketik nominal yang akan dikonversi : '))
            print(f'Hasil konversi {dollar} USD adalah Rp. {dollar*kurs2},-')
        return abc
    elif x == 3:
        dollar = int(input('Ketik nominal yang akan dikonversi : '))
        url2   = f'https://blockchain.info/tobtc?currency=USD&value={dollar}'
        data2  = requests.get(url2)
        kurs3  = float(data2.json())
        print(f'Hasil konversi {dollar} USD adalah {kurs3} bitcoin')
        awd = 'Terima Kasih'
        return awd

print('Selamat datang \nSilahkan pilih konversi yang akan Anda lakukan: \n (1) IDR Indonesia     => USD United States \n (2) USD United States => IDR Indonesia \n (3) USD United States => Bitcoin')
Pilihan = input('Pilihan Anda (1/2/3): ')

print(konversi(Pilihan))

# --------------------------------------------------
# user-key =  27a874addc68824c40b168c70417e313
# http://developers.zomato.com/api/v2.1/search?entity_id=74&entity_type=city&q=soto

# dimasukkan ke dalam postman
# liat opsi header lalu centang 'user-key'

import requests

host     = 'http://developers.zomato.com/api/v2.1'
kategori = '/categories'
apikey   = '27a874addc68824c40b168c70417e313'
headinfo = {'user-key' : apikey}

url      = host + kategori
data     = requests.get(url, headers= headinfo)
# print(data.json()['categories'])

# Mengambil data restoran terkait makanan tertentu dengan mengambil data ID kota di website Zomato
# Webscrapping