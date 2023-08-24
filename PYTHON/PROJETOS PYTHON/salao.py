import os
os.system('cls')

import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry

import sqlite3

janela= tkinter.Tk()
janela.title('Salão de Beleza')
#janela.geometry('400x300')
frame = tkinter.Frame(janela)
frame.pack()

frame1 = tkinter.LabelFrame(frame, text = 'Informações do Cliente')
frame1.grid(row=0,column=0,padx=10,pady=10)


nome_label = tkinter.Label(frame1,text='Nome do Cliente')
nome_label.grid(row=0,column=0)
cpf_label = tkinter.Label(frame1,text='CPF: ')
cpf_label.grid(row=0,column=1)
tel_label = tkinter.Label(frame1,text='Telefone')
tel_label.grid(row=0,column=2)

nome_entry = tkinter.Entry(frame1)
nome_entry.grid(row=1,column=0)
cpf_entry = tkinter.Entry(frame1)
cpf_entry.grid(row=1,column=1)
tel_entry = tkinter.Entry(frame1)
tel_entry.grid(row=1,column=2)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=15,pady=10)

frame2 = tkinter.LabelFrame(frame,text='Dados do Serviço')
frame2.grid(row=1,column=0,padx=10,pady=10)

nome_label = tkinter.Label(frame2,text='Nome do Cliente')
nome_label.grid(row=0,column=0)
cpf_label = tkinter.Label(frame2,text='CPF: ')
cpf_label.grid(row=0,column=1)
tel_label = tkinter.Label(frame2,text='Telefone')
tel_label.grid(row=0,column=2)


nome_entry = tkinter.Entry(frame2)
nome_entry.grid(row=1,column=0)
cpf_entry = tkinter.Entry(frame2)
cpf_entry.grid(row=1,column=1)
tel_entry = tkinter.Entry(frame2)
tel_entry.grid(row=1,column=2)


for widget in frame2.winfo_children():
    widget.grid_configure(padx=15,pady=10)






janela.mainloop()



