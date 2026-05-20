"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.

"""
aux1 = 0
aux2 = 0
nombres = []
notas = []

for x in range(6):
    nombre = input("ingresar nombres de los alumnos: ")
    nombres.append(nombre)
    nota= int(input("ingrese nota del alumno: "))
    notas.append(nota)

for k in range(6):
    for x in range(4-k):
        if notas[x]<notas[x+1]:
            aux1=notas[1]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=nombres[x]
            nombres[x]=nombres[x+1]
            nombres[x+1]=aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor")
for x in range(6):
    print(nombres[x],notas[x])