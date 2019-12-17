#  ------------------------ Jumat, 6 Desember 2019 -----------------------------------

import pandas as pd
import numpy as np

df = pd.read_csv('dataCoba.csv')
df = df.replace(['-', '#'], np.NaN)
df = df.fillna('XXX')
# print(df)

df2 = pd.read_csv('dataCoba.csv')
df2 = df2.replace({
    '-': '+',
    '#': np.NaN
})
# print(df2)

df3 = pd.read_csv('dataCoba.csv')
df3 = df3.replace({
    'usia': ['-', '#']
}, np.NaN)
# print(df3)

df4 = pd.read_csv('dataCoba.csv')
df4 = df4.replace({
    'usia': ['-', '#'],
    'nama': '#'
}, {
    'usia': np.NaN,
    'nama': 'Anonim'
})
# print(df4)


# -------------------------------------------------------------
df = pd.read_csv('dataCoba.csv')
# print(df)

# Mengisi kolom 'cell' kosong menggunakan 'cell' sebelumnya secara vertikal
df['usia'] = df['usia'].replace(
    to_replace = '-',
    method     = 'ffill'
)
# print(df)