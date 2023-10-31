class Carrera():
    def __init__(self, nombre, cant_anios,cursos=None) -> None:
        self.__nombre= nombre
        self.__cant_anios= cant_anios
        self.__cursos = cursos if cursos is not None else []
        self.__estudiantes = []       

    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre) ->None:
        self.__nombre = nuevo_nombre
    
    @property
    def cant_anios(self):
        return self.__cant_anios
    
    @cant_anios.setter
    def cant_anios(self,nueva_cant_anios)-> None:
        self.__cant_anios = nueva_cant_anios
    
    @property
    def cursos(self):
        return self.__cursos
    
    @cursos.setter
    def cursos(self,nuevos_cursos)->list:
        self.__cursos = nuevos_cursos
    
    @property
    def estudiantes(self):
        return self.__estudiantes
    
    @estudiantes.setter

    def estudiantes(self,nuevos_estudiantes)->list:
        self.__estudiantes = nuevos_estudiantes
    
    def get_cantidad_materias(self) -> int:
        return len(self.cursos)
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Cantidad de años : {self.cant_anios}, Estudiantes: {self.estudiantes}"
    
    

        