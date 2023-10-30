import string, random

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
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def carrera(self):
        return self.__carrera

    @property
    def archivos(self):
        return self.__archivos
    
    @nombre.setter
    def nombre(self , nuevo_nombre):
        self.__nombre = nuevo_nombre

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
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}, Carrera: {self.carrera}, Cantidad archivos:{self.cantidad_archivos}"
    

