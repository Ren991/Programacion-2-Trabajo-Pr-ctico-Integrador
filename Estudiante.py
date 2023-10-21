from Usuario import *


class Estudiante(Usuarios):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    @property
    def legajo(self):
        return self.__legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido} (Legajo: {self.legajo}, Año de inscripción: {self.anio_inscripcion_carrera})"

    def matricular_en_curso(self, curso):
        # Lógica para matricular al estudiante en un curso
        pass


""" class Estudiantes(Usuarios):
    def __init__(self, nombre:str, apellido:str, email:str, contrasenia:str,  num_legajo: int, anio_inscripcion_carrera: int):
       super().__init__(nombre, apellido, email, contrasenia)
       self.num_legajo = num_legajo
       self.anio_inscripcion_carrera = anio_inscripcion_carrera
    def __str__(self):
        return f"Estudiante: Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Legajo: {self.num_legajo}, Año de inscripción: {self.anio_inscripcion_carrera}"
    
    def matricular_en_curso(self, matricular_curso: str):
        self.matricular_curso = matricular_curso
    """
  