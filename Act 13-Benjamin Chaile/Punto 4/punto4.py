#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
#en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
#cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de
#puntos a procesar.

cantidad = int(input("¿Cuántos puntos desea ingresar? "))

cuadrante1 = 0
cuadrante2 = 0
cuadrante3 = 0
cuadrante4 = 0

for i in range(cantidad):
    print("Punto ")
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        cuadrante1 += 1

    if x < 0 and y > 0:
        cuadrante2 += 1

    if x < 0 and y < 0:
        cuadrante3 += 1

    if x > 0 and y < 0:
        cuadrante4 += 1

print("Cantidad de puntos en el primer cuadrante:", cuadrante1)
print("Cantidad de puntos en el segundo cuadrante:", cuadrante2)
print("Cantidad de puntos en el tercer cuadrante:", cuadrante3)
print("Cantidad de puntos en el cuarto cuadrante:", cuadrante4)