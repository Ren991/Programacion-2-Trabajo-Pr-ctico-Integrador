import string, random

class Curso():
    def __init__(self, nombre:str ):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        

    @property
    def nombre(self):
        return self.__nombre
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @nombre.setter
    def nombre(self):
        return self.__nombre
    
    @classmethod
    def __generar_contrasenia(cls) -> str:
        passw = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(passw) for i in range(7))

    def __str__(self):
        return f"Nombre: {self.__nombre}"

