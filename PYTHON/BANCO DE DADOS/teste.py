from Banco import Banco

class Usuarios(object):


    def __init__(self, nome = "", local = "", descricao = "",modelo = "",data = "", valor = "", serie = "",imagem = ""):
        self.info = {}
        self.nome = nome
        self.local = local
        self.descricao = descricao
        self.modelo = modelo
        self.data = data
        self.valor = valor
        self.serie = serie
        self.imagem = imagem

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()
 #nome,local,descricao,modelo,data,valor,serie,imagem
            c.execute("insert into usuarios ( nome, local, descricao,modelo,data, valor, serie,imagem) values ('" + self.nome + "', '" +
            self.local + "', '" + self.descricao + "', '" +
            self.modelo + "',  '" + self.data + "' '" + self.valor + "' '" + self.serie + "''" + self.imagem + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', local = '" + self.local + "',descricao = '" + self.descricao + "', modelo = '" + self.modelo + "', data = '" + self.data + "', valor = '" + self.valor "' '" + self.serie + "''" + self.imagem + "'
            "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
        
