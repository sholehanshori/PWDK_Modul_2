#  ------------------------ Jumat, 13 Desember 2019 -----------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

# pict = im.imread('doraemon.png')
# plt.imshow(pict)
# plt.show()

df = pd.read_csv('dataSales.csv')
# print(df)

# Hasil yang didapatkan kurang rapi dan menarik untuk di tampilkan, 
# sehingga butuh dirubah dengan Jenis Mobil sebagai kolom index

df = df.pivot(index='nama', columns='mobil')
# print(df)

fig, p = plt.subplots()
plt.imshow(df)
plt.colorbar()

col = list(map(lambda x: x[1], df.columns.tolist()))
i   = list(map(lambda x: x, df.index.tolist()))

p.set_xticks(np.arange(len(col)))
p.set_xticklabels(col)
p.set_yticks(np.arange(len(i)))
p.set_yticklabels(i)

# plt.show()


fig, p = plt.subplots()
plt.imshow(df, cmap='BuPu_r')      # penambahan '_r' sebagai reverse atau dibalik
plt.colorbar()

col = list(map(lambda x: x[1], df.columns.tolist()))
i   = list(map(lambda x: x, df.index.tolist()))

# Untuk memberi keterangan nilai dari tiap kotak
for x in range(len(i)):
    for y in range(len(col)):
        p.text(y, x, df.iloc[x, y], color='y')

p.set_xticks(np.arange(len(col)))
p.set_xticklabels(col)
p.set_yticks(np.arange(len(i)))
p.set_yticklabels(i)

# plt.show()

# ---------------------------------------------------
import mpl_toolkits.mplot3d.axes3d

# fig, p = plt.subplots()
fig = plt.figure()
p   =  plt.subplot(111, projection='3d')
data = range(11)
x   = np.array(data)

p.plot_wireframe(
    x, x, x.reshape(1, -1), color='r', linestyle=':'
)

p.scatter(x,x,x, marker='*', color='y', s=150)
p.set_xlabel('sumbu X')
p.set_ylabel('sumbu Y')
p.set_zlabel('sumbu Z')
plt.show()