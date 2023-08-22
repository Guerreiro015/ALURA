import os
os.system("cls")

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
#"sn": must be n, ne, e, se, s, sw, w, nw, or center
# imprtando os outros arquivos
from view import *
co0 = "#2e2d2b" # Preta
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

janela = Tk()
janela.title("TESTANDO COMO É FEITO UM COMBOBOX -> Caixa de seleção <-")
janela.geometry("600x300")

l_nome = Label(janela,width=15, height=2,text = 'Faça sua escolha',font=("ivy 10 bold"),anchor='center')
l_nome.grid(row=0,column=0,padx=5,pady=5,sticky=NSEW)

combo=Combobox(janela)

combo['values'] = (1,2,3,'Antonio','Luana')
combo.grid(row=1,column=0,padx=5,pady=5,sticky=NSEW)

def obter():
    resul=combo.get()
    if resul == 'Luana':
        print ('Minha Filhota')
    else:
        print (resul)
    print ('MInha Filhota')  if resul == 'Luana' else  print(resul)

botao = Button(janela,width=12, height=1,command=obter,text = 'Ver Resposta',font=("Arial 10 bold"),anchor='center',bg=co14,fg=co1)
botao.grid(row=3,column=0,padx=5,pady=5)

janela.mainloop()

