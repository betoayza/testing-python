from classes.IAnimalActioner import IAnimalActioner
import zope.interface

@zope.interface.implementer(IAnimalActioner)
class Perro:

    # def __init__(self, recorridos):
    #    self.recorridos = recorridos

    def correr(self):
        # print(1+1)
        print("El perro esta corriendo!")
     
    def realizar_sonido(self):
        print("El perro está ladrando")

    def comer(self):
        print("El perro está comiendo")



# una clase no necesita __init__, salvo que se quieran inicializar atributos
