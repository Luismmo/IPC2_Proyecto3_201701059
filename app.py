from flask import Flask, jsonify, request

#el parametro 'name' sirve para que al aplicacion sepa si está siendo ejecutada desde un archivo principal o está siendo importada
#busca los templates, static files (archivos html) etc
app = Flask(__name__)

from products import products
"""rutas en flask:
dominio/ruta | www.google.com/search
 
decorador-(@app.route('/'))"""
@app.route('/') #creando una ruta y la estamos ligando a una función 
def index(): # una ruta extiende la funcionalidad de una función 
    return 'Hola mundo'

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})
"""
get para obtener
post para guardar en base de datos
put para actualizar 
delete para eliminar
LOS METODOS TRABAJAN POR DEFECTO CON GET 
"""
@app.route('/products', methods = ['GET'])
def getProducts():
    return jsonify(products)
    #return jsonify({"products":products}) #retornar con una propiedad 
    #return jsonify({"products":products, "message": "Products list"}) #retornar con una propiedad 

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name']==product_name]
    if len(productsFound)>0:
        return jsonify({'product': productsFound[0]})
    else: 
        jsonify({"message":"Product not found"})

@app.route('/products', methods = ['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message":"Producto agregado con exito", "products": products})

@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound)>0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message":"Product updated",
            "Product": productFound[0]
        })
    else:
        return jsonify({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound)>0:
        products.remove(productFound[0])
        return jsonify({
            "message":"Product deleted",
            "Product": products
        })
    else:
        return jsonify({"message": "Product not found"})



if __name__ == '__main__':
    app.run(debug=True, port= 4000)