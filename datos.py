#ARCHIVO PARA LLENAR LOS DATOS DEL PROGRAMA
from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from Archivo import *
from Carrera import *

estudiantes = [ # => Se Crean 4 Objetos de la clase estudiante
    Estudiante("Nicolas","Villalba","n@v", "1221",1221,2022,"Tecnicatura universitaria en programacion"),
    Estudiante("Rodrigo", "Diaz", "r@d", "4422", 4422, 2014,"Tecnicatura universitaria en programacion"),
    Estudiante("Casiano","Almeida","coco@321", "4321", 4321, 2011,"Tecnicatura universitaria en programacion"),
    Estudiante("Renzo", "Beccari", "r@c", "1234", 1234, 2023,"Tecnicatura universitaria en programacion"),
]
profesores = [ # => Se Crean 2 Objetos de la clase profesores
    Profesor("Mercedes","Valloni","m@v","m123","ingeniera","2012"),
    Profesor("Prueba","Profesor2","p@p","p123","Tecnico quimico","2022")
]
cursos = [
    
]
""" cursos= [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II"),
    Curso("Calculo I"),
    Curso("Precalculo II"),
    Curso("Algebra I"),
    Curso("Calculo Matemático II"),
    Curso("Quimica I"),
    Curso("Fisica II")

]
cursosTecProg = [ # => Se Crean 6 Objetos de la clase cursos
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]

cursosIngenierias = [
    Curso("Calculo I"),
    Curso("Precalculo II"),
    Curso("Algebra I"),
    Curso("Calculo Matemático II"),
    Curso("Quimica I"),
    Curso("Fisica II")
] """

carreras = [ #=> Se crean las Instancias de carreras pero sin cursos inc
    Carrera("Tecnicatura universitaria en programacion",2),
    Carrera("Ingenieria en sistemas",6),
    Carrera("Ingenieria mecánica",6),
    Carrera("ingenieria quimica",6)
]

for carrera in carreras:
    print(f"Carrera: {carrera.nombre} (Duración: {carrera.cant_anios} años)")
    print("Cursos:")
    for curso in carrera.cursos:
        print(f"  - {curso.nombre}")
    print("\n")

for estudiante in estudiantes:
    print(f'Estudiante: {estudiante.nombre} {estudiante.apellido}')
    print(f'Email: {estudiante.email}')
    print(f'Legajo: {estudiante.legajo}')
    print(f'Año de inscripción: {estudiante.anio_inscripcion_carrera}')
    if estudiante.carrera:
        print(f'Carrera inscripta: {estudiante.carrera}')
    else:
        print('No inscrito en ninguna carrera')
    print('\n')