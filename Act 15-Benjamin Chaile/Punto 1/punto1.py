"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o
igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente"
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda "Muy Bueno".

"""
alumnos = []
notas = []

for i in range(4):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))
    alumnos.append(nombre)
    notas.append(nota)

condiciones = []
for nota in notas:
    if nota >= 8:
        condiciones.append("Muy Bueno")
    elif nota >= 4:
        condiciones.append("Bueno")
    else:
        condiciones.append("Insuficiente")

print("Listado de alumnos:")
for i in range(4):
    print(f"Nombre: {alumnos[i]}, Nota: {notas[i]}, Condición: {condiciones[i]}")

muyBuenos = condiciones.count("Muy Bueno")
print(f"Cantidad de alumnos con condición 'Muy Bueno': {muyBuenos}")