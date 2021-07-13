from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from passlib.hash import sha256_crypt

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db

def create_table(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine

class Notify(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(255), unique=False, nullable=True)
    quantite = db.Column(db.String(255), nullable=True)
    code = db.Column(db.String(255), nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'product': self.product,
            'quantite': self.quantite,
            'code': self.code,
        }