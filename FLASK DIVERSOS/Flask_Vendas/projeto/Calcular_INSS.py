
from flask import Flask, render_template, request, redirect, session,flash,send_from_directory
import mysql
from datetime import *
import time
import sqlite3
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pyodbc
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
#pip install PyMySQL


engine = ce('mysql://root:lucas0108@localhost:3306/base')
bases=declarative_base()
session=sessionmaker(bind=engine)
session=session()


class usuarios(bases):
   __tablename__= "usuarios"

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(45), nullable=False)
   email = Column(String(45), nullable=False)
   empresa = Column(String(45), nullable=False)
   senha = Column(String(45), nullable=False)



app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'


@app.route('/')
def login():    
    return render_template('login.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/cadastro_usuarios')
def cadastro_usuarios():    
    return render_template('cadastro_usuarios.html')

#---------------------------------------------<>--------------------------------------------------   
#---------------------------------------------<>--------------------------------------------------   

@app.route('/calculo')
def calculo():    
    return render_template('calculo.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nome=request.form['nome']    
    senha=request.form['senha']
    usuario=request.form['nome']
    
    dados=session.query(usuarios).all()
    x=0
    for dado in dados:            
       if nome == dado.nome and senha == dado.senha: 
          x=0        
          flash(f'Usuário {usuario} Logado com Sucesso!!')         
          return redirect(url_for('index',dados=dados))           
       else: 
          x +=1           
    if x > 0:
         flash('Não foi possível fazer Login!!')
         return render_template('login.html')
    
#---------------------------------------------<>--------------------------------------------------    

@app.route('/autenticar_cadastro', methods=['POST'])
def autenticar_cadastro():
    nome=request.form['nome']
    email=request.form['email']
    empresa=request.form['empresa']
    senha=request.form['senha']
    senha2=request.form['senha2']

    usuario=request.form['nome']
    dados=session.query(usuarios).all()

    if nome == "" or email == "" or senha == "" or email == "":
        flash('Preencha todos os campos!!')
        return render_template('cadastro_usuarios.html')
    
    if not "@" in email or not ".com" in email:
        flash('E-mail digitado não é válido!!')
        return render_template('cadastro_usuarios.html')

    if nome in dados[0].nome:            
        flash('Usuario já Existe!!')
        return render_template('cadastro_usuarios.html')

    if senha != senha2:
        flash('Senhas não conferem, tente colocar senhas iguais!!')
        return render_template('cadastro_usuarios.html')
    
    
    else:        
        flash(f'Usuário {usuario} cadastrado com Sucesso!!')            
        dados=usuarios(nome=nome, email=email, empresa=empresa, senha=senha, nome=nome) #instanciando
        session.add(dados) #inserindo
        session.commit() # gravando
        flash('Jogo adcionado com Sucesso!!')      
        return redirect(url_for('login',usuario=usuario))

    

    #---------------------------------------------<>--------------------------------------------------   


@app.route('/index')
    #---------------------------------------------<>--------------------------------------------------   
def index():
    dados=session.query(usuarios).all()         

    tit="imposto de renda"
    return render_template('index.html',titulo=tit,dados=dados)

#---------------------------------------------<>--------------------------------------------------   


@app.route('/usuario')
def usuario():
    dados=session.query(usuarios).all()     
    lista = dados

    tit="USUARIOS"
    return render_template('usuarios.html',titulo=tit,usuarios=lista)

#---------------------------------------------<>--------------------------------------------------   

# @app.route('/alterar_jogos/<int:id>')
# def alterar_jogos(): 
#     id=request.form['id']   
#     nome=request.form['nome']
#     email=request.form['email']
#     empresa=request.form['empresa'] 
#     senha=request.form['senha']
    

#     session.query(usuarios).filter(usuario.id==id).update({'nome': nome,'email': email,'empresa': empresa,'senha': senha })
#     session.commit()  
      
#     flash(f'Úsuario {nome} alterado!!')
      
#     return redirect(url_for('index'))
    
#---------------------------------------------<>--------------------------------------------------   

# @app.route('/deletar_jogos/<int:id>')
# def deletar_jogos(id):       
#       session.query(usuario).filter(usuario.id==id).delete()
#       session.commit() 
#       flash(f'Jogo Deletado !!')
#       return redirect(url_for('index'))
    

#---------------------------------------------<>--------------------------------------------------   

@app.route('/logout')
def logout():    
    flash('Usuário Desconectado')
    return redirect(url_for('login'))

#---------------------------------------------<>--------------------------------------------------   


session.close()  

app.run(debug=True)
#app.run(host='0.0.0.0', port=8080)
