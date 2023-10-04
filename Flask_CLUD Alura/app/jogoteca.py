from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import dadosteca


def main():
  app = Flask(__name__) #instanciando Flask
  #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogoteca.db' #define um caminho para o arquivo de db, na pasta do projeto

  app.secret_key = 'alura'

  # db = SQLAlchemy(app)

  # connect to database
  con = sqlite3.connect('jogoteca.db', check_same_thread=False)
  
  # create cursor object
  cur = con.cursor()
  

  # class jogos(db.Model): #criando a classe cliente
  #   id = db.Column(db.Integer, primary_key=True) 
  #   nome = db.Column(db.String(100), nullable=False) 
  #   categoria = db.Column(db.String(100), nullable=False)
  #   console = db.Column(db.String(100), nullable=False)
  #   ano = db.Column(db.String(100), nullable=False)

  #   def __repr__(self): #função que retorna seu id sempre que é instanciada
  #     return '<jogos %r>' % self.id




  # class Usuarios(db.Model):
  #    id = db.Column(db.Integer, primary_key=True) 
  #    nickname = db.Column(db.String(20))
  #    nome = db.Column(db.String(20), nullable=False)
  #    senha = db.Column(db.String(100), nullable=False)

  #    def __repr__(self): #função que retorna seu id sempre que é instanciada
  #     return '<usuario %r>' % self.id
                          




  @app.route('/')
  def login():
    return render_template('login.html',titulo='LOGIN')

  @app.route('/index')
  def index():   
    lista_jogos = 'jogos.query.order_by(jogos.id)'

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
          flash('Nenhum Usuário Logado')
          return redirect(url_for('login'))
    else:
          tit="jogos de 2023"
          return render_template('index.html',titulo=tit,jogos=lista_jogos)

  @app.route('/novo_jogo')
  def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:      
          flash('Nenhum Usuário Logado')
          return redirect(url_for('login'))
    else:
          return render_template('novo_jogo.html', titulo="novo jogo")


  @app.route('/criar', methods=['POST'])
  def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    ano=request.form['ano']
    #jogar=jogos(nome,categoria,console,ano)
    #criando novo cliente a partir dos dados
    novo_jogo = '(nome=nome,categoria=categoria, console=console, ano=ano)'
    flash('Jogo adcionado com Sucesso!!')
    # db.session.add(novo_jogo)
    # db.session.commit()
    return redirect(url_for('index'))



  @app.route('/autenticar', methods=['POST'])
  def autenticar():
    nome=request.form['nome']
    dadosteca.ver_usuario(nome)
    usuarios=dadosteca.ver_usuario(nome)
      
    if nome == usuarios:
        print('Table not found!')
    else:
        print('Table found!')


  
    # if nome == usuario:
    #       if request.form['senha'] == usuario.senha:
    #           session['usuario_logado'] = usuario.nome
    #           flash('Usuário '+ usuario.nome + ' logado com sucesso!')
    #           return redirect(url_for('index'))
    #       else:
    #           flash('Usuário não logado.')
    #           return redirect(url_for('login'))
    # else:
    #   flash('Não foi possivel logar.')
    #   return redirect(url_for('login'))

  @app.route('/logout')
  def logout():
    flash('Usuário Desconectado')
    session['usuario_logado'] = None
    return redirect(url_for('login'))




  app.run(debug=True)

if __name__ == '__main__' : # chamada da funcao principal
  main()
    

  # trecho da app
#app.run(host='0.0.0.0', port=8080)
