"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".

"""
def contar(cadena):
    contador = 0
    for letra in cadena:
        if letra == 'a' or letra == 'A':
            contador += 1
    return contador

def solicitar_carga():
    texto = input("Ingrese un texto: ")
    cantidad_a = contar(texto)
    print(f"La cantidad de letras a o A en el texto es: {cantidad_a}")

solicitar_carga() 