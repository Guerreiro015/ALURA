def palavra_secreta():
    with open("lista_frutas.txt","w") as arquivo:
        arquivo.write("banana\nmelancia\nmanga\nabacaxi\nmaracuja\nmorango\nameixa\ngoiaba\ncaju\npera\ncarambola\nlaranja\ncaqui\nabacate\nmamao\n")

    import random
    with open("lista_frutas.txt","r") as lista:
        ler = lista.readlines()
    tamanho = len(ler)
    numero = random.randrange(0,tamanho)

    palavra = ler[numero]
    return palavra

    print(tamanho)
    print(palavra)
    for linha in ler:
        print(linha)



