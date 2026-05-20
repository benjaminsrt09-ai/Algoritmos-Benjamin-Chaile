#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
#el número es positivo, negativo o nulo (es decir cero)

numero = int(input("ingrese un numero "))

if numero > 0:
    print("el numero es positivo ")

if numero < 0:
        print("el numero es negativo ")

else:
    if numero == 0:
        print("el numero es de valor nulo ")