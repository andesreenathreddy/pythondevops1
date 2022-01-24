from flask import Flask, render_template, jsonify, abort, request

from model import products, save_products

app = Flask(__name__)


# http://localhost:3000/api/products
@app.route('/api/v1/products')  # this is decorator
def productList():
    return jsonify(products)


@app.route('/api/products/<int:index>')  # this is decorator
def productByIndex(index):
    try:
        return jsonify(products[index])
    except IndexError:
        abort(404)


@app.route('/api/products', methods=['POST'])  # this is decorator
def addNewProduct():
    product = request.json
    products.append(product)
    return jsonify(products)
