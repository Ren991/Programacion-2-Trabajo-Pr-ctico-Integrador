from abc import ABC


class Usuarios(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia
    
    def __str__(self):
        pass

    
    def validar_credenciales(self, email, contrasenia):
        pass