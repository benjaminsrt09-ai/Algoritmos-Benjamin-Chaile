"""
3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto.
"""

def pedir():                                                 
    return int(input("ingrese un numero"))

def sumar(a=0, b=0, c=0, d=0, e=0):                                               
    return a + b + c + d + e 

def variacion ():

    variable = int(input("ingrese la cantidad de numeros que desea sumar (solamente de 2 a 5): "))
    while variable < 2 or variable > 5:
        print("Error: El número debe estar entre 2 y 5.")
        variable = int(input("Por favor, ingrese una cantidad válida (de 2 a 5): "))
    
    n1 = pedir()
    n2 = pedir()
    

    if variable == 2:
        resultado = sumar(n1, n2)

    elif variable == 3:
        n3 = pedir()
        resultado = sumar(n1,n2,n3)

    elif variable == 4:
        n3 = pedir()
        n4 = pedir()
        resultado = sumar(n1,n2,n3,n4)

    elif variable == 5:
        n3 = pedir()
        n4 = pedir()
        n5 = pedir()
        resultado = sumar(n1,n2,n3,n4,n5)

        
    print("la suma total es: ", resultado)



variacion()