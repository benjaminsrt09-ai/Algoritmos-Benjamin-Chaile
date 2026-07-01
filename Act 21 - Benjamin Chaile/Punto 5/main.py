"""Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15."""

def cargar_productos():
    productos = []
    for x in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio: "))
        productos.append((nombre, precio))
    return productos

def listar_productos(productos):
    print("Listado de productos y precios:")
    for producto in productos:
        print(f"Producto: {producto[0]} - Precio: {producto[1]}")

def imprimir_rango_precios(productos):
    print("Productos con precio entre 10 y 15:")
    for producto in productos:
        if producto[1] >= 10 and producto[1] <= 15:
            print(f"Producto: {producto[0]} - Precio: {producto[1]}")

lista_productos = cargar_productos()
listar_productos(lista_productos)
imprimir_rango_precios(lista_productos)