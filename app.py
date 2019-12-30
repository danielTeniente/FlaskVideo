from flask import Flask
#conexión con la base de datos
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='Esto es un secreto'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/video.db'

db=SQLAlchemy(app)

from controlador import *

if __name__=='__main__':
    app.run(debug=True)