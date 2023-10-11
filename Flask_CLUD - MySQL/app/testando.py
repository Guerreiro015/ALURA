from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
#pip install mysql-connector-python
#pip install mysql.connector  
import mysql.connector
import sys
import sqlite3 as lite

import os
os.system('cls')


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lucas@0108',
    database='jogoteca'
)
cursor=conexao.cursor()
conexao.commit() # Quando edita/grava/deleta - banco de dados



#DELETE
busca='i[0]'
def excluir_usuario(i):    
    comando = f'DELETE FROM usuarios WHERE nome = "{i}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
excluir_usuario(busca)

  
#READ
def visualizar_usuarios():   
    comando=f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados

    print(resultado)
visualizar_usuarios()    


cursor.close()
conexao.close()

            #excluir_jogos(('11',))