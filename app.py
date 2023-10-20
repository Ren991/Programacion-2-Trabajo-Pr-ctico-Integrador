from Estudiante import *
from Profesor import *
from Usuario import *

alumnos = [
    {
        "mail": "pepe@123",
        "contrasenia": "1234"
    },
    {
        "mail": "coco@321",
        "contrasenia": "4321"
    }
]

profesores = [
    {
        "mail": "pepe",
        "contrasenia": "1234"
    },
    {
        "mail": "coco",
        "contrasenia": "568"
    }
]

""""AUTENTICACION USUARIO"""
def autenticar_usuario(opcion):
    emailUser = input("Ingrese mail por favor: ")
    encontrado = False  

    if opcion == "1":     
        

        for alumno in alumnos:
            if alumno["mail"] == emailUser:
                contraseniaUser = input("Ahora ingrese la contraseña: ")
                if contraseniaUser == alumno["contrasenia"]:
                    ingresar_como_alumno()
                    encontrado = True  
                    break  
                else:
                    print("Contraseña incorrecta")
                    encontrado = True  
                    break  

            
    elif opcion == "2":
        

        for profesor in profesores:
            if profesor["mail"] == emailUser:
                contraseniaUser = input("Ahora ingrese la contraseña: ")
                if contraseniaUser == profesor["contrasenia"]:
                    ingresar_como_profesor()
                    encontrado = True  
                    break  
                else:
                    print("Contraseña incorrecta")
                    encontrado = True  
                    break  

        if not encontrado:
            print("Mail inválido")

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






