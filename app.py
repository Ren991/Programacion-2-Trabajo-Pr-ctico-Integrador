#Se importan todas las clases
from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from datos import *

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
                opt_profesor = input("Ingrese (1) si desea registrarse como profesor o (2) para salir: ")
                if opt_profesor == "1":
                    registrar_nuevo_profesor(email_input)
                    break  # Sale del bucle si la opción es válida (1)
                elif opt_profesor == "2":
                    # El usuario eligió salir, puedes hacer algo aquí si es necesario
                    break
                else:
                    print("Opción no válida. Ingrese (1) para registrarse o (2) para salir.")
        else:
            print("Correo electrónico no encontrado. Debe darse de alta en alumnado.")



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
                    if usuario.carrera == cursoIngresado.carrera: #=> Se valida que la carrera del usuario y la carrera a la que pertenece el curso coincidan
                        print(f"No estás matriculado en {curso_seleccionado.nombre}.")
                        contra_user = input(f"Ingrese contraseña para matricularse a {curso_seleccionado.nombre} : ")     
                        
                        if contra_user == curso_seleccionado.contrasenia_matriculacion:
                            usuario.matricular_en_curso(curso_seleccionado.nombre) # => Método para matricular el usuario a un curso
                            print("Se ha registrado correctamente su matriculación")
                        else:
                            print("Contraseña incorrecta")
                    else: # => Si la carrera del usuario y la carrera del curso no coinciden se muestra msj de error
                        print(f"No se puede inscribir a ese curso porque no pertenece a: {usuario.carrera}")

                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

def desmatricular_de_curso(usuario):

    if not usuario.cursos:
        print("No estás matriculado en ningún curso.")
        return  # Salir de la función si no está matriculado en ningún curso
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
        for i, curso in enumerate(cursos_matriculados, 1): #=> Se enumeran los cursos matriculados.
            print(f"{i}. {curso}")

        while True:
            curso_info = input("Ingrese el número del curso al que desea ver (0 para salir): ")
            if curso_info.isdigit():#=> Se valida que el ingreso haya sido un Número
                curso_seleccionado = int(curso_info)#=> Se convierte a número el ingreso.
                if 1 <= curso_seleccionado <= len(cursos_matriculados):#=> Se valida que que el num esté entre el minimo y el maximo.
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
def ver_todos_cursos():
    if not cursos:
        print("No hay cursos disponibles en este momento.")
    else:
        for curso in cursos:
            print(f"Nombre del curso: {curso.nombre} , Carrera: Tecnicatura universitaria en programacion")

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






