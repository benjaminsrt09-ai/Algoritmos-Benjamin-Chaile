"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
utilizar herramientas basicas de python y ordenar manuealmente
"""

numeros = []
for i in range(5):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print("Lista ordenada de menor a mayor:")
for num in numeros:
    print(num)

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Lista ordenada de mayor a menor:")
for num in numeros:
    print(num)