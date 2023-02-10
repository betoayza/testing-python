from classes.Vehiculo import Vehiculo

class Avion(Vehiculo):
    def arrancar(self):
        print("Empezó a moverse por la pista...")
    
    def frenar(self):
        print("El avión llegó a su destino o hubo un accidente.")

    def acelerar(self):
        print("Se aceleró en 300 kms/h")
   