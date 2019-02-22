#una persona recibe un prestamo de bs. 10,0000 de un banco y desea saber
#cuanto  pagara de interes ,si el banco le cobra una tasa de interes de 27% anual
#1
#PRESTAMO = 100000
#DESCUENTO = 0.27
#interes = 0
#input("INGRESE PRESTAMO ")
#interes  = PRESTAMO * DESCUENTO
#input("el total a pagar es {}".format(interes))



#2 calcula el precio de un boleto  de viaje ,tomando en cuenta el numero de kilometros
#que va a recorrer ,siendo el precio de bs 10.50 por km


#km = 0
#boleto = 10.50
#km  = int(input("ingrese cuantos voletos quiere:"))
#km = boleto * km
#print(" el total es:.{}".format(km ))

#3calcular el monto a pagar  de una cabina de internet si el costo por hora  es de
#bs 1.5 y por cada 5 horas te dan una hora de promocion gratis

#hora = 1.5
#COSTO = 0
#horas = int(input("ingrese cuantas horas necesita caniva de internet :"))
#if horas <= 20:
    #costo = horas  * hora
    #print("el costo a pagar es de :{}".format(costo))


#4 calcular el cambio de monedas en dolares y euros al ingresar sierta cantidad
#en bs(tipo de cambio  $ 2500bs ,euros 1.45$

#DOLARES = 2.15
#EUROS = 1.45
#dolares = 0
#euros = 0
#menu = int (input("1.dolares_a_euros 2.euros_a_dolares"))
#if menu == 1:
   #dolares =int(input("ingrese cantidad de dolares:"))
   #cambio = dolares /EUROS
   #print("el costo a pagar es de :{}".format(cambio))
#elif menu == 2:
        #euros =int(input("ingrese cantidad de dolares"))
        #cambio = DOLAR *DOLAR
        #print("el costo a pagar es de :{}".format(cambio))

#5
#calcular e descuento  y el monto a pagar por un medicaento cualquier en una farmacia si todos los medicamentos tienen un descuento del 35%
#compra = 0
#DES = 0.35
#total_a_pagar = 0

#compra =int (input("ingrese en cuanto esta valorado tu producto:"))
#if compra <= 1000000000:
    #total_a_pagar = compra *DES
    #print("el costo a pagar con su descuento es :{}".format(total_a_pagar))

#6
#calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su salario actual  y de un descuento de 2.5%por servicios
#salario = 0
#salario_nuevo = 0
#INCRE = 0.08
#DESC = 0.025
#salario = int(input("ingresa tu salario"))
#INCRE = salario * INCRE
#salario_nuevo =INCRE + salario
#DESC = salario_nuevo * 0.025
#print("el aumento es:{}".format(INCRE))
#print("el salario nuevo es:{}".format(salario_nuevo))
#print("el descuento del salario es:{}".format(DESC))

#7
#en un hospital existen 3 areas urgencia ,pediatria y traumatologia el presuspuesto anual del hospital se reparte de la siguinte manera area 37%pediatria 42%
#traumatologia21%

#URGENCIA = 0.37
#PEDIATRIA =0.42
#TRAUMATOLOGIA =0.21
#print("calcular presupuesto")
#salida = input("ingresa presupuesto 1-si \ n 2-no")
#while salida != 2:
    #presupuesto = int(input("ingresa cantidad"))
    #print("la cantidad es:{}".format(presupuesto *URGENCIA))
    #print("la cantidad es:{}".format(presupuesto *PEDIATRIA))
    #print("la cantidad es:{}".format(presupuesto *TRAUMATOLOGIA))
    #salida = input("ingresar presupuesto 1-si \n 2-no")

#8
    #escriba un algoritmo que da cantidad de monedas en 5-10-12,5-25-50 cent y 1bolivar ,diga la cantida de dinero que se tiene ne total
    
#moneda_1 = 0
#moneda_2 = 0
#moneda_3 = 0
#moneda_4 = 0
#moneda_5 = 0
#moneda_6 = 0

#tatal_1 = 0
#tatal_2 = 0
#tatal_3 = 0
#tatal_4 = 0
#tatal_5 = 0
#tatal_6 = 0

