from sql_alchemy import db
import time
class Product(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    preco = db.Column(db.String(120), nullable=False)

    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco= preco
    
    def json(self):
        return {
            'product_id' : self.id,
            'nome': self.nome
        }
    
    @classmethod
    def find_by_id(cls, id):
        
        produto = cls.query.filter_by(id=id).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if produto:
            return produto
        return None