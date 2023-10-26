import string, random

class Curso():

    codigo_actual = 0 
    __prox_cod = 1
    def __init__(self, nombre:str ):
        self.__prox_cod = 1
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()        
        self.__codigo = Curso.obtener_siguiente_codigo()

        

    @property
    def nombre(self):
        return self.__nombre
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @property
    def codigo(self):
        return self.__codigo
    
    @nombre.setter
    def nombre(self , nuevo_nombre):
        self.__nombre = nuevo_nombre

    @classmethod
    def obtener_siguiente_codigo(cls):
        cls.codigo_actual += cls.__prox_cod
        return cls.codigo_actual
    
    @classmethod
    def __generar_contrasenia(cls) -> str:
        passw = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(passw) for i in range(7))

    def __str__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"
    

    # Ejemplo de uso
curso1 = Curso("Curso de Matemáticas")
curso2 = Curso("Curso de Historia")

print(curso1)
print(curso2)
print(curso1.contrasenia_matriculacion)
print(curso2.contrasenia_matriculacion)
print(curso1.codigo)
print(curso2.codigo)