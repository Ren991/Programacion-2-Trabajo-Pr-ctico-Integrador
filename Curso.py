from Usuario import *

import random
import string

class Curso:
    def __init__(self, nombre: str, contrasenia_matriculacion=None):
        self._nombre = nombre
        if contrasenia_matriculacion is None:
            contrasenia_matriculacion = self.generar_contrasenia()
        self._contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self):
        return f"Curso: Nombre: {self._nombre}, Contraseña de Matriculación: {self._contrasenia_matriculacion}"

    def generar_contrasenia(self):
        contrasenia = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        return contrasenia

# Nombres de cursos específicos
nombres_cursos = ["Lengua", "Matemáticas", "Física", "Química", "Historia"]

# Crear una lista de cursos con nombres específicos
cursos = [Curso(nombre) for nombre in nombres_cursos]

# Mostrar información de los cursos
for curso in cursos:
    print(curso)

print(cursos[1])

