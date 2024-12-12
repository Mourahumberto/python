from flask import request
from flask_restful import Resource, reqparse
from models.produtos import Product
from sql_alchemy import db


class Home(Resource):
    def get(self):
        
        return {'produtos' : [produto.json() for produto in Product.query.all()]} #SELECT * FROM users

class Produto1(Resource):
    argumentos = reqparse.RequestParser()

    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' canot left blank")
    argumentos.add_argument('preco')

    def get(self, id):
        produto = Product.find_by_id(id)
        if produto:
            return produto.json()
        return {"message":"Product id '{}' not exists." .format(id)}, 400
    def post(self,id):
        produto = Product.find_by_id(id)
        if produto:
            return {"message":"Product id '{}' alredy exists." .format(id)}, 400
        dados = Produto1.argumentos.parse_args()
        product = Product(id,**dados)
        db.session.add(product)
        db.session.commit()
        product1 = Product.query.filter_by(id=id).first()
        return {'produto' : product1.json()}
    def delete(self,id):
        produto = Product.find_by_id(id)
        if not produto:
            return {"message":"Product id '{}' not exists." .format(id)}, 400
        product1 = Product.query.filter_by(id=id).first()
        db.session.delete(product1)
        db.session.commit()
        return {'usuario' : product1.json()}
    def put(self,id):
        produto = Product.find_by_id(id)
        if not produto:
            return {"message":"Product id '{}' not exists." .format(id)}, 400
        product1 = Product.find_by_id(id)
        dados = Produto1.argumentos.parse_args()
        product1.nome=dados.nome
        product1.preco=dados.preco
                
        db.session.add(product1)
        db.session.commit()

        return {'usuario' : product1.json()}


class Produto2(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('nome', type=str, required=True, help="The field 'nome' canot left blank")


    def get(self):
        args = Produto2.parser.parse_args()
        nome1 = args['nome']
        produto = Product.query.filter_by(nome=nome1).first()
#        produto = Product.find_by_name(args['nome'])
        if produto:
            return produto.json()
        return {"message":"Product id '{}' not exists." .format(id)}, 400