"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.

"""
def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

def solicitar_carga():
    print("Ingrese los lados del primer rectángulo:")
    lado1_rectangulo1 = int(input("Lado 1: "))
    lado2_rectangulo1 = int(input("Lado 2: "))

    print("Ingrese los lados del segundo rectángulo:")
    lado1_rectangulo2 = int(input("Lado 1: "))
    lado2_rectangulo2 = int(input("Lado 2: "))

    superficie_rectangulo1 = retornar_superficie(lado1_rectangulo1, lado2_rectangulo1)
    superficie_rectangulo2 = retornar_superficie(lado1_rectangulo2, lado2_rectangulo2)

    if superficie_rectangulo1 > superficie_rectangulo2:
        print(f"El primer rectángulo tiene una superficie mayor: {superficie_rectangulo1}")
    elif superficie_rectangulo2 > superficie_rectangulo1:
        print(f"El segundo rectángulo tiene una superficie mayor: {superficie_rectangulo2}")
    else:
        print("Ambos rectángulos tienen la misma superficie.")

solicitar_carga()