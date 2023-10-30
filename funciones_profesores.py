from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from datos import *
from funciones_alumnos import *
from funciones_profesores import *


def registrar_nuevo_profesor(email_input):
    print("----REGISTRO NUEVO PROFESOR----")
    nombre= input("Ingrese su nombre : ")
    apellido= input("Ingrese apellido : ")
    contrasenia= input("Ingrese contrasenia : ")
    titulo= input("Ingrese su título : ")
    anio= int(input(f"Ingrese el año en que egresó de {titulo} : "))

    nuevo_profesor = Profesor(nombre,apellido,email_input,contrasenia,titulo,anio)

    profesores.append(nuevo_profesor)
    # nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio:int
    for profesor in profesores:
        print(f"Nombre: {profesor.nombre} {profesor.apellido}")
        print(f"Email: {profesor.email}")
        print(f"Contraseña: {profesor.contrasenia}")
        print(f"Título: {profesor.titulo}")


#----------------FUNCIONES PROFESORES------------------------------------------------------------------------------------#

"""INGRESO COMO PROFESOR"""
def ingresar_como_profesor(usuario):
    print(usuario.nombre)
    while True:
        print("\nSubmenú de Profesor:")
        print("1. Dictar curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            dictar_curso(usuario)
        elif opcion == "2":
            ver_cursos(usuario)
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def dictar_curso(usuario):


    cursosDictados = usuario.cursos    

    print("Seleccione una carrera:")
    for i, carrera in enumerate(carreras, 1):
        print(f"{i}. {carrera.nombre}")

    while True:
        seleccion = input("Ingrese el número de la carrera que desea seleccionar: ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(carreras):
                # El usuario ha seleccionado una carrera válida
                carrera_seleccionada = carreras[seleccion - 1]
                print(f"Ha seleccionado la carrera: {carrera_seleccionada.nombre}")
                break
            else:
                print("Número fuera de rango. Por favor, ingrese un número válido.")
        else:
            print("Entrada no válida. Por favor, ingrese un número válido.")

    cursoADictar = input("Ingrese el nombre del curso que desea dictar: ")

    if cursoADictar != "":
        nuevoCurso = Curso(cursoADictar,carrera_seleccionada) #=> Se crea nueva instancia de la clase Curso con el nombre que ingresa el usuario
        cursos.append(nuevoCurso)#=> Se appendea al array con todos los cursos

        usuario.dictar_curso(nuevoCurso) #=> Se usa el método de profesores dictar_curso 

        print("Se ha creado correctamente el curso")
        print(f"Nombre: {nuevoCurso.nombre}")
        print(f"Contraseña: {nuevoCurso.contrasenia_matriculacion}")

    for curso in cursos:
        print(f"Nombre del curso: {curso.nombre}")
        print(f"Contraseña de matriculación: {curso.contrasenia_matriculacion}")    
    for i, curso in enumerate(cursosDictados, 1):
            print(f"{i}. {curso}")

def ver_cursos(usuario):
    cursos_dictados = usuario.cursos  # Método para obtener cursos dictados por el profesor.

    if not cursos_dictados:
        print("No has creado ningún curso.")
    else:
        print("Cursos que has dictado:")
        for i, curso in enumerate(cursos_dictados, 1):
            print(f"{i}. {curso.nombre}")

        while True:
            curso_info = input("Ingrese el número del curso que desea ver (0 para salir): ")
            if curso_info.isdigit():
                curso_seleccionado = int(curso_info)
                if 1 <= curso_seleccionado <= len(cursos_dictados):
                    curso = cursos_dictados[curso_seleccionado - 1]
                    print(f"Nombre: {curso.nombre} , contraseña: {curso.contrasenia_matriculacion}")
                elif curso_seleccionado == 0:
                    break
                else:
                    print("Opción no válida. Por favor, ingrese un número válido o 0 para salir.")
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

#----------------FIN FUNCIONES PROFESORES------------------------------------------------------------------------------------#