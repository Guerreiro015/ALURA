import os
os.system("cls")

#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas
# x = coluna
# y = Linha

# Vamos ver algumas configurações de estilo mais comuns que podemos definir:
# Width – Largura do widget;
# Height – Altura do widget;
# Text – Texto a ser exibido no widget;
# Font – Família da fonte do texto;
# Fg – Cor do texto do widget;
# Bg – Cor de fundo do widget;
# Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).

# n, ne, e, se, s, sw, w, nw, or center
o0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Azul
co4 = "#403d3d" # cinza
co5 = "#e06636" # laranja
co6 = "#038cfc" # Azul claro
co7 = "#3fbfb9" # Verde azulado
co8 = "#263238" # Preto claro
co9 = "#e9edf5" # Branco cinza claro

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
# importando os outros arquivos
from view import *



# Criando janela------------------------------

janela = Tk()
janela.title("Encargos com folha de pagamento")
janela.geometry("900x600")
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


frameCima = Frame(janela,width=1043, height=30, bg=co8, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

texto_cima= Label(frameCima, text='  TABELAS DE IMPOSTO DE RENDAS e INSS ', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)

frameMeio = Frame(janela,width=1043, height=280, bg=co7, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

framebaixo = Frame(janela,width=1043, height=303, bg=co3,pady=20, relief=FLAT)
framebaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)



l_salario = Label(frameMeio, text='  TABELA DE INSS  ', font=('verdana 13 bold'),bg=co7,fg=co1)
l_salario.place(x=150,y=0)
l_insalu = Label(frameMeio, text='  Salário de Contribuição', font=('verdana 11 bold'),bg=co7,fg=co3)
l_insalu.place(x=135,y=25)

l_pericu = Label(frameMeio, text='  DE', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pericu.place(x=50,y=50)
l_pericu = Label(frameMeio, text='  ATÉ ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pericu.place(x=150,y=50)
l_pericu = Label(frameMeio, text=' Áliquota ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pericu.place(x=230,y=50)
l_pericu = Label(frameMeio, text='Parcela P/ Deduzir', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pericu.place(x=330,y=50)





de1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
de1.place(x=30,y=70)
ate1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ate1.place(x=130,y=70)
ali1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ali1.place(x=230,y=70)
par1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
par1.place(x=330,y=70)

de2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
de2.place(x=30,y=90)
ate2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ate2.place(x=130,y=90)
ali2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ali2.place(x=230,y=90)
par2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
par2.place(x=330,y=90)

de3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
de3.place(x=30,y=110)
ate3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ate3.place(x=130,y=110)
ali3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ali3.place(x=230,y=110)
par3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
par3.place(x=330,y=110)

de4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
de4.place(x=30,y=130)
ate4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ate4.place(x=130,y=130)
ali4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
ali4.place(x=230,y=130)
par4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
par4.place(x=330,y=130)




l_salario = Label(framebaixo, text='  TABELA DE IRRF  ', font=('verdana 13 bold'),bg=co3,fg=co1)
l_salario.place(x=150,y=0)
l_insalu = Label(framebaixo, text=' Base de Cálculo de IRRF ', font=('verdana 11 bold'),bg=co3,fg=co1)
l_insalu.place(x=135,y=25)

l_pericu = Label(framebaixo, text='  DE', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=50,y=50)
l_pericu = Label(framebaixo, text='  ATÉ ', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=150,y=50)
l_pericu = Label(framebaixo, text=' Áliquota ', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=230,y=50)
l_pericu = Label(framebaixo, text='Parcela P/ Deduzir', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=330,y=50)

dependente = 189.59
deducao_simplicada = 528.00
l_pericu = Label(framebaixo, text=f'Dedução Por Dependente .......... ... : R$: {dependente: .2f}', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=30,y=180)
l_pericu = Label(framebaixo, text=f'Base de DEDUÇÃO SIMPLIFICADA...:  R$: {deducao_simplicada: .2f}', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=30,y=200)





de1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
de1.place(x=30,y=70)
ate1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ate1.place(x=130,y=70)
ali1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ali1.place(x=230,y=70)
par1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
par1.place(x=330,y=70)

de2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
de2.place(x=30,y=90)
ate2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ate2.place(x=130,y=90)
ali2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ali2.place(x=230,y=90)
par2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
par2.place(x=330,y=90)

de3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
de3.place(x=30,y=110)
ate3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ate3.place(x=130,y=110)
ali3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ali3.place(x=230,y=110)
par3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
par3.place(x=330,y=110)

de4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
de4.place(x=30,y=130)
ate4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ate4.place(x=130,y=130)
ali4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ali4.place(x=230,y=130)
par4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
par4.place(x=330,y=130)

de5= Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
de5.place(x=30,y=150)
ate5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ate5.place(x=130,y=150)
ali5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ali5.place(x=230,y=150)
par5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
par5.place(x=330,y=150)






janela.mainloop()