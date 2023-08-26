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
#janela.geometry('800x600')
frame = tkinter.Frame(janela)
frame.pack()

frame1 = tkinter.LabelFrame(frame, text = 'Informações do Cliente')
frame1.grid(row=0,column=0,padx=20,pady=10)


nome_label = tkinter.Label(frame1,text='Nome do Cliente')
nome_label.grid(row=0,column=0,pady=0)
nome_entry = tkinter.Entry(frame1,width=25)
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
email_entry=tkinter.Entry(frame1,width=25)
email_entry.grid(row=1,column=3)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)


frame2=tkinter.LabelFrame(frame,text="Endereço:")
frame2.grid(row=1,column=0,padx=20,pady=10)

xxx1=tkinter.Label(frame2,text='Digite o número do CEP:')
xxx1.grid(row=0,column=1)
xxx3=tkinter.Entry(frame2,width=15)
xxx3.grid(row=0,column=2)



rua_label = tkinter.Label(frame2,text='Rua:')
rua_label.grid(row=1,column=0)
rua_entry = tkinter.Entry(frame2,width=28)
rua_entry.grid(row=2, column=0)


numero_label = tkinter.Label(frame2,text='Número:')
numero_label.grid(row=1,column=1)
numero_entry = tkinter.Entry(frame2,width=10)
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

ddd_label = tkinter.Label(frame2,text='DDD:')
ddd_label.grid(row=3,column=1)
ddd_entry = tkinter.Entry(frame2,width=10)
ddd_entry.grid(row=4, column=1)

cad_label=tkinter.Label(frame2,text='Data do Cadastro')
cad_label.grid(row=3,column=2)
cad_entry=DateEntry(frame2)
cad_entry.grid(row=4,column=2)


def cep():
    try:
        codigo=str(xxx3.get())
        print(codigo)
        print(xxx3.get())
        r = requests.get(f'https://viacep.com.br/ws/{codigo}/json/')
        dados = r.json() 

     
        rua_entry.delete(0,'end')
        bairro_entry.delete(0,'end')
        cidade_entry.delete(0,'end')
        estado_entry.delete(0,'end')
        ddd_entry.delete(0,'end')

        rua_entry.insert(0,dados["logradouro"])
        bairro_entry.insert(0,dados["bairro"])
        cidade_entry.insert(0,dados["localidade"])
        estado_entry.insert(0,dados["uf"])
        ddd_entry.insert(0,dados["ddd"])
        ce1=codigo[:5]
        ce2=codigo[5:]
        xxx1=tkinter.Label(frame2,text=f'CEP:  {ce1}-{ce2}')
        xxx1.grid(row=0,column=3)
            
    except:
        messagebox.showerror('ERRO','O Cep Digitado não é Valido')
        

xxx4=tkinter.Button(frame2,text='Consultar CEP:',bg='#3fbfb9',command=cep)
xxx4.grid(row=0,column=0)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=5)

frame3 = tkinter.LabelFrame(frame,text='Dados do Serviço')
frame3.grid(row=2,column=0,padx=20,pady=10)

servico_label = tkinter.Label(frame3,text='Servico Executado')
servico_label.grid(row=0,column=0)
servico_entry=tkinter.Entry(frame3,width=25)
servico_entry.grid(row=1,column=0)

data_servico_label = tkinter.Label(frame3,text='Data do Servico')
data_servico_label.grid(row=0,column=1)
data_servico_entry = DateEntry(frame3)
data_servico_entry.grid(row=1,column=1)

atendente_label = tkinter.Label(frame3,text='Atendente: ')
atendente_label.grid(row=0,column=2)
atendente_entry = tkinter.Entry(frame3,width=25)
atendente_entry.grid(row=1,column=2)

comissao_percentual_label = tkinter.Label(frame3,text='Percentual Comissão: ')
comissao_percentual_label.grid(row=0,column=3)
comissao_percentual_entry = tkinter.Entry(frame3,width=25)
comissao_percentual_entry.grid(row=1,column=3)


valor_label = tkinter.Label(frame3,text='Valor do Servico')
valor_label.grid(row=2,column=0)
valor_entry = tkinter.Entry(frame3)
valor_entry.grid(row=3,column=0)

parcela_label=tkinter.Label(frame3,text='Quant. Parcelas')
parcela_label.grid(row=2,column=1)
parcelas_spinbox=tkinter.Spinbox(frame3,from_=1,to='infinity',width=5)
parcelas_spinbox.grid(row=3,column=1)


def valor_parcela():

    if valor_entry.get()=='':
        va=0
        
    else:
        va=int(valor_entry.get())
        

    if comissao_percentual_entry.get() == '':
        por=0
    else:
        por=int(comissao_percentual_entry.get())

    prestacao=va/int(parcelas_spinbox.get())
    valor_parcela=tkinter.Label(frame3,text=f'R$: {prestacao:,.2f}',width=15)
    valor_parcela.grid(row=3,column=2)
    comissao=va*por/100
    valor_comissao=tkinter.Label(frame3,text=f'R$:  {comissao:,.2f}')
    valor_comissao.grid(row=3,column=3)

valor_parcela_label=tkinter.Button(frame3,text='Valor das parcela',command=valor_parcela)
valor_parcela_label.grid(row=2,column=2)

comissao_label=tkinter.Label(frame3,text='Comissão:')
comissao_label.grid(row=2,column=3)

for widget in frame3.winfo_children():
    widget.grid_configure(padx=10,pady=5)




janela.mainloop()



