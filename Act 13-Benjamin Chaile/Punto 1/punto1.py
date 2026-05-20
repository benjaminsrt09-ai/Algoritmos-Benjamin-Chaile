#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
#empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
#programa deberá informar el importe que gasta la empresa en sueldos al personal.

empleadoss = int(input("Ingrese el número de empleados: "))
sueldo = 0
sueldos100_300 = 0
sueldosMas_300 = 0
total_sueldos = 0

for i in range(empleadoss):
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    total_sueldos += sueldo
    if 100 <= sueldo <= 300:
        sueldos100_300 += 1
    elif sueldo > 300:
        sueldosMas_300 += 1

print("Empleados que cobran entre $100 y $300: ")
print(sueldos100_300)
print("Empleados que cobran más de $300: ")
print(sueldosMas_300)
print("Total gastado en sueldos: ")
print(total_sueldos)
