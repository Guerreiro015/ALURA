import os
os.system('cls')

Co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Azul
co4 = "#403d3d" # cinza
co5 = "#e06636" # laranja
co6 = "#038cfc" # Azul claro
co7 = "#3fbfb9" # Verde azulado
co8 = "#263238" # Preto claro
co9 = "#e9edf5" # Branco cinza claro
co10 = '#ffff00' # amarelo
co11 = '#ce0018' # Vermelho
co12 = '#106b21' # Verde
co13 = '#fc9303' # Laranja
co14 = '#5a005a' # roxo

import requests

import tkinter
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from datetime import timedelta
from datetime import *
from datetime import datetime
from dateutil import relativedelta

import requests
import sqlite3

conn = sqlite3.connect('salao.db')
global tree
global treev_lista

janela = tkinter.Tk()
janela.title('EMPRESA FICTÍCIA')
janela.geometry('1000x650')
janela.configure(background='#F0F8FF')
janela.resizable(width=FALSE, height=FALSE)
frame = tkinter.Frame(janela)
frame.pack()

style = ttk.Style(janela)
style.theme_use('clam')


#-------------------------------------------------------------------------------------------------
conn = sqlite3.connect('salao.db')
def visualizar():   
      lista_itens = []
      with conn:
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM salao_base")
        rows = cur.fetchall()
        for row in rows:
             lista_itens.append(row)
        return lista_itens
     
#----------------------------------------------------------------------

frame1 = tkinter.LabelFrame(frame,bg='bisque',fg='green',font='ivy 8 ')
frame1.grid(row=3,column=0,padx=10,pady=5)

def mostrar():
    global tree
    visualizar()
    tabela_head = ['INDICE','NOME','CPF','TELEFONE','E-MAIL','CADASTRO','CEP','RUA','NÚMERO','BAIRRO','CIDADE','UF',
                   'DDD','SERVIÇO','DATA SERVIÇO', 'Vlr. SERVICO','Quant. PARCELAS','Vlr. PARCELAS','% COMISSÃO','Vlr. COMISSÃO','FORMA DE PG']
    
    tree = ttk.Treeview(frame1, selectmode='extended',columns=tabela_head, show="headings",height=10)
    # ( tree é o nome da tabela) --------------------------

    # ajusta a largura da coluna para a string do cabeçalho
    for i in tabela_head:
        tree.column(i,anchor='center', width=43)
        tree.heading(i, text= i)

    # vertical scrollbar -- Barra de rolagem
    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)

    # horizontal scrollbar -- Barra de rolagem
    hsb = ttk.Scrollbar(frame3, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(row=0,column=1, sticky='ns')
    hsb.grid(row=1,column=0, sticky='ew')
    frame3.grid_rowconfigure(0, weight=5)
    frame3.grid_columnconfigure(0, weight=5)
    
    
    
    lista_itens = visualizar()
   # inserindo os itens dentro da tabela
        
    for item in lista_itens:
    
        tree.insert('', 'end', values=item)

mostrar()





janela.mainloop()



