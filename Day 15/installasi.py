'''
install xlrd
pip install xlrd
py/python/python3 -m pip install xlrd
conda install xlrd
pip3 install xlrd

py -m pip list cek list package yg ada
'''
# xlsxwriter untuk menulis file excel versi baru
# xlwt (.xls) excel versi lama
# install dulu

# import xlrd # untuk baca file excel
# file=xlrd.open_workbook('file.xlsx')
# # sheet=file.sheet_by_index(0) #by_index(0), by_name(klo ada nama)
# sheet=file.sheet_by_name('DataKaryawan')
# print(sheet.nrows,sheet.ncols)
# print(sheet.cell_value(0,0)) #baris,kolom
# print(sheet.cell_value(0,1))
# print(sheet.cell_value(0,2))

# nama kolom di file xlsx
# for i in range(sheet.ncols):
#     print(sheet.cell_value(0,i)) # (0,0)(0,1)(0,2)

# cols=[]
# for i in range(sheet.ncols):
#     cols.append(sheet.cell_value(0,i)) # semua hasil masuk ke list
# print(cols)

# print(sheet.row_values(0)) # list dari semua nilai baris 0

# for i in range(sheet.nrows):
#     print(sheet.row_values(i)) # dapat nilai semua data

# '''masukin data dari excel ke file json'''
# listxls=[] '''bikin list'''
# for i in range(sheet.nrows):
#     listxls.append(sheet.row_values(i))
# # print(listxls)

# listdict=[] '''bikin dictionary'''
# for i in listxls:
#     listdict.append(dict(zip(listxls[0],i))) # zip, memasangkan key dengan values jadi dict
# listdict=listdict[1:]    
# print(listdict)

# for i in range(len(out)): '''bikin dictionary'''
#     for j in range(len(out[i])):
#         sheet.write(i,j,out[i][j])

# with open('file.json','w') as x:
#     json.dump(listdict,x)

# '''masukin data dari excel ke file csv'''
# import xlsxwriter
# file=xlsxwriter.Workbook('test12.xlsx')
# sheet=file.add_worksheet('DataKaryawan')

# for i in range(len(listxls)):
#     for j in range(len(listxls[i])):
#         sheet.write(i,j,listxls[i][j])

# with open('file.csv','w',newline='') as x:
#     kolom=['no','nama','kota']
#     a=csv.DictWriter(x,fieldnames=kolom)
#     a.writeheader()
#     a.writerows(listdict)

# import xlsxwriter
# file=xlsxwriter.Workbook('test12.xlsx')
# sheet=file.add_worksheet('DataKaryawan')

# for i in range(len(listxls)):
#     for j in range(len(listxls[i])):
#         sheet.write(i,j,listxls[i][j])
# # sheet.write(0,0,'Nama') # baris,kolom,data
# # sheet.write(0,1,'Kota')
# # sheet.write(0,2,'Job')
# file.close() # close dulu utk muncul file

# '''ubah list jadi dictionary'''
# import xlsxwriter
# col=['no','nama','kota']
# data=[
#     [1,'Andi','Jakarta'],
#     [2,'Budi','Jakarta'],
#     [3,'Caca','Jakarta']
# ]

# file=xlsxwriter.Workbook('data.xlsx')
# sheet=file.add_worksheet('DataKaryawan')
# # write col
# for i in col:
#     sheet.write(0,col.index(i),i)

# # write data
# row=1
# for x,y,z in data:
#     sheet.write(row,0,x)
#     sheet.write(row,1,y)
#     sheet.write(row,2,z)
#     row+=1
# file.close()

# '''ambil data dari json masukin ke excel'''
# import json
# with open('file.json','r') as x:
#     out=json.load(x)
# # print(out)
# col=list(out[0].keys())
# # print(col)
# data=[]
# for i in out:
#     data.append(list(i.values()))
# # print(data)

# import xlsxwriter
# file=xlsxwriter.Workbook('datajson.xlsx')
# sheet=file.add_worksheet('DataKaryawan')

# # write col
# for i in col:
#     sheet.write(0,col.index(i),i)

# # write data
# row=1
# for x,y,z in data:
#     sheet.write(row,0,x)
#     sheet.write(row,1,y)
#     sheet.write(row,2,z)
#     row+=1
# file.close()

# '''ambil data dari csv masukin ke excel'''
# import csv
# with open('file.csv','r') as x:
#     baca=csv.DictReader(x)
#     out=[]
#     for i in baca:
#         out.append(dict(i))
#     # print(out)

# col=list(out[0].keys())
# # print(col)
# data=[]
# for i in out:
#     data.append(list(i.values()))
# # print(data)

# import xlsxwriter
# file=xlsxwriter.Workbook('datacsv.xlsx')
# sheet=file.add_worksheet('DataKaryawan')

# # write col
# for i in col:
#     sheet.write(0,col.index(i),i)

# # write data
# row=1
# for x,y,z in data:
#     sheet.write(row,0,x)
#     sheet.write(row,1,y)
#     sheet.write(row,2,z)
#     row+=1
# file.close()