"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)

"""

aux1 = 0
aux2 = 0
docentes = []
puntajes = []

for x in range(6):
    nombre = input("ingresar nombres de los docentes: ")
    docentes.append(nombre)
    puntaje= int(input("ingrese el puntaje promedio del docente: "))
    puntajes.append(puntaje)
for k in range(6):
    for x in range(5-k):
        if puntajes[x]<puntajes[x+1]:
            aux1=puntajes[x]
            puntajes[x]=puntajes[x+1]
            puntajes[x+1]=aux1
            aux2=docentes[x]
            docentes[x]=docentes[x+1]
            docentes[x+1]=aux2
print("Lista de docentes y sus puntajes ordenados de mayor a menor")
for x in range(6):
    print(docentes[x],puntajes[x])
print("El docente con la calificación más alta es: ",docentes[0],"con un puntaje de: ",puntajes[0])
print("El docente con la calificación más baja es: ",docentes[5],"con un puntaje de: ",puntajes[5])
aprobados = 0
desaprobados = 0
for x in range(6):
    if puntajes[x]>=6:
        aprobados+=1
    else:
        desaprobados+=1
print("Cantidad de docentes aprobados: ",aprobados)
print("Cantidad de docentes desaprobados: ",desaprobados)

