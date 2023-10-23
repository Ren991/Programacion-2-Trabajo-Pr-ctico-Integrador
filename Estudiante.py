from Usuario import *


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera)-> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__cursos = []

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido} (Legajo: {self.legajo}, Año de inscripción: {self.anio_inscripcion_carrera})"

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self, nuevo_legajo):
        self.__legajo = nuevo_legajo


    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion
        
    @property
    def cursos(self) -> list:
        return self.__cursos      
    

    def matricular_en_curso(self, curso) -> None:
        self.cursos.append(curso)

    def desmatricular_de_curso(self, curso) -> None:    
        self.cursos.remove(curso)
       



  