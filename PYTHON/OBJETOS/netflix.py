class cliente:
    import os
    os.system("cls")
    def __init__(self,nome,email,plano):
        self.nome = nome
        self.email = email
        self.listas_planos = ["basic","premium","top"]
        if plano in self.listas_planos:
            self.plano = plano
        else:
            print("Plano invalido")
        self.valor = 0

    
    def mudar_plano(self,novo_plano):   
        if novo_plano in self.listas_planos:
            self.plano = novo_plano
            print(f" o cliente {self.nome} mudou para o plano {self.plano}")
        else:
            print("Erro no nome do plano, nome não é válido")    


    def filmes(self,filme,plano):
        if plano == criar.plano or criar.plano == self.listas_planos[2]:
            print(f"O cliente {self.nome} Pode assistir o filme - { filme} - \n")

        else:
            print(f"O cliente {self.nome} Nâo pode assistir o filme - {filme} - Precisa alterar o plano\n")


criar = cliente("antonio","antonio@email","basic")
print(criar.nome)
print(criar.plano)

print(f" O cliente {criar.nome} foi cadastrado com sucesso no plano {criar.plano}\n")

criar.filmes("Amor De Noite","premium")

criar.mudar_plano("to")

print(f"\n O Novo plano do {criar.nome} e o plano {criar.plano}\n")

criar.filmes("Amor De Noite","premium")








        