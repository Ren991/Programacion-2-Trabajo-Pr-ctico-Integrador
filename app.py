#Se importan todas las clases
from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from datos import *
from funciones_alumnos import *
from funciones_profesores import *

def autenticar_usuario(opcion):
    #Esta función toma como parámetro la opcion del usuario (1 alumno , 2 profesor)
    #En funcion de eso se le pide el mail y luego valida que ese mail existe en el array de profesores o alumnos dependiendo elección del usuario
    #Si existe ese mail , se le solicita contraseña y luego se llama al método validar_credenciales.

    email_input = input("Ingresa tu email: ")

    usuario_encontrado = None
    arrayEstudiantes = estudiantes
    arrayProfesores = profesores
    if opcion == "1":
        for estudiante in arrayEstudiantes:
            if estudiante.email == email_input:
                usuario_encontrado = estudiante
                break
    elif opcion == "2":
        for profesor in arrayProfesores:
            if profesor.email == email_input:
                usuario_encontrado = profesor
                break

    if usuario_encontrado:
        contrasenia_input = input("Ingresa tu contraseña: ")
        if usuario_encontrado.validar_credenciales(email_input, contrasenia_input): # Se valida que el método validar_credenciales retorne true , sino muestra mensaje de error
            
            if opcion == "1":
                print(f'Bienvenido/a {estudiante.nombre}!')
                ingresar_como_alumno(usuario_encontrado)# Se llama al submenu de alumno
            elif opcion == "2":
                print(f'Bienvenido/a {profesor.nombre}!')
                ingresar_como_profesor(usuario_encontrado)# Se llama al submenu de profesor
        else:
            print("Error de ingreso. Credenciales inválidas.")
    else:
        if not usuario_encontrado and opcion == "2":
            print("Correo electrónico no encontrado")
            while True:
                opt_profesor = input("Ingrese código para registrarse como profesor : ")
                if opt_profesor.lower() == "admin": #=> Se utiliza el método lower para prevenir errores
                    registrar_nuevo_profesor(email_input)
                    break  # Sale del bucle si la opción es válida (1)
               
                else:
                    break
        else:
            print("Correo electrónico no encontrado. Debe darse de alta en alumnado.")

        
""""FIN AUTENTICACION USUARIO"""

def ver_todos_cursos():
    if not cursos:
        print("No hay cursos disponibles en este momento.")
    else:
       cursosOrdenados=sorted(cursos, key=lambda x: x.nombre)
       for curso in cursosOrdenados:
        print(f"Nombre del curso: {curso.nombre}, Carrera: {curso.carrera.nombre}")


def main_menu():
    while True:
        print("\nMenú de Usuario:")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1" or opcion == "2":
            autenticar_usuario(opcion)        
        elif opcion == "3":
            ver_todos_cursos()            
        elif opcion == "4":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main_menu() 






