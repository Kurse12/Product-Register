from tarfile import data_filter
from flask import Flask, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
import db as dbase
from product import Product

#instanciar la conexion a la base de datos
db = dbase.db_connection()

app = Flask(__name__)

app.secret_key = "secret_key"

@app.route("/")
def index():
    products = db['products']
    data = products.find()
    return render_template("index.html", dataProducts = data)

@app.route("/add_product", methods = ["POST"])
def add_product():
    if request.method == "POST":
        products = db['products']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        
        if nombre and precio and cantidad:
            product = Product(nombre, precio, cantidad)
            products.insert_one(product.toDBCollection())
        
        flash('Producto agregado correctamente')
        
        return redirect(url_for("index"))

@app.route("/edit_products/<id>")
def edit_products(id):
    products = db['products']
    data = products.find_one({'_id': ObjectId(id)})
    return render_template('edit_product.html', dataProduct = data)

@app.route("/update_product/<id>", methods=["POST"])
def update_product(id):
    if request.method == "POST":
        products = db['products']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        
    if nombre and precio and cantidad:
        products.update_one({'_id': ObjectId(id)}, {'$set': {
            'nombre': str(nombre),
            'precio': float(precio),
            'cantidad': int(cantidad)
        }})
        flash('Producto actualizado correctamente')
        return redirect(url_for("index"))

@app.route("/delete_product/<string:id>")
def delete_products(id):
    products = db['products']
    products.delete_one({'_id': ObjectId(id)})
    flash('Producto eliminado correctamente')
    return redirect(url_for("index"))

if __name__ == "__main__":
    
    app.run()
