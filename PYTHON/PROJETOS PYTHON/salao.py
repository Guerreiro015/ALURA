import os
os.system('cls')
import requests

import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
import requests
from tkinter import*
from tkinter import messagebox



import sqlite3

janela= tkinter.Tk()
janela.title('Empresa Ficticia')
#janela.geometry('800x400')
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
email_label.grid(row=0,column=3)
email_entry=tkinter.Entry(frame1)
email_entry.grid(row=1,column=3)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)


frame2=tkinter.LabelFrame(frame,text="Dados Endereço:")
frame2.grid(row=1,column=0)

xxx1=tkinter.Label(frame2,text='CEP:')
xxx1.grid(row=0,column=1)
xxx3=tkinter.Entry(frame2)
xxx3.grid(row=0,column=2)



rua_label = tkinter.Label(frame2,text='Rua:')
rua_label.grid(row=1,column=0)
rua_entry = tkinter.Entry(frame2)
rua_entry.grid(row=2, column=0)


numero_label = tkinter.Label(frame2,text='Número:')
numero_label.grid(row=1,column=1)
numero_entry = tkinter.Entry(frame2)
numero_entry.grid(row=2, column=1)

bairro_label = tkinter.Label(frame2,text='Bairro:')
bairro_label.grid(row=1,column=2)
bairro_entry = tkinter.Entry(frame2)
bairro_entry.grid(row=2, column=2)

cidade_label = tkinter.Label(frame2,text='Cidade:')
cidade_label.grid(row=1,column=3)
cidade_entry = tkinter.Entry(frame2)
cidade_entry.grid(row=2, column=3)

estado_label = tkinter.Label(frame2,text='Estado:')
estado_label.grid(row=3,column=0)
estado_entry = tkinter.Entry(frame2)
estado_entry.grid(row=4, column=0)

uf_label = tkinter.Label(frame2,text='UF:')
uf_label.grid(row=3,column=1)
uf_entry = tkinter.Entry(frame2)
uf_entry.grid(row=4, column=1)

codigo=str('04760060')
print(codigo)
b=str(xxx3.get())
print(b)

def cep():
    print(b)
    r = requests.get(f'https://viacep.com.br/ws/{codigo}/json/')
    dados = r.json() 

    #try:
    print(dados) 
    rua_entry.delete(0,'end')
    bairro_entry.delete(0,'end')
    cidade_entry.delete(0,'end')
    estado_entry.delete(0,'end')
    uf_entry.delete(0,'end')

    rua_entry.insert(0,dados["logradouro"])
    bairro_entry.insert(0,dados["bairro"])
    cidade_entry.insert(0,dados["localidade"])
    estado_entry.insert(0,dados["uf"])
    uf_entry.insert(0,dados["uf"])
            
    #except:
        # messagebox.showerror('CEP NÃO É VÁLIDO')
        # print('erro')

xxx4=tkinter.Button(frame2,text='Consultar CEP:',bg='Blue',fg='Yellow',command=cep)
xxx4.grid(row=0,column=0)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=5)

frame3 = tkinter.LabelFrame(frame,text='Dados do Serviço')
frame3.grid(row=2,column=0,padx=20,pady=10)

servico_label = tkinter.Label(frame3,text='Tipo de Servico')
servico_label.grid(row=0,column=0)
servico_entry=tkinter.Entry(frame3)
servico_entry.grid(row=1,column=0)

atendente_label = tkinter.Label(frame3,text='Atendente: ')
atendente_label.grid(row=0,column=1)
atendente_entry = tkinter.Entry(frame3)
atendente_entry.grid(row=1,column=1)

data_servico_label = tkinter.Label(frame3,text='Data do Servico')
data_servico_label.grid(row=0,column=2)
data_servico_entry =  tkinter.Entry(frame3)
data_servico_entry.grid(row=1,column=2)

valor_label = tkinter.Label(frame3,text='Data do Servico',width=17)
valor_label.grid(row=0,column=3)
valor_entry = DateEntry(frame3)
valor_entry.grid(row=1,column=3)

for widget in frame3.winfo_children():
    widget.grid_configure(padx=10,pady=5)




janela.mainloop()



