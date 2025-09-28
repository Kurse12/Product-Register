from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

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
