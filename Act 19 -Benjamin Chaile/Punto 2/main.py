"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""






def cargar():
    lista = []
    for i in range(10):
        sueldo = int(input(f"Ingrese el sueldo {i + 1}: "))
        lista.append(sueldo)
    return lista

def mostrar(lista):
    print("Sueldos:")
    for sueldo in lista:
        print(sueldo)

def contar(lista, limite):
    cuenta = 0
    for sueldo in lista:
        if sueldo > limite:
            cuenta += 1
    return cuenta

def promedio(lista):
    return sum(lista) / len(lista)

def debajo(lista, prom):
    print("Sueldos por debajo del promedio:")
    for sueldo in lista:
        if sueldo < prom:
            print(sueldo)

def principal():
    lista = cargar()
    mostrar(lista)

    limite = 4000
    cantidad = contar(lista, limite)
    print("Cantidad de sueldos superiores a", limite, ":", cantidad)

    prom = promedio(lista)
    print("Promedio:", prom)

    debajo(lista, prom)

principal()
