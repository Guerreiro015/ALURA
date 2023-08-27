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
janela.title('EMPRESA FICTICIA')
#janela.geometry('800x600')
janela.configure(background='#F0F8FF')
frame = tkinter.Frame(janela)
frame.pack()

frame1 = tkinter.LabelFrame(frame, text = 'Informações do Cliente',font=' ivy 10 bold')
frame1.grid(row=0,column=0,padx=10,pady=5)


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


cep_label=tkinter.Label(frame1,text='Digite o número do CEP:')
cep_label.grid(row=2,column=0)
cep_entry=tkinter.Entry(frame1,bg='#F0F8FF')
cep_entry.grid(row=2,column=1)



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
        codigo=str(cep_entry.get())
        # print(codigo)
        # print(xxx3.get())
        r = requests.get(f'https://viacep.com.br/ws/{codigo}/json/')
        dados = r.json() 

     
        rua_entry.delete(0,'end')
        bairro_entry.delete(0,'end')
        cidade_entry.delete(0,'end')
        estado_entry.delete(0,'end')
        ddd_entry.delete(0,'end')
        cep_entry.delete(0,'end')

        rua_entry.insert(0,dados["logradouro"])
        bairro_entry.insert(0,dados["bairro"])
        cidade_entry.insert(0,dados["localidade"])
        estado_entry.insert(0,dados["uf"])
        ddd_entry.insert(0,dados["ddd"])
        ce1=codigo[:5]
        ce2=codigo[5:]
        cep_entry.insert(0, (ce1,'-',ce2))
        
            
    except:
        messagebox.showerror('CEP NÃO EXISTE','O Cep Digitado não é Valido')
        

xxx4=tkinter.Button(frame1,text='Consultar CEP:',bg='#F0F8FF',command=cep)
xxx4.grid(row=2,column=2)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)

    #-------------------------------------------------------------------

frame2 = tkinter.LabelFrame(frame,text='Dados do Serviço',font=' ivy 10 bold')
frame2.grid(row=2,column=0,padx=10,pady=5)

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

comissao_label=tkinter.Label(frame2,text='Valor Comissão:')
comissao_label.grid(row=2,column=3)
comissao_entry=tkinter.Entry(frame2)
comissao_entry.grid(row=3,column=3)

def valor_parcela():
 try:
    if valor_entry.get()=='':
        va=0
        
    else:
        va=float(valor_entry.get())
        

    if comissao_percentual_entry.get() == '':
        por=0
    else:
        por=float(comissao_percentual_entry.get())

    prestacao=va/int(parcelas_spinbox.get())
    valor_parcela_entry.delete(0,'end')
    valor_parcela_entry.insert(0,f'R$:  {prestacao:,.2f}')
   
    comissao=va*por/100
    comissao_entry.delete(0,'end')
    comissao_entry.insert(0,f'R$:  {comissao:,.2f}')
 except:  
     messagebox.showerror(' É sério? você digitou letra ?', 'Os valores tem que ser números')

valor_parcela_label=tkinter.Button(frame2,text='Valor das parcela',command=valor_parcela,border=4,)
valor_parcela_label.grid(row=2,column=2)
valor_parcela_entry=tkinter.Entry(frame2)
valor_parcela_entry.grid(row=3,column=2)


forma_pag_label=tkinter.Label(frame2,text='Forma de Pagamento')
forma_pag_label.grid(row=0,column=4)
forma_pag_entry=ttk.Combobox(frame2,values=['Pix','Dinheiro','Débito','Crédito','Fiado','Cortesia da casa'])
forma_pag_entry.grid(row=1,column=4)


