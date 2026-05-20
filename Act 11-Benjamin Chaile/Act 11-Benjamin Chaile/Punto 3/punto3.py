#3. Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso
#contrario informar el producto y la división del primero respecto al segundo.

numero1 = int(input("ingrese un numero "))
numero2 = int(input("ingrese un numero "))

if numero1 > numero2:

    print("la suma de ambos es ")
    print(int(numero1 + numero2))
    print("y su diferencia es de ")    
    print(int(numero1 - numero2))

else:
    print("el producto de ambos numeros es de ")
    print(int(numero1 * numero2))
    print((numero1/numero2))

