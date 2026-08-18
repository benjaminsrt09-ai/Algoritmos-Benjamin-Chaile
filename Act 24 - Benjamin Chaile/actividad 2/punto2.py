""" 2:
 En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
 para realizar misiones cooperativas.
 Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej: "DragonesDeFuego")
 y el Valor sea una lista de cadenas con los nombres de los jugadores (nicknames) que lo integran.
 Desarrollar las siguientes funciones:
 1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
    preguntar cuántos integrantes posee para cargar sus respectivos nombres de
    usuario en la lista interna.
 2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
    de miembros que posee cada uno.
 3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
    gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
    "Solitario" (no pertenece a ningún clan)."""


def cargar():
    clanes = {}

    for i in range(3):
        nombre = input(f"Ingrese el nombre del clan {i + 1}: ")
        cantidad = int(input(f"¿Cuántos integrantes tiene {nombre}?: "))
        jugadores = []

        for j in range(cantidad):
            jugador = input(f"Ingrese el nickname del jugador {j + 1}: ")
            jugadores.append(jugador)

        clanes[nombre] = jugadores

    return clanes


def listar_clanes(clanes):
    print("Listado de Clanes")

    for nombre in clanes:
        jugadores = clanes[nombre]
        print("Clan:", nombre, "Cantidad de miembros:", len(jugadores))


def buscar_jugador(clanes):
    buscado = input("Ingrese el nickname del jugador a buscar: ")
    encontrado = False

    for nombre in clanes:
        jugadores = clanes[nombre]

        for i in range(len(jugadores)):
            if jugadores[i] == buscado:
                print("El jugador", buscado, "pertenece al clan:", nombre)
                encontrado = True
                break

        if encontrado == True:
            break

    if encontrado == False:
        print("El jugador", buscado, "es solitario (no pertenece a ningún clan).")


clanes = cargar()
listar_clanes(clanes)
buscar_jugador(clanes)
