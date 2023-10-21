from Usuario import *
from Curso import *

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio:int):
        self.__titulo = titulo
        self.__anio_egreso = anio
        self.__mis_cursos = []
        super().__init__(nombre, apellido, email, contrasenia)

    @property
    def titulo(self):
        return self.__titulo
    @property
    def anio_egreso(self):
        return self.__anio_egreso

    def dictar_curso(self, curso: Curso):
        self.__mis_cursos.append(curso)