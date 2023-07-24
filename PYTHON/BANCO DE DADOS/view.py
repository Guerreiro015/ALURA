
import os
os.system("cls")

# import sqlite
import sqlite3 as lite

# Criando banco de dados
con = lite.connect("dados.bd")

#Inserir dados
dados = ['vaso','sala','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem']
cur = con.cursor()
query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra,valor_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)"

cur.execute(query,dados)

#VER DADOS

ver_dados = []
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario"
    cur.execute(query)

    dad = cur.fetchall()

    for x in dad:
        ver_dados.append(x)


print(ver_dados)

