import zope.interface

# Interfaz para definir signaturas de metodos para un animal


class IAnimalActioner(zope.interface.Interface):

    """Esta es la documentacion de una interfaz para acciones de un animal"""

    # metodos y atributos
    # el atributo solo puede ser un doc string
    x = zope.interface.Attribute(
        "El atributo de una interfaz solo tiene fines documentativos")

    def correr(self):
        pass

    def realizar_sonido(self):
        pass

    def comer(self):
        pass


# Las interfaces tienen una semantica más estricta
# y mejor mensajes de error que abc
# 'Interface' es la interfaz padre de todas las interfaces

# Las interfaces no son clases, por lo que no se puede
# acceder a sus atributos usando: IMiInterface.<atributo>
