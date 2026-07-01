"""Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea
el número de documento del alumno. Como valor almacenar una lista con
componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las
materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas."""

def cargar_alumnos():
    alumnos = {}
    for i in range(3):
        dni = int(input(f"Ingrese el DNI del alumno {i+1}: "))
        materias_notas = []
        

        continua = "s"
        while continua == "s":
            materia = input("Ingrese nombre de la materia: ")
            nota = int(input("Ingrese la nota: "))
            materias_notas.append((materia, nota))
            continua = input("¿Desea agregar otra materia? [s/n]: ")
        
        alumnos[dni] = materias_notas
    return alumnos

def listar_alumnos(alumnos):
    print("\nListado completo de alumnos y sus notas:")
    for dni in alumnos:
        print(f"\nDNI: {dni}")

        for materia, nota in alumnos[dni]:
            print(f"  Materia: {materia} - Nota: {nota}")

def consultar_alumno(alumnos):
    dni_consulta = int(input("\nIngrese el DNI del alumno a consultar: "))
    if dni_consulta in alumnos:
        print(f"Materias y notas para el DNI {dni_consulta}:")
        for materia, nota in alumnos[dni_consulta]:
            print(f"  {materia}: {nota}")
    else:
        print("El alumno con ese DNI no se encuentra registrado.")

diccionario_alumnos = cargar_alumnos()
listar_alumnos(diccionario_alumnos)
consultar_alumno(diccionario_alumnos)