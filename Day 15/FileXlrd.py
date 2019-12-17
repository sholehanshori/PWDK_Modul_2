#  ------------------------ Rabu, 13 November 2019 -----------------------------------

import xlrd

# pip install xlrd
# py -m pip install xlrd

# Cara install multi package 
# install namaP1 namaP2 namaP3
# P = package

file  = xlrd.open_workbook('file.xlsx')
sheet = file.sheet_by_index(0)

# print(sheet.nrows, sheet.ncols)
# print(sheet.cell_value(0,0))        # (  0  ,  0   )
# print(sheet.cell_value(0,1))        # (baris, kolom)
# print(sheet.cell_value(0,2))

# nama kolom di file xlsx
# for i in range(sheet.ncols):
    # print(sheet.cell_value(0,i))

# memasukkan kolom ke dalam list
# cols = []
# for i in range(sheet.ncols):
#     cols.append(sheet.cell_value(0,i))
# print(cols)

# alternative atau cara cepatnya
# print(sheet.row_values(0))

# for i in range(sheet.nrows):
#     print(sheet.row_values(i))


# ==================================================
''' Convert file xlsx ke Json dan Csv, vice versa '''
# xlsx => json
# xlsx => csv
# json => xlsx
# csv  => xlsx

data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
print(data)

out = []
for i in data:
    out.append(dict(zip(data[0], i)))
out = out[1:]
print(out)

# ==================================================
import csv
with open('file.csv', 'w', newline='') as file:
    kolom = list(out[0].keys())
    tulis = csv.DictWriter(file, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(out)

# ==================================================
import json
with open('file.json', 'w') as outfile:
    json.dump(out, outfile)