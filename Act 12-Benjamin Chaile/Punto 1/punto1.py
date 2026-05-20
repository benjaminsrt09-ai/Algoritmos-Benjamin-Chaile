#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
#informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

for i in range(10):
    nota = int(input("Ingrese la nota del alumno: "))
    if nota >= 7:
        print("El alumno tiene una nota mayor o igual a 7.")
    else:
        print("El alumno tiene una nota menor a 7")