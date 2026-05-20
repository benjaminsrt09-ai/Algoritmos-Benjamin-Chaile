"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""

lista1 = []
lista2 = []
for i in range(4):
    num1 = int(input("Ingrese un número para la primera lista: "))
    num2 = int(input("Ingrese un número para la segunda lista: "))
    lista1.append(num1)
    lista2.append(num2)
lista3 = []
for i in range(4):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)
print("La tercera lista con la suma de los elementos es:")
print(lista3)

