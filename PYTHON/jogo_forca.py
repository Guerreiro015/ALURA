def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra = " BANANA   "
    enforcou = False
    acertou = False
    palavra = palavra.upper()# Transformar em maisculos
    palavra = palavra.lower()# Transformar em minúsculo
    palavra = palavra.strip() # tira espaços no inicio e fim
    
    print(palavra)   

    index = 0

    while(not enforcou and not acertou):
        print("jogando...")
        chute = input("Qual chute? ")
        chute = chute.strip()
        chute = chute.lower()

        for letra in (palavra):
            if (chute.lower() == letra.lower()):
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