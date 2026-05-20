"""

3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.

"""

aux1 = 0
aux2 = 0
atletas = []
tiempos = []
for x in range(5):
    nombre = input("ingresar nombres de los atletas: ")
    atletas.append(nombre)
    tiempo= int(input("ingrese el tiempo del atleta en segundos: "))
    tiempos.append(tiempo)
for k in range(5):
    for x in range(4-k):
        if tiempos[x]>tiempos[x+1]:
            aux1=tiempos[x]
            tiempos[x]=tiempos[x+1]
            tiempos[x+1]=aux1
            aux2=atletas[x]
            atletas[x]=atletas[x+1]
            atletas[x+1]=aux2
print("Lista de atletas y sus tiempos ordenados de menor a mayor")
for x in range(5):
    print(atletas[x],tiempos[x])
promedio = sum(tiempos)/len(tiempos)
print("El promedio de los tiempos es: ",promedio)
print("El atleta con mejor tiempo es: ",atletas[0],"con un tiempo de: ",tiempos[0])
print("El atleta con peor tiempo es: ",atletas[4],"con un tiempo de: ",tiempos[4])
print("Los atletas que superaron el promedio son: ")
for x in range(5):
    if tiempos[x]<promedio:
        print(atletas[x],"con un tiempo de: ",tiempos[x])
        