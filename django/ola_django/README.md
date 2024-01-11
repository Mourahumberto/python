Criando o projeto.
$ virtualenv --python=$(which python3.11) venv
$ pip install django
$ django-admin startproject project .

Subindo o servidor
$ python3 manage.py runserver