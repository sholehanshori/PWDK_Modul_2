#  ------------------------ Kamis, 21 November 2019 -----------------------------------

# Install MySQL
# pip install MySQL-connector-python
# py -m pip install MySQL-connector-python
# pip3 install MySQL-connector-python

import mysql.connector

db = mysql.connector.connect(
    host   = 'localhost',
    port   = 3306,
    user   = 'sholeh_as',
    passwd = 'shaolin35',
    auth_plugin = 'mysql_native_password',
    database = 'ptabc'
)
c = db.cursor()
# c.execute('show databases')
# c.execute('show tables')
# c.execute('select * from karyawan')
# print(c.fetchall())

# x = c.fetchall()
# print(x)

sql = 'insert into karyawan (nama, gaji) values (%s, %s)'
val = ("Andi", 15000000)
c.execute(sql, val)     #executemany
db.commit()
print(c.rowcount, 'Data tersimpan')
# print(c.fetchall())


# sql = 'create database x'
# c.execute(sql)