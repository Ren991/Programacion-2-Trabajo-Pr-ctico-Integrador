from abc import ABC



class Usuarios(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia
    
    def __str__(self):
        pass

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contrasenia(self):
        return self.__contrasenia 
    

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self.__contrasenia = nueva_contrasenia

    
    def validar_credenciales(self, email_user, contrasenia_user):
          return self.__email == email_user and self.__contrasenia == contrasenia_user
        