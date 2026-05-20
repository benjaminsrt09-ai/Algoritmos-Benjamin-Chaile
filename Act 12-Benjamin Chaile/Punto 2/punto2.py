#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.

personas = int(input("Ingrese la cantidad de personas: "))

suma = 0

for i in range(personas):
    altura = int(input("Ingrese la altura de la persona: ")) 
    suma += altura

promedio = suma / personas
print("La altura promedio de las personas es:")
print(promedio)
