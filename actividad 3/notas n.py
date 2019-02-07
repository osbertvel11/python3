#osbert
#realizar el promedio de n notas utilizando el for
valor = int(input("cuantas notas desea ingresar"))
suma = 0
for i in range (valor):
    nota = input("ingrese nota:")
    suma = suma + int(nota)
promedio = suma / valor
print("el promedio es {}".format(promedio))
    
