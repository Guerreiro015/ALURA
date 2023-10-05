from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
from dadosteca import *



app = Flask(__name__) #instanciando Flask
  

app.secret_key = 'alura'

  

@app.route('/')
def login():
    return render_template('login.html',titulo='LOGIN')

@app.route('/index')
def index():   
    lista_jogos = visualizar_jogos()

    tit="jogos de 2023"
    return render_template('index.html',titulo=tit,jogos=lista_jogos)

@app.route('/buscar_jogos')
def buscar_jogos(): 
    buscar=request.form['busca'] 
    lista_jogos = ver_jogos(buscar)
    if lista_jogos==[]:
       flash('Nenhum jogo para buscar!!')
       return render_template('index.html',titulo=tit,jogos=lista_jogos)

    else:
      tit="Jogos Encontrado"
      return render_template('buscar.html',titulo=tit,jogos=lista_jogos)


@app.route('/novo_jogo')
def novo_jogo():
    return render_template('novo_jogo.html', titulo="novo jogo")


@app.route('/criar', methods=['POST'])
def criar():
   
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    ano=request.form['ano']

    novo_jogo = (nome,categoria,console,ano)
    inserir_jogos(novo_jogo)
    flash('Jogo adcionado com Sucesso!!')
    return redirect(url_for('index'))
 
   

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nome=request.form['nome']
    senha=request.form['senha']

    ver_usuario(nome)
    logar=ver_usuario(nome)
      
    if nome == logar[0] and senha == logar[1]:
         flash('Logado com Sucesso!!')
         return redirect(url_for('index'))
    else:
         flash('Não foi possível fazer Login!!')
         return redirect(url_for('login'))

  
    
@app.route('/logout')
def logout():
    flash('Usuário Desconectado')
    session['usuario_logado'] = None
    return redirect(url_for('login'))




app.run(debug=True)

    

  # trecho da app
#app.run(host='0.0.0.0', port=8080)
