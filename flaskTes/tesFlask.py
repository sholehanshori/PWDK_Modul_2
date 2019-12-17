#  ------------------------ Selasa, 17 Desember 2019 -----------------------------------

# install Flask
# pip install flask

from flask import Flask, send_from_directory, abort, jsonify, render_template

server = Flask(__name__)

# home route
@server.route('/')
def home():
    return '<h1> Welcome to my server </h1>'

# ----------------------------------------------------------------------------------
# render route
@server.route('/html')
def html():
    return render_template('html.html')
# Untuk membuka file html, 'http://127.0.0.1:5000/html'

# ----------------------------------------------------------------------------------
# send data from flask, render html
@server.route('/data')
def data():
    nama = "Andi"
    kota = "Jakarta"
    return render_template(
        'data.html',
        data = {'name' : nama, 'city' : kota}
    )

# ----------------------------------------------------------------------------------
Employees = [
    {"id":1, "nama":"Andi", "usia": 20, "kota":"Jakarta"},
    {"id":2, "nama":"Budi", "usia": 21, "kota":"Jakarta"},
    {"id":3, "nama":"Caca", "usia": 22, "kota":"Jakarta"},
    {"id":4, "nama":"Dani", "usia": 21, "kota":"Jakarta"},
    {"id":5, "nama":"Elis", "usia": 25, "kota":"Jakarta"}
]

# route response json
@server.route('/karyawan')
def karyawan():
    return jsonify(Employees)

# ----------------------------------------------------------------------------------
# dynamic route: karyawan/1
@server.route('/karyawan/<int:id>')
def employees(id):
    if id-1 > len(Employees)-1 or id < 1:
        abort(404)
    else:
        return jsonify(Employees[id-1])

# ----------------------------------------------------------------------------------
# Render static file :  storage
@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)

# ----------------------------------------------------------------------------------
# Error handling: route untuk error 404
@server.errorhandler(404)
def notFound(error):
    return render_template('error.html')
    #  atau '<h1> Sorry cant fulfill your request >_< </h1>'

# ----------------------------------------------------------------------------------
if __name__== '__main__':
    server.run(
        debug = True,
        host  = 'localhost',
        port  = 5000
    )


## LATIHAN ##
# [ 1.] Biodata data (CV) html => server Flask
# - Home
# - About
# - Education
# - Skills
# - Experience

# [ 2.] Response:
# - /table => HTML tabel data digidb
# - /json  => JSON data digimon