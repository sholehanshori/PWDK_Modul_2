#  ------------------------ Jumat, 22 November 2019 -----------------------------------

import mysql.connector

db = mysql.connector.connect(
    host     = 'localhost',
    user     = 'sholeh_as',
    passwd   = 'shaolin35',
    database = 'ptabc'
)

# ------ 1 ------
c     = db.cursor()
query = 'select nama from karyawan'
c.execute(query)

out = c.fetchall()
# print(out)
# print(list(map(lambda x: x[0], out)))

# ------ 2 ------
d     = db.cursor(dictionary=True)
query = 'select nama from karyawan'
d.execute(query)

out2 = d.fetchall()
# print(out2)

# ------ 3 ------
e     = db.cursor()
query = 'insert into karyawan (nama) values (%s)'
data  = ('Toni',)
# e.execute(query, data)
# db.commit()

# ------ 4 ------
f     = db.cursor()
query = 'delete from karyawan where nama = %s'
data  = ('Toni',)
f.execute(query, data)
# db.commit()

# ------ 5 ------
g     = db.cursor()
query = 'update karyawan set nama = %s where nama = %s'
data  = ('Hani', 'Ani')
g.execute(query,data)
# db.commit()

# ------ 6 ------
h     = db.cursor()
query = 'update karyawan set nama = %s, gaji = %s where id_kar = %s'
data  = ('Zizi', 20000000, 5)
h.execute(query,data)
# db.commit()

# ------ 7 ------
i     = db.cursor()
query = 'alter table karyawan add column hobby varchar(255)'
i.execute(query)
# db.commit()