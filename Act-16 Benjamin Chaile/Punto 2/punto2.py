"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.

"""
aux1 = 0
aux2 = 0
vendedores = []
ventas = []

for x in range(5):
    nombre = input("ingresar nombres de los vendedores: ")
    vendedores.append(nombre)
    venta= int(input("ingrese total de ventas del vendedor: "))
    ventas.append(venta)
for k in range(5):
    for x in range(4-k):
        if ventas[x]<ventas[x+1]:
            aux1=ventas[x]
            ventas[x]=ventas[x+1]
            ventas[x+1]=aux1
            aux2=vendedores[x]
            vendedores[x]=vendedores[x+1]
            vendedores[x+1]=aux2
print("Lista de vendedores y sus ventas ordenadas de mayor a menor")
for x in range(5):
    print(vendedores[x],ventas[x])
print("El vendedor que menos vendió fue: ",vendedores[4],"con un total de ventas de: ",ventas[4])
print("El vendedor que más vendió fue: ",vendedores[0],"con un total de ventas de: ",ventas[0])

