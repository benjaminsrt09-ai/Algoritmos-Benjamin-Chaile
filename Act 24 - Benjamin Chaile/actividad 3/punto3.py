"""3:
 Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
 en cada habitación de la casa.
 Crear un diccionario donde la Clave sea el nombre del ambiente (ej: "Cocina", "Dormitorio")
 y el Valor sea una lista de tuplas, donde cada tupla represente un
 dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
 Desarrollar las siguientes funciones:
 1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
    ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
    operador decida no cargar más para ese ambiente.
 2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
    en Watts acumulado en cada una de ellas.
 3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
    energía consume de toda la casa (el valor máximo individual dentro de todas las
    listas del diccionario), indicando en qué habitación se encuentra.
"""

def cargar():
    casa = {}

    for i in range(3):
        habitacion = input(f"Ingrese el nombre de la habitacion {i + 1}: ")
        lista = []

        seguir = "si"

        while seguir.lower() == "si":
            dispositivo = input(
                f"Ingrese el nombre del dispositivo para {habitacion}: "
            )

            consumo = float(
                input(f"Ingrese el consumo en Watts de {dispositivo}: ")
            )

            lista.append((dispositivo, consumo))

            seguir = input(
                "¿Desea ingresar otro dispositivo en esta habitacion? (si/no): "
            )

        casa[habitacion] = lista

    return casa


def consumo_por_habitacion(casa):
    print("Consumo por Habitacion")

    for habitacion in casa:
        lista = casa[habitacion]
        total = 0

        for i in range(len(lista)):
            dispositivo = lista[i]
            total = total + dispositivo[1]

        print(
            "Habitacion:",
            habitacion,
            "Consumo Total:",
            total,
            "Watts"
        )


def dispositivo_critico(casa):
    mayor = -1
    dispositivo_mayor = ""
    habitacion_mayor = ""

    for habitacion in casa:
        lista = casa[habitacion]

        for i in range(len(lista)):
            dispositivo = lista[i]
            nombre = dispositivo[0]
            consumo = dispositivo[1]

            if consumo > mayor:
                mayor = consumo
                dispositivo_mayor = nombre
                habitacion_mayor = habitacion

    if dispositivo_mayor != "":
        print(
            "Dispositivo critico:",
            dispositivo_mayor,
            "con",
            mayor,
            "Watts en la habitacion:",
            habitacion_mayor
        )


casa = cargar()
consumo_por_habitacion(casa)
dispositivo_critico(casa)