def cadastro():
# try:
     no=nome_entry.get()
     cp=cpf_entry.get()
     te=tel_entry.get()
     em=email_entry.get()
     ca=cad_entry.get()
     ce=cep_entry.get()
     ru=rua_entry.get()
     nu=numero_entry.get()
     ba=bairro_entry.get()
     ci=cidade_entry.get()
     uf=estado_entry.get()
     dd=ddd_entry.get()
     se=servico_entry.get()
     da=data_servico_entry.get()
     va=valor_entry.get()
     pa=parcelas_spinbox.get()
     vp=valor_parcela_entry.get()
     co=comissao_percentual_entry.get()
     cco=comissao_entry.get()
     fo=forma_pag_entry.get()  

     lista = (no,cp,te,em,ca,ce,ru,nu,ba,ci,uf,dd,se,da,va,pa,vp,co,cco,fo) 
     x=0
     for i in lista:
       if i == "":
         x += 1

     if x > 0:
            messagebox.showerror('Errro','Preencha todos os dados e tente novamente') 
     else:  
            # Create Table
            conn = sqlite3.connect('salao.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS salao_base 
            (nome TEXT, cpf TEXT, tel TEXT, email TEXT, cadastro TEXT, cep TEXT, 
            rua TEXT, numero TEXT, bairro TEXT, cidade TEXT, uf TEXT, ddd TEXT, servico TEXT, d_servico TEXT,
            valor FLOAT,q_parcela FLOAT, parcela FLOAT, com FLOAT, comissao FLOAT, forma TEXT)'''
                    
            conn.execute(table_create_query)
                    
            # Insert Data
            insert_query = '''INSERT INTO salao_base 
                            (nome , cpf , tel , email , cadastro , cep,
                            rua , numero, bairro ,cidade ,uf ,ddd ,servico ,d_servico ,
                            valor ,q_parcela , parcela ,com , comissao, forma ) VALUES 
                            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )'''
            
            # insert_tuple = (no,cp,te,em,ca,ce,ru,nu,ba,ci,uf,dd,se,da,va,pa,vp,co,cco,fo)
            # cursor = conn.cursor()

            x=int(pa)
            y = int(pa)
            for i in range(0,x):
                
                insert_tuple = (no,cp,te,em,ca,ce,ru,nu,ba,ci,uf,dd,se,da,va,pa,vp,co,cco,fo)
                cursor = conn.cursor()

                cursor.execute(insert_query, insert_tuple)
                conn.commit()

                if y > 1:
                   y = y - 1
                   pa=float(y)
                   
            conn.close()    
            
            messagebox.showinfo('Sucesso ','Os dados foram inseridos com sucesso')
  #except:
     messagebox.showerror('Errro','Verifique os dados e tente novamente')
          

def limpar():
     nome_entry.delete(0,'end')
     cpf_entry.delete(0,'end')
     tel_entry.delete(0,'end')
     email_entry.delete(0,'end')
     cad_entry.delete(0,'end')
     cep_entry.delete(0,'end')
     rua_entry.delete(0,'end')
     numero_entry.delete(0,'end')
     bairro_entry.delete(0,'end')
     cidade_entry.delete(0,'end')
     estado_entry.delete(0,'end')
     ddd_entry.delete(0,'end')
     servico_entry.delete(0,'end')
     data_servico_entry.delete(0,'end')
     valor_entry.delete(0,'end')
     parcelas_spinbox.delete(0,'end')
     valor_parcela_entry.delete(0,'end')
     comissao_percentual_entry.delete(0,'end')
     comissao_entry.delete(0,'end')
     forma_pag_entry.delete(0,'end')


salvar_botao=tkinter.Button(frame2,command=cadastro,text='Salvar Dados',font='ivy 8 bold',border=4,bg='#7FFFD4')
salvar_botao.grid(row=2,column=5,pady=10)

limpar_botao=tkinter.Button(frame2,command=limpar,text='Limpar Dados',font='ivy 8 bold',border=4,bg='#7FFFD4')
limpar_botao.grid(row=3,column=5,pady=10)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#---------------------------------------------------------


#-------------------------------------------------------------------------------------------------
con = sqlite3.connect('salao.db')
def visualizar():   
      lista_itens = []
      with con:
        #conn = sqlite3.connect('salao.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM salao_base")
        rows = cur.fetchall()
        for row in rows:
             lista_itens.append(row)
        return lista_itens
     
#----------------------------------------------------------------------

frame3 = tkinter.LabelFrame(frame)
frame3.grid(row=3,column=0,padx=10,pady=5)

def mostrar():
    visualizar()
    tabela_head = ['NOME','CPF',  'TELEFONE','E-Mail', 'SERVIÇO','DATA SERVIÇO', 'VALOR SERVICO','PARCELAS','VALOR DAS PARCELAS','COMISSÕES %','VALOR COMISSÕES']
    #0,1,2,3,12,13,14,15,16
    tree = ttk.Treeview(frame3, selectmode='extended',columns=tabela_head, show="headings",height=10)
    # ( tree é o nome da tabela) --------------------------
    # vertical scrollbar -- Barra de rolagem
    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)

    # horizontal scrollbar -- Barra de rolagem
    hsb = ttk.Scrollbar(frame3, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew',padx=5,pady=5)
    vsb.grid(row=0,column=1, sticky='ns')
    hsb.grid(row=1,column=0, sticky='ew')
    frame3.grid_rowconfigure(0, weight=5)
    frame3.grid_columnconfigure(0, weight=9)
    

    hd=["sw","sw","sw","sw","sw","center","center","center","center","center",'center']
    h=[130,80,80,100,130,120,100,80,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title().upper(), anchor=SW)
        # ajusta a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    lista_itens = visualizar()
   # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)



mostrar()

janela.mainloop()



