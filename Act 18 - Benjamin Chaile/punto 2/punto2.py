"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""

def ordenamiento(valor1, valor2, valor3):

    if valor1 <= valor2 and valor2 <= valor3:
        print(f"Lista ordenada de menor a mayor: {valor1}, {valor2}, {valor3}")

    elif valor1 <= valor3 and valor3 <= valor2:
        print(f"Lista ordenada de menor a mayor: {valor1}, {valor3}, {valor2}")

    elif valor2 <= valor1 and valor1 <= valor3:
        print(f"Lista ordenada de menor a mayor: {valor2}, {valor1}, {valor3}")

    elif valor2 <= valor3 and valor3 <= valor1:
        print(f"Lista ordenada de menor a mayor: {valor2}, {valor3}, {valor1}")

    elif valor3 <= valor1 and valor1 <= valor2:
        print(f"Lista ordenada de menor a mayor: {valor3}, {valor1}, {valor2}")

    else:
        print(f"Lista ordenada de menor a mayor: {valor3}, {valor2}, {valor1}")


def solicitar_carga():
    v1 = int(input("Ingrese el primer valor: "))
    v2 = int(input("Ingrese el segundo valor: "))
    v3 = int(input("Ingrese el tercer valor: "))

    ordenamiento(v1, v2, v3)


solicitar_carga()