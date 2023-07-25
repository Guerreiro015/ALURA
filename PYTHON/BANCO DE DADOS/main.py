from tkinter import*
from tkinter import Tk, StringVar, ttk

#cores

cor0 = "#2e2d2b" # Preta
cor1 = "#feffff" # Branca
cor2 = "#4fa882" # Verde
cor3 = "#38576b" #  - Valor
cor4 = "#403d3d" #  - Letra
cor5 = "#e06636" #  - profit
cor6 = "#038cfc" # Azul
cor7 = "#3fbfb9" # Verde
cor8 = "#263238" # + Verde
cor9 = "#e9edf5" # + Verde

# Criando janela

janela = Tk()
janela.title("")
janela.geometry("900x600")
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

janela.mainloop()

# Criando frames

frameCima = Frame(janela,width=1043, height=303, bg=cor1, relief=FLAT)
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela,width=1043, height=50, bg=cor1, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=0, padx=0, sti)
frameMeio = Frame






