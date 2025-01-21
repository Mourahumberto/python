from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sql_alchemy import db
from resources.produtos import Home, Produto1, Produto2
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import timedelta

app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
# usado quando é localhopst/ app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@localhost:5432/produtodb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@db:5432/produtodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_strong_secret_key'
app.config["JWT_SECRET_KEY"] = 'your_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)


# db.init_app(app)
jwt = JWTManager(app)
class Login(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "test" or password != "test":
            return {"message":"Bad username or password" }

        access_token = create_access_token(identity=username)
        return {"access_token": access_token}
#@app.before_request
#def cria_banco():
#    db.create_all()

api.add_resource(Login, '/login')
api.add_resource(Home, '/')
api.add_resource(Produto1, '/produto/<string:id>')
api.add_resource(Produto2, '/produtoname/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
