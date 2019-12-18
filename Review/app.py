#  ------------------------ Rabu, 18 Desember 2019 -----------------------------------

from flask import request, redirect, jsonify, Flask, render_template
app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('home.html')

@app.route('/home')
def home():
    return redirect('/')

x = [
    {'no': 1, 'nama': 'Andi'},
    {'no': 2, 'nama': 'Budi'},
    {'no': 3, 'nama': 'Caca'}
]

@app.route('/data')
def data():
    return jsonify(x)

@app.route('/data/<int:no>')
def nodata(no):
    return jsonify(x[no-1])

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        body = request.json
        print(body['kota'])
        return jsonify({
            'status': 'Data sukses terkirim',
            'kota': body['kota']
        })
    else:
        return 'Anda request selain GET & POST'

# Buka postman pilih 'Body', 'raw', jenis text 'Json'

if __name__ == '__main__':
    app.run(debug=True)