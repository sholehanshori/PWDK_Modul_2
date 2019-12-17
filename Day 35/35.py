#  ------------------------ Senin, 16 Desember 2019 -----------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d


fig = plt.figure()
p   = plt.subplot(111, projection='3d')

x  = np.arange(10)
y  = np.arange(10)
z  = np.arange(10)

# Untuk visualisasi berupa garis
# p.scatter(x, y, z)
# plt.show()

# --------------------------------------------------
# Membentuk grafik bar 3 dimensi

# Merepresentasikan titik mulai tiap sumbu axis
x  = np.arange(10)
y  = np.arange(10)
z  = np.zeros(10)

# Merepresentasikan value dari tiap sumbu axis
dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(10)

p.set_xlabel('Sumbu X')
p.set_ylabel('Sumbu Y')
p.set_zlabel('Sumbu Z')

p.bar3d(x, y, z, dx, dy, dz)
plt.show()

# --------------------------------------------------
# Install seaborn
# pip install seaborn
import seaborn

# Install folium
# pip install folium
import folium