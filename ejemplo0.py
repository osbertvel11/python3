## osbert
##calcular la edad actual de una persona,
#previamente ingresando
#el año  actual y el nacimiento

print("Bienvenido al Programa".center(50,"*"))
FEC_ACT = 2019
fec_nac = int(input("ingresa tu anio de nacimiento"))

edad = FEC_ACT - fec_nac

print("tu edad es {}".format (edad))
if edad >= 18:
    print("eres mayor de edad ")
else:
    print("eres menor de edad ")


#print("Tu edad es {}.format (edad)

