$ pip install virtualenv
crie um ambiente virtual
$ virtualenv ambflaskalc
$ source ambflaskalc/bin/activate

para desativar
$ deactivate

instalando as bibliotecas
$ pip install Flask
$ pip install Flask-Restful
$ pip install -U Flask-SQLAlchemy

1) Acessando o shell
$ export FLASK_APP=app
$ flask shell

2) Criando e deletando a tabela no bd usando o flask shell

>>> db.drop_all()
>>> db.create_all()

3) criando user dentro da tabela.
>>> from app import db, Student
>>> student_john = Student(firstname='john', lastname='doe',
                       email='jd@example.com', age=23,
                       bio='Biology student')
>>> sammy = Student(firstname='Sammy',
               lastname='Shark',
               email='sammyshark@example.com',
               age=20,
               bio='Marine biology student')

>>> carl = Student(firstname='Carl',
               lastname='White',
               email='carlwhite@example.com',
               age=22,
               bio='Marine geology student')

>>> db.session.add(sammy)
>>> db.session.add(carl)
>>> db.session.commit()

4) verificando usuário que ainda está na memória.
>>> student_john
>>> student_john.firstname
>>> student_john.bio

4.1)printando o id
>>> print(student_john.id)
A resposta é "None" pelo fato que ainda não foi para o banco e não tem essa var

5) adicionando ao bd
>>> db.session.add(student_john)
>>> db.session.commit()

6) Alterando um user
>>> netin = Student.query.filter_by(firstname="Neto").first()
>>> netin.firstname="humberto"
>>> db.session.add(netin)
>>> db.session.commit()

7) fazendo queries

>>> Student.query.all()
>>> Student.query.filter_by(firstname='Sammy').all() # tras uma list
>>> Student.query.filter_by(firstname='Sammy').first() # tras um student
>>> Student.query.filter_by(id=3).first()
forma simples de trazer a forma primária
>>> Student.query.get(3)

DOC referencia (https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)
DOC referencia 

tipos de query
Student.query.<tab>
