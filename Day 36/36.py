#  ------------------------ Selasa, 17 Desember 2019 -----------------------------------

# install plotly
# pip install plotly

import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

pio.renderers.default = "browser"

x = np.array([1,2,3,4,5])
y = np.array([2,1,4,1,3])

myFig = go.Figure(
    data = go.Bar(x=x, y=y)
)

# myFig.show()
myFig.write_html('plotlyTes.html', auto_open=True)

# Belajar Flask, liat di folder "flaskTes"