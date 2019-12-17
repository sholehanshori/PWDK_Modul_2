#  ------------------------ Rabu, 11 Desember 2019 -----------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [9,5,7,3,6],
    'z': [2,3,4,5,3]
})

plt.figure('Tes Grafik 1')
plt.plot(df['x'], df[['y', 'z']])

plt.grid(True)
plt.xticks(np.arange(0, 7, step=1), rotation=45)
plt.title('Tes Chart')
plt.show()