from Estudiante import *
from Profesor import *
from Usuario import *
from Curso import *

usuarios = [
    Usuarios("pepe","coco","pepe@123", "1234"),
    Usuarios("coco","sinApellido","coco@321", "4321"),
    Usuarios("pipo","hola","pepe", "1234"),
    Usuarios("prueba","prueba1","coco", "568")
]

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]

for curso in cursos:
    print(f"Nombre del curso: {curso.nombre}")
    print(f"Contraseña de matriculación: {curso.contrasenia_matriculacion}")

contrasenia_ingresada = input("Ingresa la contraseña para el curso de Ingles I: ")


for curso in cursos:
    if curso.nombre == "Ingles I":
        if contrasenia_ingresada == curso.contrasenia_matriculacion:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
        break
else:
    
    print("Curso de Química no encontrado.")




""""AUTENTICACION USUARIO"""
def autenticar_usuario(opcion):
    email_input = input("Ingresa tu email: ")
    contrasenia_input = input("Ingresa tu contraseña: ")

    if opcion == "1":
        # Buscar al usuario con el correo electrónico proporcionado
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.validar_credenciales(email_input, contrasenia_input):
                usuario_encontrado = usuario
                break

        if usuario_encontrado:           
            print(f'Bienvenido/a {usuario.nombre}!')
            ingresar_como_alumno()
        else:
            print("Credenciales inválidas. Acceso denegado.")        
        
""""FIN AUTENTICACION USUARIO"""

""""INGRESO COMO ALUMNO"""

def ingresar_como_alumno():
    while True:
        print("\nSubmenú de Alumno:")
        print("1. Matricularse a un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matricular_a_curso()
        elif opcion == "2":
            print("Viendo curso...")
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def matricular_a_curso():
    cursos_disponibles = cursos 

    print("Cursos disponibles:")
    for i, curso in enumerate(cursos_disponibles, 1): #Enumerate es un método , crea una tupla para cada elemento, con el índice y el nombre.
        print(f"{i} {curso.nombre}") # Muestra el índice y el nombre

    while True:
        cursoIngresado = input("Ingrese el número del curso al que desea matricularse: ")
        if cursoIngresado.isdigit():
            cursoIngresado = int(cursoIngresado)
            if 1 <= cursoIngresado <= len(cursos_disponibles):
                curso_seleccionado = cursos_disponibles[cursoIngresado - 1]
                print(f"Ha seleccionado matricularse en {curso_seleccionado.nombre}.")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


matricular_a_curso()



""""FIN INGRESO COMO ALUMNO"""


"""INGRESO COMO PROFESOR"""
def ingresar_como_profesor():
    while True:
        print("\nSubmenú de Profesor:")
        print("1. Dictar curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Dictar un curso...")
        elif opcion == "2":
            print("Viendo curso...")
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


""""FIN INGRESO COMO PROFESOR"""


def main_menu():
    while True:
        print("\nMenú de Usuario:")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            autenticar_usuario(opcion)
        elif opcion == "2":
            autenticar_usuario(opcion)
            
        elif opcion == "3":
            print("Lista de cursos:")
            
        elif opcion == "4":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main_menu()






