from Usuario import *
from Curso import *

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio:int):
        self.__titulo = titulo
        self.__anio_egreso = anio
        self.__cursos = []
        super().__init__(nombre, apellido, email, contrasenia)

    @property
    def titulo(self):
        return self.__titulo
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    @property
    def cursos(self) -> list:
        return self.__cursos   

    def dictar_curso(self, curso: Curso):
        self.cursos.append(curso)