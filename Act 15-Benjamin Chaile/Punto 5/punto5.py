"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.

"""
paises = []
habitantes = []
for i in range(5):
    pais = input("Ingrese el nombre de un país: ")
    habitantesPais = int(input(f"Ingrese la cantidad de habitantes de {pais}: "))
    paises.append(pais)
    habitantes.append(habitantesPais)
for i in range(len(paises)):
    for j in range(i + 1, len(paises)):
        if paises[i] > paises[j]:
            paises[i], paises[j] = paises[j], paises[i]
            habitantes[i], habitantes[j] = habitantes[j], habitantes[i]
print("Lista de países ordenada alfabéticamente:")
for i in range(len(paises)):
    print(f"País: {paises[i]}, Habitantes: {habitantes[i]}")
for i in range(len(habitantes)):
    for j in range(i + 1, len(habitantes)):
        if habitantes[i] < habitantes[j]:
            habitantes[i], habitantes[j] = habitantes[j], habitantes[i]
            paises[i], paises[j] = paises[j], paises[i]
print("Lista de países ordenada por cantidad de habitantes (de mayor a menor):")
for i in range(len(paises)):
    print(f"País: {paises[i]}, Habitantes: {habitantes[i]}")

