"""
3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
más posiciones en la lista)

"""

numero = []
for i in range (5):
    numero.append(int(input("Ingrese un numero: ")))
mayor = numero[0]
for i in range (1, len(numero)):
    if numero[i] > mayor:
        mayor = numero[i]

print ("El numero mayor es: ", mayor)

contador = 0

for i in range (len(numero)):
    if numero[i] == mayor:
        contador += 1

if contador > 1:
    print ("El numero mayor se repite en la lista") 

    for i in range (5):
        if numero[i] == mayor:
            print ("El numero mayor se encuentra en la posicion: ", i)

menor = numero[0]
for i in range (1, len(numero)):
    if numero[i] < menor:
        menor = numero[i]

print ("El numero menor es: ", menor)