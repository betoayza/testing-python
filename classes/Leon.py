from classes.IAnimalActioner import IAnimalActioner
import zope.interface

@zope.interface.implementer(IAnimalActioner)
class Leon:
    def correr(self):
        print("El leon esta corriendo.")

    def realizar_sonido(self):
        print("El leon está rugiendo.")

    def comer(self):
        print("El leon está comiendo una zebra")