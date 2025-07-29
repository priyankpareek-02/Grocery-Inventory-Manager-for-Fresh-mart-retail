from flask import Flask, request, jsonify, render_template
from products_dao import get_all_products, add_product, update_product, delete_product, get_low_stock_products
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(get_all_products())

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    add_product(data['name'], data['quantity'], data['price_per_unit'])
    return jsonify({'message': 'Product added successfully'})

@app.route('/products/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    update_product(id, data['name'], data['quantity'], data['price_per_unit'])
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    delete_product(id)
    return jsonify({'message': 'Product deleted successfully'})

@app.route('/products/low-stock', methods=['GET'])
def low_stock_products():
    threshold = request.args.get('threshold', default=5, type=int)
    return jsonify(get_low_stock_products(threshold))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
