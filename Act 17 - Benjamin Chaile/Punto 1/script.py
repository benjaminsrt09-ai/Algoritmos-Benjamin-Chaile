"""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50
del primer elemento de "lista"
Volver a imprimir la lista.
"""


lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

primera = []

for x in range(len(lista)):

    lista2 = []

    for j in lista[x]:

        if j > 50:
            primera.append(j)
        
        else:
            lista2.append(j)

    lista[x] = lista2

lista[0] = primera

print(lista)


