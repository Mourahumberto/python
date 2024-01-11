from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from models.site import SiteModel
from flask_jwt_extended import jwt_required
from resources.filtros import normalize_path_params, consulta_sem_cidade, consulta_com_cidade
import psycopg2
from config import *
   
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str, location='values')
path_params.add_argument('estrelas_min',type=float, location='values')
path_params.add_argument('estrelas_max',type=float, location='values')
path_params.add_argument('diaria_min',type=float, location='values')
path_params.add_argument('diaria_max',type=float, location='values')
path_params.add_argument('limit',type=float, location='values')
path_params.add_argument('offset',type=float, location='values')

    
class Hoteis(Resource):
    def get(self):
        
        connection = psycopg2.connect(user=USER, password=PASSWD, host=HOST, port=PORT, database=DATABASE )
        cursor = connection.cursor()
        dados = path_params.parse_args()
       
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos)
        #mais uma forma de fazer consulta no dicionário
        if not parametros.get('cidade'):
            tupla = tuple([parametros[chave] for chave in parametros])
            cursor.execute(consulta_sem_cidade, tupla)
            resultado = cursor.fetchall()
            
        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            cursor.execute(consulta_com_cidade, tupla)
            resultado = cursor.fetchall()
            
        hoteis = []
        if resultado:
            for linha in resultado:
                hoteis.append({
                'hotel_id' : linha[0],
                'nome': linha[1],
                'estrelas': linha[2],
                'diaria': linha[3],
                'cidade': linha[4],
                'site_id': linha[5]
                })
            print("saindo")
        return {'hoteis' : hoteis} #SELECT * FROM hoteis

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' canot left blank")
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    argumentos.add_argument('site_id', type=int, required=True, help="Every hotel needs to be linked with a site")
    
    
    def get(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            hotel = HotelModel.find_hotel(hotel_id)
            return hotel.json()
        return {"message": "Hotel id '{}' not exists." .format(hotel_id)}, 400
    
    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists." .format(hotel_id)}, 400
        
        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        if not SiteModel.find_by_id(dados.get('site_id')):
            return {'message': 'The hotel must be associated to a valide site id.'}, 400
        try:
            hotel.save_hotel()
        except: 
            return{'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json()
    
    @jwt_required() 
    def put(self, hotel_id):    
        dados = Hotel.argumentos.parse_args()
        hotel2 = HotelModel.find_hotel(hotel_id)
        if hotel2:
            hotel2.update_hotel(**dados)
            try:
                hotel2.save_hotel()
            except: 
                return{'message': 'An internal error ocurred trying to save hotel.'}, 500
            return hotel2.json(), 200
        hotel2 = HotelModel(hotel_id, **dados)
        hotel2.save_hotel()
        return hotel2.json(), 201
    
    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except: 
                return{'message': 'An internal error ocurred trying to delete hotel.'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404