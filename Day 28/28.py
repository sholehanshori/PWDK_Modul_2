#  ------------------------ Selasa, 3 Desember 2019 -----------------------------------

# Pandas ---- pip install pandas

# Hal yg penting untuk dipahami
# numpy  = array, dimensi, shape
# pandas = konsep dataframe

import pandas as pd
import numpy as np

# Membentuk index series
a = np.array([1,2,3,4,5,6,7,8,9])
aSeries = pd.Series(a)
print(aSeries)

aDataFrame = pd.DataFrame([[1,2], [3,4], [4,5]], columns=['A', 'B'])
print(aDataFrame)