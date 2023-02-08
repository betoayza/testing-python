from classes.Persona import Persona


class Student(Persona):
    def __init__(self, nombre, apellido, dni, edad, legajo):
        super().__init__(nombre, apellido, dni)
        self.edad = edad
        self.legajo = legajo

    def get_edad(self):
        return self.edad

    def get_legajo(self):
        return self.legajo

    def __str__(self):
        return "ESTUDIANTE:\nNombre: {}\nApellido: {}\nDNI: {}\nEdad: {}\nLegajo: {}".format(self.nombre, self.apellido, self.dni, self.edad, self.legajo)
