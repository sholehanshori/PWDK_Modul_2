#  ------------------------ Selasa, 26 November 2019 -----------------------------------

import pymongo

dburl   = 'mongodb://localhost:27017/'
mymongo = pymongo.MongoClient(dburl)

# dbs = mymongo.list_database_names()
# print(dbs)

mydb  = mymongo['pymongodb']        # Database yg dipakai
mycol = mydb['colmong']             # Kolom/tabel yg dipakai
# alldata = list(mycol.find())
# alldata = list(mycol.find({'usia': 'Andi'}))
alldata = list(mycol.find({'usia': {'$gt': 24} }))
# print(alldata)


# Bila memasukkan 1 data
# mydata = {'nama': 'Deni', 'usia': 18, 'kota': 'Kediri'}
# mycol.insert_one(mydata)


# Bila memasukkan lebih dari 1 data
mydata = [
    {'nama': 'Euis', 'usia': 35, 'kota': 'Denpasar'},
    {'nama': 'Fafa', 'usia': 29, 'kota': 'Jakarta'},
    {'nama': 'Gian', 'usia': 22, 'kota': 'Sorong'}
]
# mycol.insert_many(mydata)


# Menampilkan beberapa data tertentu
nama = ['Andi', 'Euis', 'Fafa']
# print(list(mycol.find({'nama': {'$in': nama}})))

# Mengambil data menggunakan "inserted_id"
# x = mycol.insert_one({'nama': 'Nino'})
# print(x.inserted_id)
# print(list(mycol.find({'_id': x.inserted_id})))


# Menghapus salah satu atau banyak data
y = {'nama' : 'Nino'}
# mycol.delete_one(y)


# Untuk meng-update data atau edit data
data = {'nama' : 'Euis'}
new  = {'nama' : 'Gus De'}
mycol.update_one(data, {'$set': new})



# Usia > 25 dan usia < 30 => update nama: 'Youngman'
data2 = {'$and': [{'usia': {'$gt': 25}}, {'usia': {'$lt': 30}}]}
new2  = {'nama': 'Youngman'}
# mycol.update_many(data2, {'$set': new2})

# --------------------------------------------------------------------
import datetime

dburl   = 'mongodb://localhost:27017/'
mymongo = pymongo.MongoClient(dburl)

mydb2  = mymongo['hahaha']        # Database yg dipakai
mycol2 = mydb2['hahaha1']         # Kolom/tabel yg dipakai

# mycol2.insert_one({'nama': 'Budi', 'waktu': datetime.datetime.now()})         # Penggunaan hanya waktu lokal
# mycol2.insert_one({'nama': 'Deni', 'waktu': datetime.datetime.utcnow()})      # Penggunaan waktu global GMT
query  = mycol2.find({'nama': 'Deni'}, {'waktu':1})
# print(list(query)[0]['waktu'])


# Menggunakan waktu global GMT di convert menjadi waktu lokal
import pytz
jkt = pytz.timezone('Asia/Jakarta')
print(jkt.localize(list(query)[0]['waktu']))




# kaggle datasets download -d (link)
# kaggle datasets list
# kaggle datasets list --sort-by 