#3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
#(mensajes "Lista 1", "Lista 2" , "Listas iguales") Tener en cuenta que
#puede haber dos o más estructuras repetitivas en un algoritmo.

suma1 = 0
suma2 = 0

print("Cargar valores de la Lista 1")
for i in range(15):
    valor = int(input("Ingrese el valor de la lista 1: "))
    suma1 += valor

print("Cargar valores de la Lista 2")
for i in range(15):
    valor = int(input("Ingrese el valor de la lista 2: "))
    suma2 += valor

if suma1 > suma2:
    print("Lista 1 mayor")

if suma2 > suma1:
    print("Lista 2 mayor")

if suma1 == suma2:
    print("Listas iguales")



