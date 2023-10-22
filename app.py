from Estudiante import *
from Profesor import *
from Usuario import *
from Curso import *

usuarios = [ 
    
    Usuario("pipo","hola","pepe", "1234"),
    Usuario("prueba","prueba1","coco", "568")
]


estudiantes = [ # => Se Crean 4 Objetos de la clase estudiante
    Estudiante("Nicolas","Villalba","n@v", "1221",1221,2022),
    Estudiante("Rodrigo", "Diaz", "r@d", "4422", 4422, 2014),
    Estudiante("Casiano","Almeida","coco@321", "4321", 4321, 2011),
    Estudiante("Renzo", "Beccari", "r@c", "1234", 1234, 2023),
]

profesores = [ # => Se Crean 2 Objetos de la clase profesores
    Profesor("Mercedes","Valloni","m@v","m123","ingeniera","2012"),
    Profesor("Prueba","Profesor2","p@p","p123","Tecnico quimico","2022")
]

cursos = [ # => Se Crean 6 Objetos de la clase cursos
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
    
    #ESTA FUNCION DEPENDIENDO DE LA OPCION QUE INGRESA EL USUARIO (1 o 2) ITERA EN ARRAY DE PROFESORES O EN 
    #ARRAY DE ESTUDIANTES

    email_input = input("Ingresa tu email: ")
    contrasenia_input = input("Ingresa tu contraseña: ")

    if opcion == "1":
        # Buscar al usuario con el correo electrónico proporcionado
        usuario_encontrado = None
        for estudiante in estudiantes:
            if estudiante.validar_credenciales(email_input, contrasenia_input):#=> método para validar credenciales, el mismo se hereda de usuario
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
            if profesor.validar_credenciales(email_input, contrasenia_input): #=> método para validar credenciales, el mismo se hereda de usuario
                usuario_encontrado = profesor
                break

        if usuario_encontrado:           
            print(f'Bienvenido/a {profesor.nombre}!')
            ingresar_como_profesor(usuario_encontrado)          
            
        else:
            print("Credenciales inválidas. Acceso denegado.")

        
""""FIN AUTENTICACION USUARIO"""


#-----------------FUNCIONES ALUMNOS-----------------------------------------------------------------------------------#

def ingresar_como_alumno(usuario):# tomo como parametro el Objeto Estudiante     
    
    while True:
        print("\nSubmenú de Alumno:")
        print("1. Matricularse a un curso")
        print("2. Desmatricularse a un curso")
        print("3. Ver curso")
        print("4. Volver al menú principal")
        print(f"Cursos del usuario = {usuario.cursos}")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matricular_a_curso(usuario)
        elif opcion == "2":
           desmatricular_de_curso(usuario)
        elif opcion == "3":
            mostrar_cursos(usuario)
        elif opcion == "4":
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
                        usuario.matricular_en_curso(curso_seleccionado.nombre) # => Método para matricular el usuario a un curso
                        print("Se ha registrado correctamente su matriculación")

                    else:
                        print("Contraseña incorrecta")

                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")



def desmatricular_de_curso(usuario):
    print("Cursos en los que estás matriculado:")
    for i, curso in enumerate(usuario.cursos, 1):
        print(f"{i}. {curso}")

    while True:
        cursoIngresado = input("Ingrese el número del curso del que desea desmatricularse: ")
        if cursoIngresado.isdigit():
            cursoIngresado = int(cursoIngresado)
            if 1 <= cursoIngresado <= len(usuario.cursos):
                curso_seleccionado = usuario.cursos[cursoIngresado - 1]
                usuario.desmatricular_de_curso(curso_seleccionado) # => Se llama al método del objeto Estudiante para desmatricularse de curso.
                print(f"Te has desmatriculado de {curso_seleccionado}.")                
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")



def mostrar_cursos(usuario):
    cursos_matriculados = usuario.cursos # => Método para obtener cursos del usuario logueado.

    if not cursos_matriculados:
        print("No estás matriculado en ningún curso.")
    else:
        print("Cursos en los que estás matriculado:")
        for i, curso in enumerate(cursos_matriculados, 1):
            print(f"{i}. {curso}")

        while True:
            curso_info = input("Ingrese el número del curso al que desea ver (0 para salir): ")
            if curso_info.isdigit():
                curso_seleccionado = int(curso_info)
                if 1 <= curso_seleccionado <= len(cursos_matriculados):
                    curso = cursos_matriculados[curso_seleccionado - 1]
                    print(f"Nombre: {curso}")
                elif curso_seleccionado == 0:
                    break
                else:
                    print("Opción no válida. Por favor, ingrese un número válido o 0 para salir.")
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")


        

#----------------FIN FUNCIONES ALUMNOS-----------------------------------------------------------------------------------#


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
    
    cursoADictar = input("Ingrese el nombre del curso que desea dictar")

    if cursoADictar != "":
        nuevoCurso = Curso(cursoADictar) #=> Se crea nueva instancia de la clase Curso con el nombre que ingresa el usuario
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






