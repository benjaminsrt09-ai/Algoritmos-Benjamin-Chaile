"""
4. Cargar por teclado y almacenar en una lista las alturas de 5 personas
(valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más
altas que el promedio y cuántas más bajas.

"""

alturas = []

for i in range(5):
    altura = float(input("Ingrese la altura de la persona: "))
    alturas.append(altura)

suma = 0
for altura in alturas:
    suma += altura

promedio = suma / len(alturas)

print("El promedio de las alturas es:", promedio)

altas = 0
bajas = 0

for altura in alturas:
    if altura > promedio:
        altas += 1
    elif altura < promedio:
        bajas += 1

print("Personas más altas que el promedio:", altas)
print("Personas más bajas que el promedio:", bajas)