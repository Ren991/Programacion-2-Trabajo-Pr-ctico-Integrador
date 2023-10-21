from Estudiante import *
from Profesor import *
from Usuario import *
from Curso import *

usuarios = [
    
    Usuario("pipo","hola","pepe", "1234"),
    Usuario("prueba","prueba1","coco", "568")
]

estudiantes = [
    Estudiante("Nicolas","Villalba","n@v", "1221",1221,2022),
    Estudiante("Rodrigo", "Diaz", "r@d", "4422", 4422, 2014),
    Estudiante("Casiano","Almeida","coco@321", "4321", 4321, 2011),
    Estudiante("Renzo", "Beccari", "r@c", "1234", 1234, 2023),
]

profesores = [
    Profesor("Mercedes","Valloni","m@v","m123","ingeniera","2012"),
    Profesor("Prueba","Profesor2","p@p","p123","Tecnico quimico","2022")
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



""""AUTENTICACION USUARIO"""

def autenticar_usuario(opcion):
    
    #ESTA FUNCION DEPENDIENDO DE LA OPCION QUE INGRESA EL USUARIO ITERA EN EL ARRAY DE PROFESORES O EN 
    #ARRAY DE ESTUDIANTES

    email_input = input("Ingresa tu email: ")
    contrasenia_input = input("Ingresa tu contraseña: ")

    if opcion == "1":
        # Buscar al usuario con el correo electrónico proporcionado
        usuario_encontrado = None
        for estudiante in estudiantes:
            if estudiante.validar_credenciales(email_input, contrasenia_input):
                usuario_encontrado = estudiante
                break

        if usuario_encontrado:           
            print(f'Bienvenido/a {estudiante.nombre}!')                   
            ingresar_como_alumno(usuario_encontrado) #Paso como parámetro el Objeto Estudiante
        else:
            print("Credenciales inválidas. Acceso denegado.")

    elif opcion == "2":
        usuario_encontrado = None
        for profesor in profesores:
            if profesor.validar_credenciales(email_input, contrasenia_input):
                usuario_encontrado = profesor
                break

        if usuario_encontrado:           
            print(f'Bienvenido/a {profesor.nombre}!')
                      
            
        else:
            print("Credenciales inválidas. Acceso denegado.")

        
""""FIN AUTENTICACION USUARIO"""


#-----------------FUNCIONES ALUMNOS-----------------------------------------------------------------------------------#

def ingresar_como_alumno(usuario):# tomo como parametro el Objeto Estudiante 
    print(usuario.nombre)
    
    while True:
        print("\nSubmenú de Alumno:")
        print("1. Matricularse a un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        print(f"Cursos del usuario = {usuario.cursos}")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matricular_a_curso(usuario)
        elif opcion == "2":
            print("Viendo curso...")
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        


def matricular_a_curso(usuario):
    cursos_disponibles = cursos 

    print("Cursos disponibles:")
    for i, curso in enumerate(cursos_disponibles, 1): #Enumerate es un método , crea una tupla para cada elemento, con el índice y el nombre.
        print(f"{i} {curso.nombre}") # Muestra el índice y el nombre

    while True:
        cursoIngresado = input("Ingrese el número del curso al que desea matricularse: ")
        if cursoIngresado.isdigit(): # isDigit retorna true en caso de que sea numero y en caso de que sea string devuelve false.
            cursoIngresado = int(cursoIngresado)
            if 1 <= cursoIngresado <= len(cursos_disponibles): # valida que el numero que ingrese el usuario este entre el 1 y el último num de curso.
                curso_seleccionado = cursos_disponibles[cursoIngresado - 1]
                
                if curso_seleccionado.nombre in usuario.cursos:
                    # El usuario ya se matriculo en ese curso
                    print(f"Ya estás matriculado en {curso_seleccionado.nombre}.")
                else:
                    # El usuario no está matriculado en el curso
                    print(f"No estás matriculado en {curso_seleccionado.nombre}.")
                    contra_user = input(f"Ingrese contraseña para matricularse a {curso_seleccionado.nombre}")     
                    
                    if contra_user == curso_seleccionado.contrasenia_matriculacion:
                        usuario.matricular_en_curso(curso_seleccionado.nombre)
                        print("Se ha registrado correctamente su matriculación")

                    else:
                        print("Contraseña incorrecta")

                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")



#----------------FIN FUNCIONES ALUMNOS-----------------------------------------------------------------------------------#


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






