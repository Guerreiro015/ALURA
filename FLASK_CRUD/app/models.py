from database import db
#Criar um banco de dados
class usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Interger,primay_key=True)
    nome = db.column(db.String(100))
    email = db.column(db.String(100))
    senha = db.column(db.String(100))

    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def __rep__(self):
        return f'usuario: {self.nome}'

