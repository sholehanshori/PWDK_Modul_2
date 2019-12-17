#  ------------------------ Kamis, 14 November 2019 -----------------------------------

import xlsxwriter
file  = xlsxwriter.Workbook('z.xlsx')
sheet = file.add_worksheet('Data')
for i in range(10):
    sheet.write(i, 0, i)
file.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
