#  ------------------------ Selasa, 10 Desember 2019 -----------------------------------

# Install matplotlib
# pip install matplotlib

# from matplotlib import pyplot as plt
# atau
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9]
y = [1,3,5,2,4,6,8,7,3]

plt.plot(x,y)

plt.title('X vs Y')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['Garis XY'])

# plt.show()


# ------------------------------------------------------
a = np.array([1,2,3,4,5,6,7,8,9])
b = a ** 2
c = a ** 3

plt.plot(a, a, a, b, a, c)

plt.title('Testing')
plt.xlabel('Nilai A')
plt.ylabel('Nilai B / C')
plt.grid(True)
plt.legend(['Garis AA', 'Garis AB', 'Garis AC'])

plt.show()