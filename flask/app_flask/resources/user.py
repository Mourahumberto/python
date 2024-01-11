from flask_restful import Resource, reqparse
from models.user import UserModel
from secrets import compare_digest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from blacklist import BLACKLIST
# from werkzeug.security import compare_

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' it's necessary")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' it's necessary")

class Users(Resource):
    def get(self):
        return {'usuarios' : [user.json() for user in UserModel.query.all()]} #SELECT * FROM users

class User(Resource): 
    # /usuarios/{user_id}
    def get(self, user_id):
        if UserModel.find_user(user_id):
            user = UserModel.find_user(user_id)
            return user.json()
        return {"message": "User id '{}' not exists." .format(user_id)}, 400
    
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except: 
                return{'message': 'An internal error ocurred trying to delete user.'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404
    
class UserRegister(Resource):

    # /cadastro
    def post(self):
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
            print("teste")
            return {"message": "The login '{}' alredy exists".format(dados['login'])}
        user = UserModel(**dados)
        user.save_user()
        return{"message": "User created successfully!"}, 201
    
class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])
        
        if user and compare_digest(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token' :token_de_acesso}, 200
        return{'message': 'The username or passowerd is incorrect'}

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully!'}, 200