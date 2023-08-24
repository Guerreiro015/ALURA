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
frame1.grid(row=0,column=0,padx=20,pady=10)


nome_label = tkinter.Label(frame1,text='Nome do Cliente')
nome_label.grid(row=0,column=0,pady=0)
nome_entry = tkinter.Entry(frame1)
nome_entry.grid(row=1,column=0,)

cpf_label = tkinter.Label(frame1,text='CPF: ')
cpf_label.grid(row=0,column=1)
cpf_entry = tkinter.Entry(frame1)
cpf_entry.grid(row=1,column=1)

tel_label = tkinter.Label(frame1,text='Telefone')
tel_label.grid(row=0,column=2)
tel_entry = tkinter.Entry(frame1)
tel_entry.grid(row=1,column=2)

email_label=tkinter.Label(frame1,text='Email')
email_label.grid(row=2,column=0)
email_entry=tkinter.Entry(frame1)
email_entry.grid(row=3,column=0)

inicio_label = tkinter.Label(frame1,text='Data Cadastro')
inicio_label.grid(row=2,column=2)
inicio_entry = DateEntry(frame1)
inicio_entry.grid(row=3, column=2)


for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)

frame2 = tkinter.LabelFrame(frame,text='Dados do Serviço')
frame2.grid(row=1,column=0,padx=20,pady=10)

servico_label = tkinter.Label(frame2,text='Tipo de Servico')
servico_label.grid(row=0,column=0)
servico_entry=tkinter.Entry(frame2)
servico_entry.grid(row=1,column=0)

atendente_label = tkinter.Label(frame2,text='Atendente: ')
atendente_label.grid(row=0,column=1)
atendente_entry = tkinter.Entry(frame2)
atendente_entry.grid(row=1,column=1)

data_servico_label = tkinter.Label(frame2,text='Data do Servico')
data_servico_label.grid(row=0,column=2)
data_servico_entry = DateEntry(frame2)
data_servico_entry.grid(row=1,column=2)


for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=5)






janela.mainloop()



