from flask import Flask, make_response, request, json, jsonify
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = "This is an INSECURE secret!! DO NOT use this in production!",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@delivery_db/delivery',
))

models.init_app(app)
models.create_table(app)

@app.route('/myService/hello')
def hello():
    return 'Hello, welcome to my service API\n'

@app.route('/api/detail', methods=['POST'])
def post_create():
#recup
    name = request.form['name']
    seller = request.form['seller']
    price = request.form['price']

    item = models.Delivery()
    item.name = name
    item.seller = seller
    item.price = price

    models.db.session.add(item)
    models.db.session.commit()

    response = jsonify({'message': 'Delivery added', 'delivery': item.to_json()})

    return response

@app.route('/api/get_detail', methods=['GET'])
def delivery():

    data = []

    for row in models.Delivery.query.all():
               data.append(row.to_json())

    response = jsonify(data)

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


