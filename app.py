from flask import Flask, render_template, request, redirect, url_for
import db as dbase
from product import Product


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_product")
def add_product():
    return "Add Product Page"

@app.route("/edit_products")
def edit_products():
    return "Edit Products Page"

@app.route("/delete_products")
def delete_products():
    return "Delete Products Page"

if __name__ == "__main__":
    
    app.run(port=5000, debug=True)
