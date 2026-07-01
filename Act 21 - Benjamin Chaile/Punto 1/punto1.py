"""
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

def cargar_lista():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista

def retornar_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return (mayor, menor)


lista = cargar_lista()
mayor, menor = retornar_mayor_menor(lista)
print("Lista completa:", lista)
print("El mayor es:", mayor)
print("El menor es:", menor)