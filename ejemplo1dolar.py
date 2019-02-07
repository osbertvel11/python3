#osbert
#crear un program que les permita seleccionar entre una de dos opcions
#convertir dolares a quetzales o quetzales a dolares

print ("BIENVENIDO AL SISTEMA".center(50,"*"))

print ("seleccionar opcion")
print ("1.quetzales a dolares:")
print ("2.dolares a quetzales:")


op = 0
op = int(input())
valdolar = 7.71

if op == 1:
    cant = float(input("ingrese la cantidad:"))
    total = (cant/valdolar)
    print("conversion: ","$.",total)
          
elif  op == 2:
     cant = float(input("ingrese la cantidad:"))
     total = (cant*valdolar)
     print("conversion: ","Q.",total)

else:
          print("opcion no valida:")
          
          
