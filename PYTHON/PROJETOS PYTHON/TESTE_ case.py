a=5

def semana(dia):
   match dia:
    case 1:
       print("Segunda")

    case 2:
       print("Terça")
    
    case 3:
       print("Quarta")

    case 4:
       print("Quinta")  

    case 5:
       print("Sexta")   
      
    case 6:
       print("Sábado")  

    case 7:
       print("Domingo")     

    case _:
       print(" Não tem esta opção cadastrada")


for i in range(0,10):
   semana(i)







