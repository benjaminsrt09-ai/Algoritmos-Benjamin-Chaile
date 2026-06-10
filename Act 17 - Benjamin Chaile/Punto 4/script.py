"""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""

nombres=[]
sueldos=[]

n=int(input("ingrese la cantidad de empleados: "))

for x in range (n+1):
    valor2=str(input(f"ingrese el nombre del empleado numero {x}: "))
    nombres.append(valor2)
    valor1=int(input(f"ingrese el sueldo de {nombres[x]}: "))
    sueldos.append(valor1)

    if sueldos [x] > 10000:
        nombres.pop(x)
        sueldos.pop(x)

print(nombres)
print(sueldos)
