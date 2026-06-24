"""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def cargar_articulos():
    articulos = []
    precios = []
    for x in range (5):
        arti = input("ingresar nombre del producto: ")
        articulos.append(arti)
        valor = int(input(f"ingresar precio de {arti}:"))
        precios.append(valor)

    return articulos, precios

def imprimir(articulos, precios):
    for x in range (5):
        print(f"articulo: {articulos[x]} su precio es de: ${precios[x]}")

def mayor(articulos,precios):
    precioM = precios[0]
    nombre = articulos[0]
    for x in range (1, 5):
        if precios[x] > precioM:
            precioM = precios[x]
            nombre = articulos[x]
    print (f"el articulo con mayor precio es: {nombre} con un precio de: ${precioM}")

def importe(nombre, precioM):
    importe=int(input("ingrese un importe para buscar productos con precios menores o iguales "))
    print(f"productos con precios menor o igual a ${importe}:")
    encontrado = False
    for x in range (5):
        if precioM[x] <= importe:
            print(f"{nombre[x]}: ${precioM[x]}")
            encontrado = True
    if not encontrado:
        print("no se encontraron artículos con un importe menor o igual al ingresado ")

listas_articulos, listas_precios = cargar_articulos()

imprimir(listas_articulos, listas_precios)
mayor(listas_articulos, listas_precios)
importe(listas_articulos, listas_precios)