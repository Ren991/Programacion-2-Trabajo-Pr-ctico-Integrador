from datetime import date
import random


class Archivo():
    def __init__(self,nombre,formato):

        self.__nombre = nombre        
        self.__fecha= self.generar_fecha_aleatoria()
        self.__formato = formato
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def formato(self):
        return self.__formato
    
    def generar_fecha_aleatoria(self): #=> Se creó este método para simular el ordenamiento de archivos por fecha.
        # Generar una fecha aleatoria en un rango de años, meses y días deseado
        year = random.randint(2000, 2023)  
        month = random.randint(1, 12)
        day = random.randint(1, 28) 

        #Con este método se excluirían los días 29-30-31. 
        
        return date(year, month, day)
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Fecha: {self.fecha} , Formato: {self.formato}"