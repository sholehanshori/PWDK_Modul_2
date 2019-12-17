#  ------------------------ Rabu, 13 November 2019 -----------------------------------

import xlsxwriter
# pip install xlsxwriter
# py -m pip install xlswriter

# Membuat file excel 
file = xlsxwriter.Workbook('test123.xlsx')
sheet = file.add_worksheet('Data')

sheet.write(0, 0, 'Name')       # row, col, data
sheet.write(0, 1, 'City')       # row, col, data
sheet.write(0, 2, 'Job')        # row, col, data

file.close()        # Untuk menutup semua function, artinya semua selesai

# ==================================================
import xlrd
file2 = xlrd.open_workbook('file.xlsx')
sheet = file2.sheet_by_name('Sheet1')
data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
print(data)

# ==================================================
### Latihan ####
# xlsx => new xlsx
# json => new xlsx
# csv  => new xlsx

import xlsxwriter
col = ['no', 'nama', 'kota']
data = [
    [1, 'Andi', 'Jakarta'],
    [2, 'Budi', 'Jakarta'],
    [3, 'Caca', 'Jakarta']
]
file3 = xlsxwriter.Workbook('data.xlsx')
sheet = file3.add_worksheet('SheetA')

# write col
for i in col:
    sheet.write(0, col.index(i), i)

# write data
row = 1
for x, y, z in data:
    sheet.write(row, 0, x)
    sheet.write(row, 1, y)
    sheet.write(row, 2, z)
    row += 1
file3.close()
# ==================================================
import json
with open('file.json', 'r') as file4:
    x = json.load(file4)
col  = list(x[0].keys())
data = []
for i in x:
    data.append(list(i.values()))
# print(x)
# print(data)

# ==================================================
# Alternative
file5 = xlrd.open_workbook('file.xlsx')
sheet = file5.sheet_by_index(0)

newFile  = xlsxwriter.Workbook('testFile.xlsx')
newSheet = newFile.add_worksheet('Item')

for i in range(sheet.ncols):
    newSheet.write(0, i, sheet.cell_value(0,i))

for i in range(1, sheet.nrows):
    for j in range(sheet.ncols):
        newSheet.write(i, j, sheet.cell_value(i, j))

newFile.close()

# ==================================================
#### Tugas ####
# Dimasukkan ke dalam file excel (.xlsx)
# ab = input('Masukkan data : ')
# ac = input('Masukkan kata : ')
