from abc import ABC, abstractmethod 



class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
    
    @abstractmethod
    def __str__(self):
        return f" Nombre: {self._nombre}, Apellido: {self._apellido}, Email: {self._email}"

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def email(self):
        return self._email
    
    @property
    def contrasenia(self):
        return self._contrasenia 
    

    @nombre.setter
    def nombre(self, nombre)->str:
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido)->str:
        self._apellido = apellido

    @email.setter
    def email(self,nuevo_email)->str:
        self.__email = nuevo_email

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self._contrasenia = nueva_contrasenia

    
    def validar_credenciales(self, email_user, contrasenia_user):
          return self._email == email_user and self._contrasenia == contrasenia_user
        