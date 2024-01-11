from flask import Flask
from flask_restful import Api
from sql_alchemy import db
from resources.produtos import Home, Produto1

app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@localhost:5432/produtodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

    
@app.before_request
def cria_banco():
    db.create_all()

api.add_resource(Home, '/')
api.add_resource(Produto1, '/produto/<string:id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
