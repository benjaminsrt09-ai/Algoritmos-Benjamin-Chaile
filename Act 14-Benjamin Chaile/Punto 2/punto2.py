#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas. Imprimir las dos listas de sueldos.
print ("turno mañana")
sueldosM = []
for i in range(4):
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    sueldosM.append(sueldo)
print ("turno tarde")
sueldosT = []
for i in range(4):
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    sueldosT.append(sueldo)
print ("sueldos turno mañana: ", sueldosM)
print ("sueldos turno tarde: ", sueldosT)