import os
os.system("cls")

from tkinter import*
from tkinter import Tk, StringVar, ttk

#cores

co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" #  - Valor
co4 = "#403d3d" #  - Letra
co5 = "#e06636" #  - profit
co6 = "#038cfc" # Azul
co7 = "#3fbfb9" # Verde azulado
co8 = "#263238" # Preto claro
co9 = "#e9edf5" #  Branco cinza claro

# Criando janela

janela = Tk()
janela.title("CONTROLE DE INVENTARIO")
janela.geometry("900x600")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#janela.mainloop()

# Criando frames

frameCima = Frame(janela,width=1043, height=50, bg=co1, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

frameMeio = Frame(janela,width=1043, height=300, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

frameBaixo = Frame(janela,width=1043, height=303, bg=co1, relief=FLAT)
frameBaixo.grid(row=2,column=0, pady=0, padx=1, sticky=NSEW)

janela.mainloop()







