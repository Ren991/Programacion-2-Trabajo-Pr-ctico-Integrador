from Usuario import *
from Curso import *

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio:int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio
        self.__cursos = []
        

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    @anio_egreso.setter
    def anio_egreso(self, anio_egreso):
        self.__anio_egreso = anio_egreso
    
    @property
    def cursos(self) -> list:
        return self.__cursos   

    def dictar_curso(self, curso: Curso):
        self.cursos.append(curso)
    
    def __str__(self) -> str:
        return f"El profesor es: {self.nombre}"