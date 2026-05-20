#1. Definir una lista que almacene por asignación los nombres de 5 personas.
#Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.

nombres = ["Benjamin","Luciano","Fabian","Sebastian","Virginia"]

x=0
contador=0
for i in range(5):
    if len(nombres[x]) >= 5:
        contador += 1
print(f"Cantidad de nombres con 5 o más caracteres: {contador}")