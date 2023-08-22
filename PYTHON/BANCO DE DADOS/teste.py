import os
os.system('cls')

import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('alunosbd.db')
table_create_query = '''CREATE TABLE IF NOT EXISTS alunos 
            (nome TEXT, sobrenome TEXT)
            '''
conn.execute(table_create_query)
            
def Inserir():
    n='antonio'
    s='neto'
    data_insert_query = '''INSERT INTO alunos (nome, sobrenome) VALUES 
        (?, ?)'''
    data_insert_tuple = (n,s)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()         

Inserir()