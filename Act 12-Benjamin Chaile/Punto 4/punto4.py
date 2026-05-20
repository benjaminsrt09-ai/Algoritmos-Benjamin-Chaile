#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.+

negativos = 0
positivos = 0
multiplos15 = 0
acumuladoPares = 0

for i in range(10):
    valor = int(input("Ingrese un valor entero: "))
    
    if valor < 0:
        negativos += 1
    else:
        if valor > 0:
            positivos += 1
    
    if valor % 15 == 0:
        multiplos_15 += 1
    
    if valor % 2 == 0:
        acumulado_pares += valor

print("Cantidad de valores ingresados negativos:", negativos)
print("Cantidad de valores ingresados positivos:", positivos)
print("Cantidad de múltiplos de 15:", multiplos_15)
print("Valor acumulado de los números ingresados que son pares:", acumulado_pares)