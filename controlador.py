from app import app
from modelos import *
from flask import render_template

@app.route('/')
def index():
    #listas
    usuarios=Usuario.query.all()
    bonos=Bono.query.all()
    usuario_bonos=[]
    for usuario in usuarios:
        total_bono=0
        for bono in bonos:
            if(bono.departamento==usuario.departamento):
                total_bono+=bono.cantidad
        usuario_bonos+=[[usuario.nombre,total_bono]]
    return render_template('index.html',list=usuario_bonos)
