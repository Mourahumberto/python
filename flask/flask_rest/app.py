from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
pessoa = {
    'nome': "default",
    'cpf': "default"
}
parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Rate to charge for this resource')
parser.add_argument('endereco', type=str, help='Rate to charge for this resource')
parser.add_argument('idade', type=str, help='Rate to charge for this resource')
parser.add_argument('cpf', type=str, help='Rate to charge for this resource')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class TodoSimple(Resource):
    def get(self):
        return "I'm GET"
    def put(self):
        return "I'M PUT"
    #curl http://localhost:5000/testemethod  -X PUT

class ArgmSimple(Resource):

    def get(self, id):
        return "I'm GET"
    def put(self,id):
        args = parser.parse_args()
        print(id)
        pessoa['nome'] = args['nome']
        pessoa['cpf'] = args['cpf']
        print(pessoa)
        return pessoa

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/testmethod')
api.add_resource(ArgmSimple, '/testargm/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)