#4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
#mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un
#número entero)

numero = int(input("ingrese un numero positivo de uno o dos digitos "))

if numero < 9 :
    print("el numero es de un digito ")

else :
    print("el numero es de dos digitos ")

