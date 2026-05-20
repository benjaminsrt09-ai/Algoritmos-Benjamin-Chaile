"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.3
"""
sueldos = []
cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
for i in range(cantidad_empleados):
    sueldo = int(input(f"Ingrese el sueldo del empleado {i + 1}: "))
    sueldos.append(sueldo)
for i in range(len(sueldos)):
    for j in range(i + 1, len(sueldos)):
        if sueldos[i] > sueldos[j]:
            sueldos[i], sueldos[j] = sueldos[j], sueldos[i]
print("Lista de sueldos ordenada de menor a mayor:")
for sueldo in sueldos:
    print(sueldo)
