from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.user import Users, User, UserRegister, UserLogin, UserLogout
from resources.site import Site, Sites
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from config import *
from sql_alchemy import banco

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER}:{PASSWD}@{HOST}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True
app.config['JWT_SECRET_KEY'] = {JWT_SECRET_KEY}
app.config['JWT_BLACKLIST_ENABLED'] = True
banco.init_app(app)
api = Api(app)
jwt = JWTManager(app)

@app.route("/")
def index():
    return '<h1>Bem vindo a API!</h1>'

@app.before_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Users, '/usuarios')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Sites, '/sites')
api.add_resource(Site, '/sites/<string:url>')

