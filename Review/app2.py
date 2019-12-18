#  ------------------------ Rabu, 18 Desember 2019 -----------------------------------

from flask import Flask, jsonify, request, render_template, redirect
import mysql.connector as mc
app = Flask(__name__)


# Menyambung dengan SQL, dimana membuat querry database terlebih dahulu
dbku = mc.connect(
    host = 'localhost',
    user = 'sholeh_as',
    passwd = 'shaolin35',
    database = 'testing'
)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        body = request.form
        x    = dbku.cursor()
        data = (body['nama'], body['usia'])
        sql  = f'insert into datadiri (nama, usia) values {data}'
        x.execute(sql)
        dbku.commit()
        return redirect('/data')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        x     = dbku.cursor()
        x.execute('select * from datadiri')
        hasil = x.fetchall()
        hasil = list(map(lambda i: {'id':i[0], 'nama':i[1], 'usia':i[2]}, hasil))
        print(hasil)
        return jsonify(hasil)
    elif request.method == 'POST':
        body = request.json
        x    = dbku.cursor()
        data = (body['nama'], body['usia'])
        sql  = f'insert into datadiri (nama, usia) values {data}'
        x.execute(sql)
        dbku.commit()
        return 'INI ADALAH POST'

@app.route('/data/<int:no>', methods=['GET', 'PUT', 'DELETE'])   # Variasi bisa dicoba untuk PUT dan DELETE
def datas(no):
    x     = dbku.cursor()
    sql   = f'select * from datadiri where id = {no}'
    x.execute(sql, no)
    hasil = x.fetchall()
    hasil = list(map(lambda i: {'id':i[0], 'nama':i[1], 'usia':i[2]}, hasil))
    print(hasil)
    return jsonify(hasil)


if __name__ == '__main__':
    app.run(debug=True)