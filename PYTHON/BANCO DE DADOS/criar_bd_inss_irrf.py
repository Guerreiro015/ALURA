import sqlite3 as lite

# Criando banco de dados
con = lite.connect("dados.bd")

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, de1 DECIMAL,ate1 DECIMAL,ali1 DECIMAL,par1 DECIMAL,
                de2 DECIMAL,ate2 DECIMAL,ali1 DECIMAL,par2 DECIMAL
                de3 DECIMAL,ate3 DECIMAL,ali1 DECIMAL,par3 DECIMAL
                de4 DECIMAL,ate4 DECIMAL,ali1 DECIMAL,par4 DECIMAL
                de2 DECIMAL,ate1 DECIMAL,ali1 DECIMAL,par1 DECIMAL)''')

    de1.delete(0, 'end')
    ate1.delete(0, 'end')
    ali1.delete(0, 'end')
    par1.delete(0, 'end')

    de2.delete(0, 'end')
    ate2.delete(0, 'end')
    ali2.delete(0, 'end')
    par2.delete(0, 'end')
    
    de3.delete(0, 'end')
    ate3.delete(0, 'end')
    ali3.delete(0, 'end')
    par3.delete(0, 'end')

    de4.delete(0, 'end')
    ate4.delete(0, 'end')
    ali4.delete(0, 'end')
    par4.delete(0, 'end')

    deir1.delete(0, 'end')
    ateir1.delete(0, 'end')
    aliir1.delete(0, 'end')
    parir1.delete(0, 'end')

    deir2.delete(0, 'end')
    ateir2.delete(0, 'end')
    aliir2.delete(0, 'end')
    parir2.delete(0, 'end')
    
    deir3.delete(0, 'end')
    ateir3.delete(0, 'end')
    aliir3.delete(0, 'end')
    par3.delete(0, 'end')

    deir4.delete(0, 'end')
    ateir4.delete(0, 'end')
    aliir4.delete(0, 'end')
    parir4.delete(0, 'end')

