class Persona:
    def __init__ (self, nombre, apellido, dni):
        self.nombre = nombre;
        self.apellido = apellido;
        self.dni = dni

    def saludar(self):
        print("Mucho gusto ", self.nombre, " " ,self.apellido);
  
    def get_dni(self):
            return self.dni

            