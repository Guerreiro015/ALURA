def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra = "banana"
    enforcou = False
    acertou = False
    maiusculo = palavra.upper()# Transformar em maisculos
    minusculo = palavra.lower()# Transformar em minúsculo
    print(maiusculo)
    print(minusculo)

    index = 0

    while(not enforcou and not acertou):
        print("jogando...")
        chute = input("Qual chute? ")
        for letra in (palavra):
            if (chute==letra):
                print(f"A letra ( {letra} ) digitada foi encontrda na posição ( {index} )")
                index=index+1
            else:
               # print(f"A letra ( {chute}) digitada, não tem na palavra secreta")
                index=index+1
                continue
        acertou = True
    print("Fim do jogo")
        

if(__name__ == '__main__'):
    jogar()