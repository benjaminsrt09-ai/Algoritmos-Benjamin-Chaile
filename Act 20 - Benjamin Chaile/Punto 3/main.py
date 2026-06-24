"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def cargar_lista():
    lista = []
    print("por favor, ingrese 10 números enteros (pueden ser positivos o negativos):")
    x = 0
    while x < 10:
        num = int(input(f"numero {x+1}: "))
        if num == 0:
            print("ingrese un numero distinto de 0")
        else:
            lista.append(num)
            x += 1
    return lista

def separar_listas(lista_original):
    positivos = []
    negativos = []
    for num in lista_original:
        if num >=0:
            positivos.append(num)
        else:
            negativos.append(num)
    return positivos, negativos 

def imprimir_listas(positivos, negativos):
    print(f"lista de valores positivos: {positivos}")
    print(f"lista de valores negativos: {negativos}")

lista_principal = cargar_lista()
lista_pos, lista_neg = separar_listas(lista_principal)
imprimir_listas(lista_pos, lista_neg)
    