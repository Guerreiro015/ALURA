with open("modo.txt","w") as moelo:
    moelo.write("hoje dva dar")

with open("modo.txt",'r') as moelo:
    mo = moelo.read()
print(mo)