from flask_restful import Resource

class Carros(Resource):
    def get(self):
        return "Carros"