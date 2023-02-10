# ABC es la clase abstracta base de la bibilioteca estandar de python.
# ABC permite crear interfaces
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass # pass es para no ejecutar la funcion. Se usa cuando no hay implementacion.

    @abstractmethod
    def frenar(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass


# abc es la librerio o bibiloteca
# ABC es la clase
# abstractmethod es el método

# Las clases abstractas pueden también tener métodos concretos
# Estos se acceden en la clase implementadora mediante "super().<metodo()>"
# Las clases abstractas no pueden ser instanciadas, pero sí las subclases concretas

# Tanto con Clases Abstractas como con Interfaces se puede lograr el polimorfismo