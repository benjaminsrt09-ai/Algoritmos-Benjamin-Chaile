"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""

def cargar_edades():
    
    lista_edades = []
    cantidad = int(input("¿cuantas edades desea ingresar?: "))

    for x in range (cantidad):
        edad =  int(input(f"ingresa la dead de la persona {x+1}:"))
        lista_edades.append(edad)

    return lista_edades

def contar_mayores(edades):
    contador = 0
    for edad in edades:
        if edad >=18:
            contador += 1
    return contador 

def mostrar_resultado(total):
    print(f"la cantidad de personas mayores de edad son: {total}")

edades_ingresadas = cargar_edades()

total_mayores = contar_mayores(edades_ingresadas)

mostrar_resultado(total_mayores)
