import os
os.system("cls")

#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas
# x = coluna
# y = Linha

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

texto_cima= Label(frameCima, text='  CÁLCULO DE  ---   IRRF - INSS - FGTS', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)

frameMeio = Frame(janela,width=1043, height=300, bg=co7, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

framebaixo = Frame(janela,width=1043, height=303, bg=co3,pady=20, relief=FLAT)
framebaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)










meio_salario = Label(frameMeio, text='  Valor do salário bruto', font=('verdana 10 bold'),bg=co7,fg=co1)
meio_salario.place(x=0,y=0)
meio_faltas= Label(frameMeio, text='  Valor das faltas', font=('verdana 10 bold'),bg=co7,fg=co1)
meio_faltas.place(x=0,y=30)
meio_depe= Label(frameMeio, text='  Quant. de depenndentes ', font=('verdana 10 bold'),bg=co7,fg=co1)
meio_depe.place(x=0,y=60)
meio_pensao= Label(frameMeio, text='  Pensão Alimentícia', font=('verdana 10 bold'),bg=co7,fg=co1)
meio_pensao.place(x=0,y=90)

e_salario = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_salario.place(x=200,y=0)
e_faltas = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_faltas.place(x=200,y=30)
e_depe = Entry(frameMeio,width=10,justify=LEFT,relief=SOLID)
e_depe.place(x=200,y=60)
e_pensao = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_pensao.place(x=200,y=90)

imagem=Image.open("baseir.png")
imagem = imagem.resize((300,260))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frameMeio, image = imagem,bg=co1,fg=co4)
l_imagem.place(x=550,y=0)



campos = [e_salario,e_faltas,e_depe,e_pensao]
def calculo():
    for i in campos:
         if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    messagebox.showinfo('Sucesso', 'Cálculo executado com sucesso')

def deletar():
   try:

    e_salario.delete(0, 'end')
    e_faltas.delete(0, 'end')
    e_depe.delete(0, 'end')
    e_pensao.delete(0, 'end')
   
    messagebox.showinfo('Sucesso', 'Os dados foram limpos com sucesso')
 
    
   except IndexError:
    messagebox.showerror('Erro', 'Seleciona um dos dados na tabela') 

l_botao = Button(frameMeio,command=calculo,width=15,text="CALCULAR".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 12 bold"),bg=co1,fg=co4)
l_botao.place(x=130,y=230)
l_botao = Button(frameMeio,command=deletar,width=15,text="LIMPAR".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 12 bold"),bg=co1,fg=co4)
l_botao.place(x=130,y=170)

baixo_salario = Label(framebaixo, text='  BASE DO INSS', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_salario.place(x=0,y=0)
baixo_faltas= Label(framebaixo, text='  BASE DO IRRF', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_faltas.place(x=0,y=30)
baixo_depe= Label(framebaixo, text='  BASE DO FGTS ', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_depe.place(x=0,y=60)
baixo_pensao= Label(framebaixo, text='  Pensão Alimentícia', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_pensao.place(x=0,y=90)


            
    # base_salario = e_salario-e_faltas
    # e_base = Label(framebaixo, base_salario, font=('verdana 10 bold'),bg=co7,fg=co1)
    # e_base.place(x=200,y=0)

janela.mainloop()