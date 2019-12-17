#  ------------------------ Jumat, 15 November 2019 -----------------------------------
# Practice membuat pola di OpenSpace
# Pola seperti di bawah ini kemudian di masukkan ke dalam file .xlsx
'''
1 2 3       1 4 7       3 2 1       9 6 3
4 5 6       2 5 8       6 5 4       8 5 2
7 8 9       3 6 9       9 8 7       7 4 1
'''


import xlsxwriter
file = xlsxwriter.Workbook('file.xlsx')
# sheet = add.Workbook()
sheet1 = file.add_worksheet('sheet 1')
sheet2 = file.add_worksheet('sheet 2')
sheet3 = file.add_worksheet('sheet 3')
sheet4 = file.add_worksheet('sheet 4')

n1 = 1
for r in range(3):
    for c in range(3):
        sheet1.write(r,c,n1)
        n1 += 1

n2 = 1
for r in range(3):
    for c in range(3):
        sheet2.write(r,c,n2)
        n2 += 3
    n2 -= 8

n3 = 3
for r in range(3):
    for c in range(3):
        sheet3.write(r,c,n3)
        n3 -= 1
    n3 += 6

n4 = 9
for r in range(3):
    for c in range(3):
        sheet4.write(r,c,n4)
        n4 -= 3
    n4 += 8

file.close()