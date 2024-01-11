import os

USER = os.environ.get("USER")
PASSWD = os.environ.get("PASSWD")
DATABASE = os.environ.get("DATABASE")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
PORT = '5432'
HOST = 'localhost'

# aqui colocaria no .bashrc ou em algum lugar como variável de ambiente.
