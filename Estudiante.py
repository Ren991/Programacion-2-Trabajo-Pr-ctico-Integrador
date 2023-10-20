from Usuario import *




class Estudiantes(Usuarios):
    def __init__(self, nombre:str, apellido:str, email:str, contrasenia:str,  num_legajo: int, anio_inscripcion_carrera: int):
       super().__init__(nombre, apellido, email, contrasenia)
       self.num_legajo = num_legajo
       self.anio_inscripcion_carrera = anio_inscripcion_carrera
    def __str__(self):
        return f"Estudiante: Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Legajo: {self.num_legajo}, Año de inscripción: {self.anio_inscripcion_carrera}"
    
    def matricular_en_curso(self, matricular_curso: str):
        self.matricular_curso = matricular_curso
   
  