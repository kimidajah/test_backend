# flask microfw
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
mysql = MySQL()
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'backendtest'

mysql.init_app(app)

class Products (Resource):
    def get(self):
        try:
            sql = mysql.connection.cursor()
            sql.execute("""SELECT * FROM products""")
            products = sql.fetchall()
            result = jsonify(products=products)
            result.status_code = 200
            return (result)
        except Exception as err:
            print(err)
            result = jsonify('failed to fecth....')
            result.status_code = 400
            return (result)
        finally:
            sql.close()
    def post(self):
        try:
            sql = mysql.connection.cursor()
            _nama = request.form['nama']
            _deskripsi = request.form['deskripsi']
            create_product = """INSERT INTO products (nama, deskripsi) VALUES (%s, %s)"""
            sql.execute(create_product, (_nama, _deskripsi))
            mysql.connection.commit()
            result = jsonify(data="produc berhasil di tambahkan!")
            result.status_code = 200 
            return(result)
        except Exception as err:
            print(err)
            result = jsonify(data="produc gagal di tambahkan!")
            result.status_code = 400 
            return(result)
        finally:
            sql.close()

    
api.add_resource(Products, '/products', endpoint="products")
app.run(host="localhost", port="3200")