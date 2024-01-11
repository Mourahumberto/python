from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

    def __init__(self, owner, senha):
        self.owner = owner
        self.senha = senha
    
    def json(self):
        return {
            'user_id' : self.id,
            'owner': self.owner
        }

@app.before_request
def cria_banco():
    db.create_all()

def find_user(owner):
    user = User.query.filter_by(owner=owner).first()
    if user:
        return user
    return None
    
@app.route("/usuario", methods=['POST'])
def create():
    data1 = request.json
    owner = data1.get('owner')
    senha = data1.get('senha')
    if find_user(owner) == None:
        user = User(owner=owner, senha=senha) 
        db.session.add(user)
        db.session.commit()
        user1 = User.query.filter_by(owner=owner).first()
        return {'usuario' : user1.json()}
    return 'alredy exist'


@app.route("/usuario", methods=['DELETE'])
def delete():
    data1 = request.json
    owner = data1.get('owner')
    user1 = User.query.filter_by(owner=owner).first()
    db.session.delete(user1)
    db.session.commit()

    return {'usuario' : user1.json()}

@app.route("/")
def index():
    return {'usuarios' : [user.json() for user in User.query.all()]} #SELECT * FROM users

@app.route("/teste", methods=['GET', 'POST'])
def query_example():
    data1 = request.json
    owner = data1.get('owner')

    print(owner)
    return jsonify(data1)