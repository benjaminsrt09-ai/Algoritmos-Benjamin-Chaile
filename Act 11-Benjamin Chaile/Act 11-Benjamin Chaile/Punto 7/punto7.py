#7. Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor
#y el menor de ellos)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))


mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3


if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3


print("El valor mayor es ")
print(mayor)
print("El valor menor es ")
print(menor)