"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""

nombres=[]
dias=[]

for x in range (3):
    valor2=str(input(f"ingrese el nombre del empleado numero {x}: "))
    nombres.append(valor2)
    valor1=int(input(f"ingrese la cantidad de dias que {nombres[x]} faltó: "))
    dias.append(valor1)

for x in range (3):
    print(f"NOMBRE:  {nombres[x]}.   DIAS QUE FALTÓ: {dias[x]}")



if dias[0] < dias[1] and dias[0]< dias[2]:
    print(f"{nombres[0]} es quien menos faltas tiene.")

elif dias[0] > dias[1] and dias[1]< dias[2]:
    print(f"{nombres[1]} es quien menos faltas tiene.")

elif dias[0] > dias[2] and dias[2] < dias[1]:
    print(f"{nombres[2]} es quien menos faltas tiene.")