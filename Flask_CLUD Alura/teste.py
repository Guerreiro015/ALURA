<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<link rel="stylesheet" href="../static/bootstrap.css" >
<body background="/images/fundo.jpg" bgproperties="fixed">
(corpo do documento em HTML)
</body>

def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = '''UPDATE dados SET 
                de1=?,ate1=?,ali1=?,par1=?,
                de2=?,ate2=?,ali2=?,par2=?,
                de3=?,ate3=?,ali3=?,par3=?,
                de4=?,ate4=?,ali4=?,par4=?,
                deir1=?,ateir1=?,aliir1=?,parir1=?,
                deir2=?,ateir2=?,aliir2=?,parir2=?,
                deir3=?,ateir3=?,aliir3=?,parir3=?,
                deir4=?,ateir4=?,aliir4=?,parir4=?,
                deir5=?,aliir5=?,parir5=?,tetoinss=?,
                dedudep=?,dedusimp=?'''
        
        cur.execute(query,i)
        con.commit()

def visualizar():   
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM dados")
        linha_dados = cur.fetchall()
        for i in linha_dados:
             lista_itens.append(i)
        return lista_itens
    #print(lista_itens)#
            


def inserir_dados(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO dados(de1,ate1,ali1,par1,de2,ate2,ali2,par2,de3,ate3,ali3,par3,de4,ate4,ali4,par4,deir1,ateir1,aliir1,parir1,deir2,ateir2,aliir2,parir2,deir3,ateir3,aliir3,parir3,deir4,ateir4,aliir4,parir4,deir5,aliir5,parir5,tetoinss,dedudep,dedusimp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                
                           
        cur.execute(query,i)
        con.commit()     