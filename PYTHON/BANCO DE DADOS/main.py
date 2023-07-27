import os
os.system("cls")

from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date


#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas

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

# Criando janela------------------------------

janela = Tk()
janela.title("CONTROLE DE INVENTARIO")
janela.geometry("900x600")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#janela.mainloop()

# Criando frames-------------------------------

frameCima = Frame(janela,width=1043, height=50, bg=co1, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

frameMeio = Frame(janela,width=1043, height=300, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

frameBaixo = Frame(janela,width=1043, height=303, bg=co1,pady=20, relief=FLAT)
frameBaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)

# Preparando a imagem - FrameCima-------------------------------
foto=Image.open("inventario.png")
foto = foto.resize((45,45))
foto = ImageTk.PhotoImage(foto)

foto_logo = Label(frameCima, image = foto, text='  INVENTÁRIO DOMÉSTICO', width=900, compound=LEFT, relief=RAISED, anchor= NW, font=('verdana 20 bold'),bg=co1,fg=co4)
foto_logo.place(x=0,y=0)

# Trabahando no FrameMeio -------------------------------------

l_nome = Label(frameMeio,text="Nome", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_nome.place(x=10,y=10)
e_nome = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)# PODEMOS USAR SOLID OU ("solid")
e_nome.place(x=130,y=11)

l_local = Label(frameMeio,text="Local/Área", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_local.place(x=10,y=40)
e_local = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_local.place(x=130,y=41)

l_descricao = Label(frameMeio,text="Descrição", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_descricao.place(x=10,y=70)
e_descricao = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_descricao.place(x=130,y=71)

l_marca = Label(frameMeio,text="Marca/Modelo", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_marca.place(x=10,y=100)
e_marca = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_marca.place(x=130,y=101)

l_compra = Label(frameMeio,text="Data da Compra", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_compra.place(x=10,y=130)
# CRIANDO UM CALENDARIO-----------------------------------------
e_compra = DateEntry(frameMeio,width=12,BackGround='darkblue',bordwidth=2,year=2023)# Criando um calendario
e_compra.place(x=130,y=131)
#---------------------------------------------------------------------------------------


l_valor = Label(frameMeio,text="Valor da Compra", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_valor.place(x=10,y=160)
e_valor = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_valor.place(x=130,y=161)

l_serie = Label(frameMeio,text="Número de Serie", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_serie.place(x=10,y=190)
e_serie = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_serie.place(x=130,y=191)

#Criando botões --------------------------------------------
l_img_item = Label(frameMeio,text="Imagem do ítem", compound=CENTER,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co0)
l_img_item.place(x=10,y=220)

l_img_item = Button(frameMeio,width=25,text="Imagem do ítem".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_img_item.place(x=130,y=221)


#____________________________________
foto_adicionar = Image.open("Adicionar.png")
foto_adicionar = foto_adicionar.resize((20,20))
foto_adicionar = ImageTk.PhotoImage(foto_adicionar)

foto_atualizar = Image.open("carregar.png")
foto_atualizar = foto_atualizar.resize((20,20))
foto_atualizar = ImageTk.PhotoImage(foto_atualizar)

foto_deletar = Image.open("lixeira.png")
foto_deletar = foto_deletar.resize((20,20))
foto_deletar = ImageTk.PhotoImage(foto_deletar)

foto_ver = Image.open("ver.png")
foto_ver = foto_ver.resize((20,20))
foto_ver = ImageTk.PhotoImage(foto_ver)



# Botão adicionar
l_adicionar = Button(frameMeio,image=foto_adicionar,width=95,text="  Adicionar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_adicionar.place(x=330,y=10)

# Botão Atualizar
l_atualizar = Button(frameMeio,image=foto_atualizar,width=95,text="  Atualizar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_atualizar.place(x=330,y=50)

# Botão Deletar
l_deletar = Button(frameMeio,image=foto_deletar,width=95,text="  Deletar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_deletar.place(x=330,y=90)

# Botão Mostrar
l_ver_item = Button(frameMeio,image=foto_ver,width=95,text="  Ver Ítens".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_ver_item.place(x=330,y=220)


# Frames dos totais
l_total = Label(frameMeio,text="         Valor Total dos Ítens           ",height=2,anchor=NW,font=("ivy 10 bold"),bg=co7,fg=co1)
l_total.place(x=460,y=10)
l_total = Label(frameMeio,text="",width=15, height=1,anchor=CENTER,font=("ivy 17 bold"),bg=co7,fg=co1)
l_total.place(x=460,y=30)


l_quant = Label(frameMeio,text="       Quantidade Total dos Ítens   ", height=2,anchor=NW,font=("ivy 10 bold"),bg=co7,fg=co1)
l_quant.place(x=460,y=110)
l_quant = Label(frameMeio,text="",width=15, height=3,anchor=CENTER,font=("ivy 17 bold"),bg=co7,fg=co1)
l_quant.place(x=460,y=130)

#-----------------------------------------------------------
# tabela -----------------------------------------------------------

# Criando cabeçalo da tabela  duas barras de rolagem with dual scrollbars
tabela_head = [' Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

lista_itens = []

global tree

tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

# vertical scrollbar -- Barra de rolagem
vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

# horizontal scrollbar -- Barra de rolagem
hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameBaixo.grid_rowconfigure(0, weight=12)

hd=["center","center","center","center","center","center","center", 'center']
h=[40,150,100,160,130,100,100, 100]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # ajusta a largura da coluna para a string do cabeçalho
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


# inserindo os itens dentro da tabela
for item in lista_itens:
    tree.insert('', 'end', values=item)


quantidade = [8888,88]

for iten in lista_itens:
    quantidade.append(iten[6])

Total_valor = sum(quantidade)
Total_itens = len(quantidade)

l_total['text'] = f'R$ {Total_valor:,.2f}'
l_quant['text'] = Total_itens




janela.mainloop()

