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
    password='Lucasluana@0108',
    database='jogoteca'
)
cursor=conexao.cursor()
conexao.commit() # Quando edita/grava/deleta - banco de dados


dados=('Romeu','Rome','123')
nom=('Romeu')
nick=('gato')
sen=('123')
dados=f'("{nom}","{nick}","{sen}")'
print(dados)

def inserir_usuarios(i):
        comando =f'INSERT INTO usuarios(nome,nickname,senha) VALUES("i")'
        cursor.execute(comando)
        conexao.commit() # Quando edita/grava/deleta - banco de dados
inserir_usuarios(dados)


  
def visualizar_jogos():   
        #READ
    comando=f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados

    print(resultado)
visualizar_jogos()    


cursor.close()
conexao.close()

            #excluir_jogos(('11',))