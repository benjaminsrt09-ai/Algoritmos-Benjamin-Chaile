"""4:
 Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
 y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
 Diseñar un diccionario donde la Clave sea el identificador único del dron (ej: "DRON-01")
 y el Valor sea una lista de tuplas que almacene las coordenadas de
 las paradas programadas: [(latitud, longitud)].
 Desarrollar las siguientes funciones:
 1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
    uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas geográficas.
 2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
    de coordenadas asociadas.
 3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
    cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad de elementos).
"""
def cargar():
    datos = {}

    for i in range(3):
        nombre = input(
            f"Ingrese el identificador del dron {i + 1} (ej: DRON-01): "
        )

        cantidad = int(
            input(f"¿Cuantas paradas realizara el {nombre}?: ")
        )

        paradas = []

        for j in range(cantidad):
            latitud = float(
                input(f"Ingrese la latitud de la parada {j + 1}: ")
            )

            longitud = float(
                input(f"Ingrese la longitud de la parada {j + 1}: ")
            )

            paradas.append((latitud, longitud))

        datos[nombre] = paradas

    return datos


def imprimir_rutas(datos):
    print("Listado Completo de Rutas")

    for nombre in datos:
        paradas = datos[nombre]

        print("Dron:", nombre)

        for j in range(len(paradas)):
            coordenada = paradas[j]

            print(
                "Parada",
                j + 1,
                ": Latitud",
                coordenada[0],
                ", Longitud",
                coordenada[1]
            )


def ruta_mas_larga(datos):
    mayor = -1
    dron_mayor = ""

    for nombre in datos:
        paradas = datos[nombre]

        if len(paradas) > mayor:
            mayor = len(paradas)
            dron_mayor = nombre

    if dron_mayor != "":
        print(
            "El dron con la ruta mas larga es",
            dron_mayor,
            "con",
            mayor,
            "paradas registradas."
        )


datos = cargar()
imprimir_rutas(datos)
ruta_mas_larga(datos)