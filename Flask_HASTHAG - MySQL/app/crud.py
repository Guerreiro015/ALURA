from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
#pip install mysql-connector-python
#pip install mysql.connector  
import mysql.connector


#app = Flask(__name__) #instanciando Flask
  
#app.secret_key = 'alura'

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lucasluana@0108',
    database='jogoteca'

)

cursor=conexao.cursor()

conexao.commit() # Quando edita/grava/deleta - banco de dados
#resultado = cursor.fetchall() # ler banco de dados

nome='re5'
categoria='zumbi'
console='ps4'
ano='2006'

comando =f'INSERT INTO jogos(nome,categoria,console,ano) VALUES("{nome}","{categoria}","{console}","{ano}")'
cursor.execute(comando)




cursor.close()
conexao.close()






#app.run(debug=True)

    

  # trecho da app
#app.run(host='0.0.0.0', port=8080)
