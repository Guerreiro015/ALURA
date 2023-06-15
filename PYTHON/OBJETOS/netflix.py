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
        else:
            print("Plano para alterar não é válido")       

criar = cliente("antonio","antonio@email","basic")
print(criar.nome)
print(criar.plano)

print(f" O cliente {criar.nome} foi cadastrado com sucesso no plano {criar.plano}")

criar.mudar_plano("top")
print(f" o cliente {criar.nome} mudou para o plano {criar.plano}")
print(criar.plano)





        