#moneda_1 = int(input("ingresa monedas de 5 :."))
#total_1 = moneda_1 * 0.05
#moneda_2 = int(input("ingresa monedas de 10 :."))
#total_2 = moneda_2 * 0.10
#moneda_3 = int(input("ingresa monedas de 12,5 :."))
#total_3 = moneda_3 * 0.125
#moneda_4 = int(input("ingresa monedas de 25 :."))
#total_4 = moneda_4 * 0.25
#moneda_5 = int(input("ingresa monedas de 50 :."))
#total_5 = moneda_5 * 0.50
#moneda_6 = int(input("ingresa moneda de 1 bolivar :."))
#total_6 = moneda_6 * 1

#total = total_1 +total_2 + total_3 + total_4 +total_5 +total_6
#print("total de dinero es de: ",total)



#9
#escriba un algoritmo  que dado el nmero  de horas trabajadas por un empleado y el sueldo por hora ,calcule el sueldo total de ese empleado .tenga en cuenta que
#las horas extras se pagan el doble

#val_h = 0
#h = 0
#hor_ex = 0
#valor_horas = int(input("valor d las horas extras:"))
#hora =int(input("horas trabajadas: "))
#val_h =int(valor_horas)* int(hora)
#h = int(valor_horas) *int(hor_ex)  
#h_ex = int(valor_horas) + int(valor_horas) -int(hor_ex) 
#print("su sueldo normal es :.{}".format(val_h))
#print("su sueldo extra es :.{}".format(h))
#print("EL TOTAL ES :.{}".format(hor_ex))


#11
#un constructor sabe que necesita 0,5 metros cubicos de arena  por metro cuadrado
#HORAS = 3600
#MINUTOS = 60
#SEGUNDOS = 0.25
#menu = int(input("1.tiempo en horas 2.tiempoen minutos 3.tiempo en segundos"))
#if menu == 1 :
    #horas = int(input("ingrese cuantas horas necesita"))
    #tiempo = horas * HORAS
    #total = tiempo * SEGUNDOS
    #print("el totala pagar por el tiempo es de :{}".format(total))
#elif menu == 2:
    #minutos = int(input("ingrese cuantos minutos necesita"))
    #tiempo = minutos * MINUTOS
    #total = tempo * SEGUNDOS
    #print("el total a pagar por el tiempo es de :{}".format(total))
#if menu == 3:
    #segundos = int(input("ingrese cuantos segundos necesita"))
    #total = segundo  * SEGUNDOS
    #print("el total a pagar por el tiempo es de :{}".format(total))


#12
#calcular el nuevo salario de un empleado si se le descuenta el 20% de su salario actual
#DESCUENTO = 0.20
#salario = 0
#salario = int(input("ingrese  sueldo :"))
#descuento = salario * DESCUENTO
#resta = salario - descuento
#print("su sueldo nuevo es de :{}".format(resta))

#13

#n1 = 0
#n2 = 0
#n1 = int(input("ingrese primer numero "))
#n2 = int(input("ingrese segundo numero "))
#suma = n1 +n2
#elevacion = n2 ** 2
#total = suma + elevacion
#print("el total es de :{}".format(total))
#cubo = (n1 ** 3) + (n2 **3)
#promedio = cubo / 2
#print("el promedio de sus cubos es de :{}".format(promedio))

#14

#n1 = 0
#n2 = 0
#n3 = 0
#lista = 0
#n1 = int(input("ingrese primer numero"))
#n2 = int(input("ingrese segundo numero"))
#n3 = int(input("ingrese tercer numero"))
#lista(n1,n2,n3)

#15

#anios = o
#meses = 0
#anios = int(input("ingrses edad en anios"))
#meses = int(input("ingrses meses  despues de los  anios"))
#mult = anios *12
#suma = meses + mult
#print("total de sus meses:{}".format(suma))


#16
#PORCENTAJE = 0.025
#capital = 0
#capital = int(input("ingrese el capital a invertir:"))
#mult = capital * PORCENTAJE
#total = mult *12
#print("el dienro a ganar en un año es :{}".format(total))




    
    




   
   
    
    

                      
                      

