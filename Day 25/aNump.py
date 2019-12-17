#  ------------------------ Rabu, 27 November 2019 -----------------------------------
import numpy as np

x = [1,2,3,4,5]
y = np.array(x)

# print(x[::2])
# print(y[::2])

# print(x + x)
# print(y + y)
# print(type(y))

# ------------------------------------------------------------------
a = [
    [1,2,3], [4,5,6]
]

b = np.array(a)
# Mempunyai fugnsi yg sama seperti index hanya penulisannya berbeda
# print(a[1][1])
# print(b[1, 1])    # b[1][1]

# ------------------------------------------------------------------
c = [1,2,3]
c = np.array(c)
# Meng-cek jumlah dimensi
# print(c)
# print(c.ndim)   # 1 dimensi

d = [[1,2,3], [4,5,6]]
d = np.array(d)
# Cek jumlah dimensi
# print(d)
# print(d.ndim)   # 2 dimensi

e = [[[1,2,3],[4,5,6],[7,8,9]]]
e = np.array(e)
# Cek jumlah dimensi
# print(e)
# print(e.ndim)   # 3 dimensi

# print(e.size)
# print(e.dtype)
# print(e.itemsize)
# print(e.shape)

# ------------------------------------------------------------------
# Memiliki karakteristik seperti range
# print(np.arange(10))        # print(np.arange(1, 10, 2))
# print(list(range(10)))      # print(list(range(1, 10, 2)))

# print(np.random.random(10))     # Memiliki 1 list, dengan isi 10 data, dan rentang dari 0 - 1
# print(np.random.rand(2, 4))     # Memiliki 2 list, dengan isi 4 data, dan rentang dari 0 - 1
# print(np.random.randint(7, size=(2, 5)))       # Memiliki 2 list, dengan isi 5 data, dan rentang 0 - 7

# Spacing
# print(np.linspace(1, 5, 5))         # Untuk membuat rentang berdasarkan jumlah yg mau ditampilkan
# print(np.linspace(0, 100, 5))

# ------------------------------------------------------------------
f = [(1,2,3), (4,5,6), (7,8,9)]
f = np.array(f)

# print(f.ndim)   # memiliki dimensi 2
# print(f[0,2])

# print(f[0,2])
# print(f[0:2, 0:2])  # hanya bisa 2 grup data saja, karena 2 dimensi
# print(f[0:, 2])     # menampilkan elemen ke-2 dari setiap grup data
# print(f[0:, 0:2])   # menampilkan 2 elemen pertama dari tiap grup

# ------------------------------------------------------------------
g = [(1,2,3,4,5), (4,5,6,7,8), (7,8,9,10,11)]
g = np.array(g)

# print(g[0:, :1])                # size=3 shape=(3,1)

# print(g[0:, 0])                 # size=3 shape=(3,)
# # Merubah bentuk seperti yg di atas
# print(g[0:, :1].reshape(3,))    # size=3 shape=(3,)
# print(g[0:, :1].reshape(3,1,1))     # 3 dimensi, isi 1 grup, isi 1 elemen


# ------------------------------------------------------------------
# Penjumlahan dan Pengurangan "matriks"
h = np.array([
    [0, -7],
    [-1, 3]
])

i = np.array([
    [2, 4],
    [3, 8]
])

# print(a)
# print(b)

# print(h+i)
# print(h-i)
# ------------------------------------------------------------------
# Min / Max
ab = [1,2,3,4,5]
ba = np.array(ab)

# print(max(ab))  
# print(min(ab))

# print(ba.max())     # Mempunyai fungsi seperti pada 'list'
# print(ba.min())

# ------------------------------------------------------------------
from functools import reduce
x1 = [1,20,3,4,5]

xsum = reduce(lambda a,b: a+b, x1)
print(xsum)
xmax = reduce(lambda a,b: a if (a>b) else b, x1)
print(xmax)
xmin = reduce(lambda a,b: a if (a<b) else b, x1)
print(xmax)

abc = np.array(x1)
print(np.mean(abc))
print(np.median(abc))
print(np.pi)
print(np.sin(0))
print(np.cos(0))

# ------------------------------------------------------------------
# Menyelesaikan permasalahan matriks
# 2x + y = 5        | 2  1 | | x |  =  | 5 |
#  x + y = 7        | 1  1 | | y |     | 7 |

j = np.array([
    [2,1], [1,1]
])
k = np.array([5, 7])

# Penyelesaian mudah
hasil = np.linalg.solve(j, k)
# print(hasil)

# ------------------------------------------------------------------
# 4x + 7y = 2
# 3x + 2y = -5
# nilai 2x - 3y = ?

n = np.array([
    [4, 7],
    [3, 2]
])
o = np.array([2, -5])

hasil1 = np.linalg.solve(n, o)
# print(hasil1)
hasil2 = hasil1[0] * 2
hasil3 = hasil1[1] * 3
hasil4 = hasil2 - hasil3
# print(hasil4)
# atau
print(f'2x - 3y = {2*hasil1[0] - 3*hasil1[1]}')


# ------------------------------------------------------------------
# Ayam + kambing = 25  ~ 1A + 1K = 25
# Jumlah kaki 70       ~ 2A + 4K = 70

l = np.array([
    [1, 1],
    [2, 4]
])
m   = np.array([25, 70])
out = np.linalg.solve(l, m)

print(f'Jumlah Ayam: {int(out[0])} \nJumlah Kambing: {int(out[1])}')

# ------------------------------------------------------------------
# 2 buku, 1 pensil, 1 penghapus = 4700
# 1 buku, 2 pensil, 1 penghapus = 4300
# 3 buku, 2 pensil, 1 penghapus = 7100

p = np.array([
    [2, 1, 1],
    [1, 2, 1],
    [3, 2, 1]
])
q = np.array([4700, 4300, 7100])
out = np.linalg.solve(p, q)
print(f'Harga Buku {int(out[0])} \nHarga Pensil {int(round(out[1]))} \nHarga Penghapus {int(out[2])}')
