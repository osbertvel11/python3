#osbert
#solicitar al usuario que seleccione una opcion dos numeros y elevar el primer con el seundo
#solicitar tres nuemros y elevar el primero al segundo y el resultado mostrarlo al tercero


print("1.la elevacion.2 por  el tercero".center(50,"-"))
valor= input(":.") 
if valor == ("1"):
   valor1 = int(input("ingresa un valor:"))
   valor2 = int(input("ingresa un valor:"))
   elevacion = int(valor1) ** int(valor2)
   print("la elevacion es:.{}".format(elevacion))
elif  valor == ("2"):
    valor1 = int(input("ingresa un valor:"))
    valor2 = int(input("ingresa un valor:"))
    valor3 = int(input("ingresa un valor:"))
    elevacion = int(valor1) ** int(valor2)**(valor3)
    print("la elevacion es:.{}".format(elevacion))
