$ pip install virtualenv
crie um ambiente virtual
$ virtualenv ambvir
$ source ambvir/bin/activate

para desativar
$ deactivate

instalando as bibliotecas
$ pip install Flask
$ pip install Flask-Restful

criando requeriments
$ pip freeze > requirements.txt

instalando as mesmas dependencias que estão no requeriments.txt
pip install -r requeriments.txt