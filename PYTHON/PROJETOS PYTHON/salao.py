import os
os.system('cls')
import requests

import tkinter
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date


import requests
import sqlite3

janela = tkinter.Tk()
janela.title('Empresa Ficticia')
#janela.geometry('800x600')
frame = tkinter.Frame(janela)
frame.pack()

frame1 = tkinter.LabelFrame(frame, text = 'Informações do Cliente')
frame1.grid(row=0,column=0,padx=20,pady=5)


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

cad_label=tkinter.Label(frame1,text='Data do Cadastro')
cad_label.grid(row=0,column=4)
cad_entry=DateEntry(frame1)
cad_entry.grid(row=1,column=4)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)


xxx1=tkinter.Label(frame1,text='Digite o número do CEP:')
xxx1.grid(row=2,column=1)
xxx3=tkinter.Entry(frame1,width=15)
xxx3.grid(row=2,column=2)



rua_label = tkinter.Label(frame1,text='Rua:')
rua_label.grid(row=3,column=0)
rua_entry = tkinter.Entry(frame1,width=28)
rua_entry.grid(row=4, column=0)


numero_label = tkinter.Label(frame1,text='Número:')
numero_label.grid(row=3,column=1)
numero_entry = tkinter.Entry(frame1,width=10)
numero_entry.grid(row=4, column=1)

bairro_label = tkinter.Label(frame1,text='Bairro:')
bairro_label.grid(row=3,column=2)
bairro_entry = tkinter.Entry(frame1)
bairro_entry.grid(row=4, column=2)

cidade_label = tkinter.Label(frame1,text='Cidade:')
cidade_label.grid(row=3,column=3)
cidade_entry = tkinter.Entry(frame1)
cidade_entry.grid(row=4, column=3)

estado_label = tkinter.Label(frame1,text='Estado:')
estado_label.grid(row=3,column=4)
estado_entry = tkinter.Entry(frame1,border=5,justify=CENTER)
estado_entry.grid(row=4, column=4)

ddd_label = tkinter.Label(frame1,text='DDD:')
ddd_label.grid(row=3,column=5)
ddd_entry = tkinter.Entry(frame1,width=10,border=5,justify=CENTER) # Justify(center,left,right)
ddd_entry.grid(row=4, column=5)



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
        xxx1=tkinter.Label(frame1,text=f'CEP:  {ce1}-{ce2}')
        xxx1.grid(row=0,column=3)
            
    except:
        messagebox.showerror('CEP NÃO EXISTE','O Cep Digitado não é Valido')
        

xxx4=tkinter.Button(frame1,text='Consultar CEP:',bg='#3fbfb9',command=cep)
xxx4.grid(row=2,column=0)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)

frame2 = tkinter.LabelFrame(frame,text='Dados do Serviço')
frame2.grid(row=2,column=0,padx=20,pady=5)

servico_label = tkinter.Label(frame2,text='Servico Executado')
servico_label.grid(row=0,column=0)
servico_entry=tkinter.Entry(frame2,width=30)
servico_entry.grid(row=1,column=0)

data_servico_label = tkinter.Label(frame2,text='Data do Servico')
data_servico_label.grid(row=0,column=1)
data_servico_entry = DateEntry(frame2)
data_servico_entry.grid(row=1,column=1)

atendente_label = tkinter.Label(frame2,text='Atendente: ')
atendente_label.grid(row=0,column=2)
atendente_entry = tkinter.Entry(frame2,width=25)
atendente_entry.grid(row=1,column=2)

comissao_percentual_label = tkinter.Label(frame2,text='Comissão %: ')
comissao_percentual_label.grid(row=0,column=3)
comissao_percentual_entry = tkinter.Entry(frame2,width=10)
comissao_percentual_entry.grid(row=1,column=3)


valor_label = tkinter.Label(frame2,text='Valor do Servico')
valor_label.grid(row=2,column=0)
valor_entry = tkinter.Entry(frame2)
valor_entry.grid(row=3,column=0)

parcela_label=tkinter.Label(frame2,text='Quant. Parcelas')
parcela_label.grid(row=2,column=1)
parcelas_spinbox=tkinter.Spinbox(frame2,from_=1,to='infinity',width=5)
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
    valor_parcela=tkinter.Label(frame2,text=f'R$: {prestacao:,.2f}',width=15)
    valor_parcela.grid(row=3,column=2)
    comissao=va*por/100
    valor_comissao=tkinter.Label(frame2,text=f'R$:  {comissao:,.2f}')
    valor_comissao.grid(row=3,column=3)

valor_parcela_label=tkinter.Button(frame2,text='Valor das parcela',command=valor_parcela,border=4,)
valor_parcela_label.grid(row=2,column=2)

comissao_label=tkinter.Label(frame2,text='Comissão:')
comissao_label.grid(row=2,column=3)

forma_pag_label=tkinter.Label(frame2,text='Forma de Pagamento')
forma_pag_label.grid(row=0,column=4)
forma_pag_entry=ttk.Combobox(frame2,values=['Pix','Dinheiro','Débito','Crédito','Fiado','Cortesia da casa'])
forma_pag_entry.grid(row=1,column=4)

salvar_botao=tkinter.Button(frame2,text='Salvar Dados',font='Arial,9,bold',border=4,bg='Green')
salvar_botao.grid(row=2,column=5,pady=10)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=5)

def cadastro():

    # Create Table
            conn = sqlite3.connect('salao.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                    registration_status TEXT, num_courses INT, num_semesters INT,parcela FLOAT)
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
            age, nationality, registration_status, num_courses, num_semesters) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title,
                                  age, nationality, registration_status, numcourses, numsemesters,prestacao)
            cursor = conn.cursor()

            x=int(parce)
            for i in range(0,x):
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()
            conn.close()    

            # firstname.delete(0,'end')
            # lastname.delete(0,'end')
            # title.delete(0,'end')
            # age.delete(0,'end')
            # nationality.delete(0,'end')
            # numcourses.delete(0,'end')
            # numsemesters.delete(0,'end')
            # registration_status.delete(0,'end')



frame3 = tkinter.LabelFrame(frame)
frame3.grid(row=3,column=0,padx=20,pady=5)

def mostrar():
    tabela_head = ['Nome','CPF',  'Telefone','E-mail', 'Serviço','Valor Servico', 'Data Serviço']
    #lista_itens = visualizar()

    tree = ttk.Treeview(frame3, selectmode="extended",columns=tabela_head, show="headings")
    # ( tree é o nome da tabela) --------------------------
    # vertical scrollbar -- Barra de rolagem
    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)

    # horizontal scrollbar -- Barra de rolagem
    hsb = ttk.Scrollbar(frame3, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame3.grid_rowconfigure(0, weight=10)

    hd=["center","center","center","center","center","center","center"]
    h=[100,80,80,80,100,80,80]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajusta a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # lista_itens = visualizar()
    # inserindo os itens dentro da tabela
    # for item in lista_itens:
    #     tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()



