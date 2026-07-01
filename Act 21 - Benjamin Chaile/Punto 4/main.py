"""Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias."""

def cargar_candidatos():
    candidatos = []
    for x in range(3):
        nombre = input("Ingrese el nombre del candidato: ")
        provincias = []
  
        for y in range(2):
            nombre_provincia = input(f"Ingrese nombre de la provincia para {nombre}: ")
            votos = int(input(f"Ingrese cantidad de votos en {nombre_provincia}: "))
            provincias.append((nombre_provincia, votos))
        candidatos.append([nombre, provincias])
    return candidatos

def imprimir_total_votos(candidatos):
    print("Total de votos por candidato:")
    for candidato in candidatos:
        nombre = candidato[0]
        total_votos = 0
  
        for provincia in candidato[1]:
            total_votos = total_votos + provincia[1]
        print(f"Candidato: {nombre} - Total de votos: {total_votos}")

datos_electorales = cargar_candidatos()
imprimir_total_votos(datos_electorales)