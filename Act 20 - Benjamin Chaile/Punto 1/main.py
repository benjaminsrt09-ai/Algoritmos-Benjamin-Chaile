"""
1. Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)
"""

def mas_caracteres(lista):
    palabra_mas_larga = lista[0]
    
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
        elif len(palabra) == len(palabra_mas_larga):
            if palabra < palabra_mas_larga:
                palabra_mas_larga = palabra
                
    return palabra_mas_larga

palabras = ["Sebastian", "Santiago", "Fobian", "Luciano", "Virginia", "Lorenzo"]
print("Palabra con mas caracteres:", mas_caracteres(palabras))
