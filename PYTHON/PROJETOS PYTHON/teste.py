import os
os.system('cls')

import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
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

janela = tkinter.Tk()
janela.title('EMPRESA FICTICIA')
janela.geometry('600x400')
janela.configure(background='#F0F8FF')
frame = tkinter.Frame(janela)
frame.pack()

frame1 = tkinter.LabelFrame(frame, text = 'Informações do Cliente',font=' ivy 10 bold')
frame1.grid(row=0,column=0,padx=10,pady=5)


nome_label = tkinter.Label(frame1,text='Nome do Cliente')
nome_label.grid(row=0,column=0,pady=0)
data_entry = DateEntry(frame1)
data_entry.grid(row=1,column=0,)
def calculo():
    valor=data_entry.get()
    print(valor)
    valor1=datetime.strptime(valor,'%d/%m/%Y').date()
    val=timedelta(30)
    valor2=(valor1+val)
    valor3=datetime.strftime(valor2,'%d/%m/%Y')
    valu=valor[3:5]
    print(valor3)
    print(valu)
    
    d = valor + relativedelta(months=1)
    print(d)

bot=tkinter.Button(frame1,text='Calcular data',command=calculo)
bot.grid(row=3,column=0)


janela.mainloop()