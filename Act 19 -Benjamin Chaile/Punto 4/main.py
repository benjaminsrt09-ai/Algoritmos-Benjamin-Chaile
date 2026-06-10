"""
4. Elaborar una función que muestre la tabla de multiplicar del valor que le
enviemos como parámetro. Definir un segundo parámetro llamado termino
que por defecto almacene el valor 10. Se deben mostrar tantos términos de
la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con
argumentos nombrados.
"""

def tabla_multiplicar(valor, termino = 10):
   
    print(f"Tabla de multiplicar del {valor}:")
    for i in range(1, termino + 1):
        print(f"{valor} x {i} = {valor * i}")


v = int(input("ingrese el numero de la tabla: "))
t = int(input("ingrese la cantidad de terminos que desea: "))


tabla_multiplicar(valor=v, termino=t)


