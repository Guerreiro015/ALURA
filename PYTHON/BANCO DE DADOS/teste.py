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


frameCima = Frame(janela,width=1043, height=50, bg=co8, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

texto_cima= Label(frameCima, text='  TABELAS DE IMPOSTO DE RENDAS e INSS ', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)

frameMeio = Frame(janela,width=1043, height=330, bg=co7, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

framebaixo = Frame(janela,width=1043, height=303, bg=co3,pady=20, relief=FLAT)
framebaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)



l_salario = Label(frameMeio, text='  TABELA DE INSS  ', font=('verdana 13 bold'),bg=co7,fg=co1)
l_salario.place(x=0,y=0)
l_insalu = Label(frameMeio, text='  Insalubridade', font=('verdana 10 bold'),bg=co7,fg=co1)
l_insalu.place(x=0,y=25)
l_pericu = Label(frameMeio, text='  Periculosidade', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pericu.place(x=0,y=50)
l_he = Label(frameMeio, text='  Horas Extras ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_he.place(x=0,y=75)
l_adno = Label(frameMeio, text='  Adicional Noturno ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_adno.place(x=0,y=100)
l_dsr = Label(frameMeio, text='  DSR  - (H.E - Adic.Notur) ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_dsr.place(x=0,y=125)
l_outros = Label(frameMeio, text='  Outros Proventos  ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_outros.place(x=0,y=150)


e_insalu = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_insalu.place(x=200,y=25)
e_pericu = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_pericu.place(x=200,y=50)
e_he = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_he.place(x=200,y=75)
e_adno = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_adno.place(x=200,y=100)
e_dsr = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_dsr.place(x=200,y=125)
e_outros = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_outros.place(x=200,y=150)
e_salario = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_salario.place(x=200,y=175)


e_faltas = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_faltas.place(x=200,y=225)
e_depe = Entry(frameMeio,width=10,justify=LEFT,relief=SOLID)
e_depe.place(x=200,y=250)
e_pensao = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_pensao.place(x=200,y=275)




campos = [e_salario,e_insalu,e_pericu,e_he,e_adno,e_dsr,e_faltas,e_depe,e_pensao,e_outros]

def atualizar():
    
    try:
        for i in campos:
            if i.get() == '':
                messagebox.showinfo('Erro', 'Preencha todos os campos')
                return
        sal = float(e_salario.get())
        ins = float(e_insalu.get())
        per = float(e_pericu.get())
        hex = float(e_he.get())
        adn = float(e_adno.get())
        ds = float(e_dsr.get())
        fal = float(e_faltas.get())
        pen = float(e_pensao.get())
        dep = float(e_depe.get())
        out = float(e_outros.get()) 
        
    except:
            messagebox.showerror('Erro', 'Por favor Verifique, A entrada de dados contém ERROS') 


janela.mainloop()