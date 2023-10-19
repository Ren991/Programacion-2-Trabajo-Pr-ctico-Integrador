from Usuario import *


class Profesores(Usuarios):
   def __init__(self, titulo: str, anio_egreso: int):
       self.titulo = titulo
       self.anio_egreso = anio_egreso
       super().__init__()