import os
os.system("cls")

#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas
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


frameCima = Frame(janela,width=1043, height=50, bg=co8, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

texto_cima= Label(frameCima, text='  CÁLCULO DE IR E INSS', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)


frameMeio = Frame(janela,width=1043, height=300, bg=co6, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

texto_meio= Label(frameMeio, text='  Cálculo de Imposto de Renda', font=('verdana 10 bold'),bg=co6,fg=co1)
texto_meio.place(x=0,y=0)

frameBaixo = Frame(janela,width=1043, height=303, bg=co3,pady=20, relief=FLAT)
frameBaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)

janela.mainloop()