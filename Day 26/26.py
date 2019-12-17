#  ------------------------ Kamis, 28 November 2019 -----------------------------------

import numpy as np

x = [[1,20,3,400,5], [3,5,7,9, 11]]

y = np.array(x)
# print(y.max())
# print(y.min())
# print(np.argmax(y))
# print(np.argmin(y))

# print(y.shape)          # (2, 5)
# print(y.reshape(10))    # nilai 10 sesuai dengan total elemen
# print(y.reshape(-1))    # mempunyai nilai seperti di atasnya, menghitung sendiri 1 dimensi yg muat

# print(y.reshape(5, -1))   # 2 dimensi dengan isi 5 bagian ...(5, 2)...
# print(y.reshape(-1, 1, 2))

a = np.array([[1,2,3], [4,5,6]])
# print(a+a)
b = np.array([[0,0,0], [0,0,0]])
# print(a+b)
c = np.zeros((2,3))
# print(c)

# Mengecek tipe dari 'c' dibandingkan dengan 'd'
# print(b.dtype)
# print(c.dtype)
# Merubah tipe dari 'c'
c = np.zeros((2,3), dtype='int32')
# print(c.dtype)
# print(c)

d = np.ones((2,3))      # 2 bagian, 3 elemen
# print(d*a)

# ----------------------------------------------------------
# Penggunaan Boolean 'True/False' terhadap 1 / 0
ab = np.zeros((2, 2), dtype=bool)
# print(ab)

ba = np.ones((2, 2), dtype=bool)
# print(ba)

ac = np.full((2,2), 1, dtype=bool)
# print(ac)

ca = np.full((2,2), 1)
# print(ca)

lain = np.full((2,2), 'Andi')
# print(lain)
# print(type(lain))


# ----------------------------------------------------------
print(lain.tolist())        # Cara merubah 'NUMPY' ke dalam 'LIST'
print(type(lain.tolist()))
# ----------------------------------------------------------


da = [0,1,2,3,4]
db = [5,6,7,8,9]
# membuat list z = [[0,1,2,3,4], [5,6,7,8,9]]

# Cara 1
z = []
z.append(da)
z.append(db)
# print(z)

# Cara 2
z = [da, db]
# print(z)

# Cara 3
z = np.array(da+db).reshape(2,-1).tolist()
# print(z)

# Cara 4
dc = []
dc.extend(da)
dc.extend(db)
z = np.array(dc).reshape(2,-1).tolist()
# print(z)

# Cara 5
xnp = np.array(da)
ynp = np.array(db)
z = np.concatenate([[xnp], [ynp]], axis=0).tolist()
# print(z)

# Cara 6
z = np.vstack([xnp, ynp]).tolist()
# print(z)

# Cara 7
z = np.r_[[xnp], [ynp]].tolist()
# print(z)

# Cara 8
z = np.row_stack((xnp, ynp)).tolist()
# print(z)


# ----------------------------------------------------------

za = np.arange(6).reshape(2,-1)      # Dalam range 5
zb = np.array([5,6,7,8,9,10]).reshape(2,-1)

zc = np.vstack([za,zb])
# print(zc)
zc = np.hstack([za,zb])
# print(zc)

# 4 Cara yg sama
zd = np.vstack([za,zb])
# print(zd)
ze = np.concatenate([za,zb], axis=0)
# print(ze)
zf = np.row_stack((za,zb))
# print(zf)
zg = np.r_[za,zb]
# print(zg)

# ----------------------------------------------------------
zh = np.arange(1,11)
# print(zh)
# print(zh[1::2])         # Cara "slicing", untuk mendapatkan nilai 'Genap' saja
# print(zh[zh%2 == 0])    # Khusus numpy, menggunakan condition seperti 'modulus'
# print(zh[zh%2 != 0])    # Untuk nilai ganjil

# print(np.where(zh % 2 != 0, 'Ganjil', zh))

# ----------------------------------------------------------
zi = np.arange(10,20)

# print(np.where(zi<16))
# print(zi[np.where(zi<16)])
# print(zi[np.arange(5)])       # Penjelasan untuk yg di atasnya

# print(zi[np.where((zi>14) & (zi<18))])              # filter antara 2 parameter
# print(zi[np.where(np.logical_and((zi>14),(zi<18)))])  # Memiliki hasil yg sama seperti sebelumnya

# ----------------------------------------------------------
# Determinan "Matriks" 2x2
zj = np.array([[3,1], [2,5]])
# print(zj)
# print(np.linalg.det(zj))

# Determinan "Matriks" 3x3
zk = np.array([[[1,2,1], [3,3,1], [2,1,2]]])
# print(zk)
# print(np.linalg.det(zk))

# Invers Matriks 2x2
zl = np.array([[3,2], [1,4]])
# print(zl)
# print(np.linalg.inv(zl))

# dot product
print(zl@np.linalg.inv(zl))         # Matematis
print(zl.dot(np.linalg.inv(zl)))    # Matematis

# Cross product x
print(np.cross(zl,zl))              # Matematis
