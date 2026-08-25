"""2-Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero)."""

def solicitar_carga():
    camaras=[]
    for i in range (4):
        lati = float(input(f"ingrese la {i+1}° latitud: "))
        longi = float(input(f"ingrese la {i+1}° longitud: "))
        camaras.append((lati,longi))
        

    return (camaras)

def posiciones(camaras):
    for i in range(len(camaras)):
        lat, lon = camaras[i]
        print(f"camara {i+1} ubicada en latitud: {lat}°, longitud: {lon}° ")


def hemisferio(camaras):
    norte = 0
    for i in range(len(camaras)):
        lat, lon = camaras[i]
        if lat > 0:
            norte += 1

    print(f"la cantidad de camaras mirando el norte es: {norte}")


    





lista_camaras= solicitar_carga()
posiciones(lista_camaras)
hemisferio(lista_camaras)