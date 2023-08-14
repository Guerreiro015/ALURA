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
janela.geometry("1000x600")
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


frameCima = Frame(janela,width=1043, height=30, bg=co8, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

texto_cima= Label(frameCima, text='  TABELAS DE IMPOSTO DE RENDAS e INSS ', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)

frameMeio = Frame(janela,width=1043, height=280, bg=co2, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

framebaixo = Frame(janela,width=1043, height=303, bg=co3,pady=20, relief=FLAT)
framebaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)



l_salario = Label(frameMeio, text='  TABELA DE INSS  ', font=('verdana 13 bold'),bg=co3,fg=co1)
l_salario.place(x=350,y=0)
l_insalu = Label(frameMeio, text='  Salário de Contribuição', font=('verdana 11 bold'),bg=co2,fg=co3)
l_insalu.place(x=335,y=25)

base_de1=0
base_de2=1320.01
base_de3=2427.36
base_de4=3641.04
base_ate1=1320
base_ate2=2571.29
base_ate3=3856.94
base_ate4=7507.49
ali1 = 7.50
ali2 = 9.00
ali3 = 12.0
ali4 = 14.0
dedu1 = 0
dedu2 = 19.8
dedu3 = 96.94
dedu4 = 174.08


teto_inss = 876.95
l_texto_titulo = Label(frameMeio, text=f'    Alíquota           Dedução ', font=('verdana 8 bold'),bg=co3,fg=co1)
l_texto_titulo.place(x=720,y=50)
l_texto_titulo = Label(frameMeio, text=f'R$: {base_de1: ,.2F}            até       R$: {base_ate1: ,.2F}                    {ali1: ,.2f}%                R$: {dedu1: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
l_texto_titulo.place(x=490,y=70)
l_texto_titulo = Label(frameMeio, text=f'R$: {base_de2: ,.2F}    até       R$: {base_ate2: ,.2F}                    {ali2:,.2f}%                 R$: {dedu2: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
l_texto_titulo.place(x=490,y=90) 
l_texto_titulo = Label(frameMeio, text=f'R$: {base_de3: ,.2F}    até       R$: {base_ate3: ,.2F}                    {ali3:,.2f}%               R$: {dedu3: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
l_texto_titulo.place(x=490,y=110)
l_texto_titulo = Label(frameMeio, text=f'R$: {base_de4: ,.2F}    até       R$: {base_ate4: ,.2F}                    {ali4:,.2f}%               R$: {dedu4: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
l_texto_titulo.place(x=490,y=130)
l_texto_titulo = Label(frameMeio, text=f'Teto Máximo de desconto de INSS... : R$: {teto_inss: .2f}', font=('verdana 7 bold'),bg=co3,fg=co1)
l_texto_titulo.place(x=490,y=150)

l_pericu = Label(frameMeio, text='  De', font=('verdana 10 bold'),bg=co2,fg=co1)
l_pericu.place(x=50,y=50)
l_pericu = Label(frameMeio, text='  Até ', font=('verdana 10 bold'),bg=co2,fg=co1)
l_pericu.place(x=150,y=50)
l_pericu = Label(frameMeio, text=' Alíquota ', font=('verdana 10 bold'),bg=co2,fg=co1)
l_pericu.place(x=230,y=50)
l_pericu = Label(frameMeio, text='  Dedução ', font=('verdana 10 bold'),bg=co2,fg=co1)
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
l_salario.place(x=350,y=0)
l_insalu = Label(framebaixo, text=' Base de Cálculo de IRRF ', font=('verdana 11 bold'),bg=co3,fg=co1)
l_insalu.place(x=335,y=25)

l_pericu = Label(framebaixo, text='  De', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=50,y=50)
l_pericu = Label(framebaixo, text='  Até ', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=150,y=50)

l_pericu = Label(framebaixo, text=' Alíquota ', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=230,y=50)
l_pericu = Label(framebaixo, text='Parc. Deduzir', font=('verdana 10 bold'),bg=co3,fg=co1)
l_pericu.place(x=330,y=50)

dependente = 189.59
deducao_simplicada = 528.00

base_deir1=0.0
base_deir2=2112.01
base_deir3=2826.66
base_deir4=3751.06
base_deir5=4664.68


base_ateir1=2112
base_ateir2=2826.65
base_ateir3=3751.05
base_ateir4=4664.68
base_ateir5=100000000

aliir1 = 0.0
aliir2 = 7.5
aliir3 = 15.0
aliir4 = 22.5
aliir5 = 27.5


deduir1 = 0
deduir2 = 158.40
deduir3 = 370.40
deduir4 = 651.73
deduir5 = 884.96


l_texto_titulo = Label(framebaixo, text=f'Alíquota          Parc. Deduzir ', font=('verdana 8 bold'),bg=co5,fg=co1)
l_texto_titulo.place(x=730,y=50)
l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir1: ,.2F}            até       R$: {base_ateir1: ,.2F}                    {aliir1: ,.2f}%                R$: {deduir1: ,.2F}', font=('verdana 7 '),bg=co3,fg=co1)
l_texto_titulo.place(x=490,y=70)
l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir2: ,.2F}    até       R$: {base_ateir2: ,.2F}                    {aliir2:,.2f}%                 R$: {deduir2: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
l_texto_titulo.place(x=490,y=90) 
l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir3: ,.2F}    até       R$: {base_ateir3: ,.2F}                    {aliir3:,.2f}%               R$: {deduir3: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
l_texto_titulo.place(x=490,y=110)
l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir4: ,.2F}    até       R$: {base_ateir4: ,.2F}                    {aliir4:,.2f}%               R$: {deduir4: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
l_texto_titulo.place(x=490,y=130)
l_texto_titulo = Label(framebaixo, text=f'         Acima  de  R$: {base_deir5: ,.2F}                                 {aliir5:,.2f}%               R$: {deduir5: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
l_texto_titulo.place(x=490,y=150)

l_pericu = Label(framebaixo, text=f'Dedução Por Dependente ...............: R$: {dependente: .2f}', font=('verdana 8 bold'),bg=co5,fg=co1)
l_pericu.place(x=490,y=180)
l_pericu = Label(framebaixo, text=f'Base de DEDUÇÃO SIMPLIFICADA...:  R$: {deducao_simplicada: .2f}', font=('verdana 8 bold'),bg=co5,fg=co1)
l_pericu.place(x=490,y=200)





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
# ate5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
# ate5.place(x=130,y=150)
ali5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
ali5.place(x=230,y=150)
par5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
par5.place(x=330,y=150)






janela.mainloop()