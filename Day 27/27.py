#  ------------------------ Jumat, 29 November 2019 -----------------------------------

import numpy as np
x = np.arange(1, 10).reshape(3, -1)
# print(x)

#----- Swaping -----
# print(x[:, [1,0,2]])        # Berdasarkan index grup
# print(x[:, [0,0,0]])        # Merubah semua kolom berdasarkan index pertama tiap row
#  #   (x[ [row , column] ])  --- representasi dari bagian atas
# print(x[[1,0,2], :])
# print(x[[0,0,0], :])

#----- Transpose -----
# a b
# c d   =    a c e
# e f        b d f

a = np.array([[1,2],[3,4],[5,6]])
# print(a)
# print(a.transpose())

#---------------------------------------------
aa = np.loadtxt('0.csv', skiprows=1, delimiter=',')        # Tidak bisa membaca 'string', hanya 'int' dan 'float'
print(aa)
print(type(aa))

ab = np.loadtxt('0.csv', skiprows=1, delimiter=',', unpack=True)  # Penggunaan 'unpack' untuk mengelompokkan 'column'
print(ab)

id, usia = np.loadtxt('0.csv', skiprows=1, delimiter=',', unpack=True)
print(id)           # Memisahkan kolom secara langsung, berupa 2 data
print(usia)

#-- Menggabungkan 2 kolom yg terpisah
ac = list(map(lambda a,b: [a,b], id, usia))
print(ac)


np.savetxt('1.csv', usia, fmt='%d', header='usia', comments='')
# Penggunaan '%d' agar berupa digit biasa
# Penggunaan comments='', karena secara default di depan header='usia', akan ada # di depan kata usia

# -- Membuat file .csv dari data di atas, tapi formatnya sesuai
np.savetxt('2.csv', aa, fmt='%d', header='id,usia', comments='', delimiter=',')
np.savetxt('3.csv', ac, fmt='%d', header='id,usia', comments='', delimiter=',')
# Penggunaan delimiter=',' agar ada pemisah ',' di antara kolom