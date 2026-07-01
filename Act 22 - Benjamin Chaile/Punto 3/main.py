"""Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos).Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos)."""

def cargar_registro():
    amenazas = {}
    for x in range(4):
        ip = input("Ingrese la dirección IP sospechosa (ej: 192.168.1.50): ")
        dispositivo = input("Ingrese el nombre del dispositivo: ")
        intentos = int(input("Ingrese la cantidad de intentos fallidos: "))
   
        amenazas[ip] = (dispositivo, intentos)
    return amenazas

def listar_amenazas(amenazas):
    print("\nLista de amenazas registradas:")
    for ip in amenazas:
  
        print(f"IP: {ip} - Dispositivo: {amenazas[ip][0]} - Intentos fallidos: {amenazas[ip][1]}")

def filtrar_bloqueos(amenazas):
    print("\nIPs que deben ser bloqueadas inmediatamente (más de 5 intentos):")
    for ip in amenazas:

        if amenazas[ip][1] > 5:
            print(f"Bloquear IP: {ip} - Pertenece a: {amenazas[ip][0]}")


registro_amenazas = cargar_registro()
listar_amenazas(registro_amenazas)
filtrar_bloqueos(registro_amenazas)