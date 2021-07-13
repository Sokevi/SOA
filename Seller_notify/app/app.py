from flask import Flask, make_response, request, json, jsonify
from passlib.hash import sha256_crypt
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = "This is an INSECURE secret!! DO NOT use this in production!",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@notify_db/notify',
))

models.init_app(app)
models.create_table(app)

@app.route('/myService/hello')
def hello():
    return 'Hello, welcome to my service API\n'

@app.route('/api/add_delivery', methods=['POST'])
def post_register(): 

    product = request.form['product']
    quantite = request.form['quantite']
    code = request.form['code']
    
    notify = models.Notify()
    
    notify.product = product
    notify.quantite = quantite
    notify.code = code

    models.db.session.add(notify)
    models.db.session.commit()

    response = jsonify({'message': 'Notifify added', 'result': notify.to_json()})

    return response

@app.route('/api/get_delivery', methods=['GET'])
def get_notifiy():
    data = []
    for row in models.Notify.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)