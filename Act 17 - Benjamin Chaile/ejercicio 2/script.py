"""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor.
"""

paises=[]
Tmes=[]
aux=[]
suma =0
Temp=0

for x in range (4):
    valor2=str(input(f"ingrese el nombre del pais numero {x}: "))
    paises.append(valor2)
    for i in range (3):
        valor1=int(input(f"ingrese la temperatura media mensual numero {i} de {paises[x]}: "))
        Tmes.append(valor1)
        suma = suma + Tmes[i]
        promedio = suma / 3
    print(f"PAIS:  {paises[x]}.     TEMPERATURA DE LOS 3 ULTIMOS MESES: {Tmes}.    PROMEDIO TRIMESTRAL:  {promedio}")

    aux.append(promedio)
    Tmes=[]
    promedio = 0
    suma = 0

for x in range (4):
     if aux[x] > Temp:
        Temp = aux[x]
        nom = paises[x]
print(f"pais con mayor promedio: {nom}")

