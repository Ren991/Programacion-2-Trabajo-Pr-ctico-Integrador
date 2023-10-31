import string, random
from Archivo import *

class Curso():

    codigo_actual = 0 
    __prox_cod = 1
    def __init__(self, nombre:str , carrera: str):
        self.__prox_cod = 1
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()        
        self.__codigo = Curso.obtener_siguiente_codigo()
        self.__carrera = carrera
        self.__archivos = []         

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self , nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self,nueva_contrasenia_matriculacion)->str:
        self.__contrasenia_matriculacion = nueva_contrasenia_matriculacion
    
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,nuevo_codigo)->str:
        self.__codigo = nuevo_codigo
    
    @property
    def carrera(self):
        return self.__carrera
    @carrera.setter
    def carrera(self,nueva_carrera)->str:
        self.__carrera = nueva_carrera    

    @property
    def archivos(self):
        return self.__archivos
    
    @archivos.setter
    def archivos(self, nuevo_archivo):
        self.__archivos = nuevo_archivo    

    @property
    def cantidad_archivos(self):
        return len(self.__archivos)        
    
    def nuevo_archivo(self,archivo):
        self.__archivos.append(archivo)

    @classmethod
    def obtener_siguiente_codigo(cls):
        cls.codigo_actual += cls.__prox_cod
        return cls.codigo_actual
    
    @classmethod
    def __generar_contrasenia(cls) -> str:
        passw = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(passw) for i in range(7))

    def __str__(self):
         return f"Nombre: {self.nombre}, Carrera: {self.carrera}"
    
