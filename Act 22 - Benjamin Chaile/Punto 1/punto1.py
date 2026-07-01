"""Crear un diccionario en Python que defina como clave el número de documento de
una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento."""

def cargar_personas():
    personas = {}
    for x in range(4):
        documento = int(input("Ingrese el número de documento: "))
        nombre = input("Ingrese el nombre de la persona: ")

        personas[documento] = nombre
    return personas

def listar_diccionario(personas):
    print("Listado completo del diccionario:")

    for documento in personas:
        print(f"Documento: {documento} - Nombre: {personas[documento]}")

def consultar_nombre(personas):
    doc_consulta = int(input("Ingrese el número de documento a consultar: "))

    if doc_consulta in personas:
        print("El nombre de la persona es:", personas[doc_consulta])
    else:
        print("El documento ingresado no existe en el diccionario.")


diccionario_personas = cargar_personas()
listar_diccionario(diccionario_personas)
consultar_nombre(diccionario_personas)
