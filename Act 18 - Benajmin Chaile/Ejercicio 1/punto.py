"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)

"""

def solicitar_carga():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))

    if valor1 <= valor2 and valor1 <= valor3:
        print("El menor valor es:", valor1)
    elif valor2 <= valor1 and valor2 <= valor3:
        print("El menor valor es:", valor2)
    else:
        print("El menor valor es:", valor3)
    

solicitar_carga()
solicitar_carga()
