"""1:
 Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes
 de dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
 monitoreo (ej: "San Telmo") y el Valor sea una lista de flotantes que represente
 las últimas 3 lecturas de contaminación tomadas en el día.
 Desarrollar las siguientes funciones:
 1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
    una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
 2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada barrio.
 3. Alerta ambiental: Mostrar en pantalla una alerta roja de "Protocolo de Emergencia"
    únicamente para las estaciones cuyo promedio de contaminación supere las 400 ppm."""


def cargar():
    datos = {}

    for i in range(3):
        nombre = input(f"Ingrese el nombre de la estación {i + 1}: ")
        valores = []

        for j in range(3):
            valor = float(
                input(
                    f"Ingrese la lectura {j + 1} de CO2 para {nombre} (ppm): "
                )
            )
            valores.append(valor)

        datos[nombre] = valores

    return datos


def reportar_promedios(datos):
    promedios = {}

    for nombre in datos:
        valores = datos[nombre]
        suma = 0

        for i in range(len(valores)):
            suma = suma + valores[i]

        promedio = suma / len(valores)
        promedios[nombre] = promedio

        print("Promedio de", nombre, ":", promedio, "ppm")

    return promedios


def alerta_ambiental(promedios):
    print("Alertas Ambientales")

    for nombre in promedios:
        promedio = promedios[nombre]

        if promedio > 400:
            print(
                "ALERTA ROJA (Protocolo de Emergencia) en:",
                nombre,
                "con",
                promedio,
                "ppm"
            )


datos = cargar()
promedios = reportar_promedios(datos)
alerta_ambiental(promedios)