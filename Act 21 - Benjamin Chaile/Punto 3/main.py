"""
Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [["juan";,(2000,3000,4233)] , ["ana",(3444,1000,5333)] , etc. ]"""

def cargar_empleados():
    empleados = []
    for x in range(5):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo1 = int(input("Ingrese primer sueldo: "))
        sueldo2 = int(input("Ingrese segundo sueldo: "))
        sueldo3 = int(input("Ingrese tercer sueldo: "))
        empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])
    return empleados

def imprimir_total_cobrado(empleados):
    print("Monto total cobrado por cada empleado:")
    for empleado in empleados:
        total = empleado[1][0] + empleado[1][1] + empleado[1][2]
        print(f"{empleado[0]}: {total}")

def imprimir_ingreso_trimestral_mayor(empleados):
    print("Empleados con ingreso trimestral mayor a 10000:")
    for empleado in empleados:
        total = empleado[1][0] + empleado[1][1] + empleado[1][2]
        if total > 10000:
            print(empleado[0])


lista_empleados = cargar_empleados()
imprimir_total_cobrado(lista_empleados)
imprimir_ingreso_trimestral_mayor(lista_empleados)