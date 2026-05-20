#2. Calcular el sueldo mensual de un operario conociendo la cantidad de horas
#trabajadas y el valor por hora.

horasTrabajadas=int(input("ingrese la cantidad de horas trabajadas por día "))
valorDeHora=int(input("ingrese el valor por hora trabajada "))
sueldo=(horasTrabajadas * valorDeHora)*30
sueldo=int(sueldo)

print("su sueldo mensual es de ")
print(sueldo)

