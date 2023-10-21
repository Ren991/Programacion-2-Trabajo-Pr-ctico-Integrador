from Estudiante import *
from Profesor import *
from Usuario import *

usuarios = [
    Usuarios("pepe","coco","pepe@123", "1234"),
    Usuarios("coco","sinApellido","coco@321", "4321"),
    Usuarios("pipo","hola","pepe", "1234"),
    Usuarios("prueba","prueba1","coco", "568")
]



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
            print("Credenciales válidas. Acceso concedido.")
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
            print("Matriculando a un curso...")
        elif opcion == "2":
            print("Viendo curso...")
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


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






