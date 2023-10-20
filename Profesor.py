from Usuario import *



class Profesores(Usuarios):
   def init(self, nombre:str, apellido:str, email:str, contrasenia:str, titulo: str, anio_egreso: int):
       super().init(nombre, apellido , email, contrasenia)
       self.titulo = titulo
       self.anio_egreso = anio_egreso
   def str(self):
        return f"Profesor: Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Legajo: {self.titulo}, Año de inscripción: {self.anio_egreso}"
   def dictar_curso(self, dictar_curso):
       self.dictar_curso = dictar_curso