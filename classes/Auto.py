from classes.Vehiculo import Vehiculo

class Auto (Vehiculo):
    def arrancar(self):
        print("Run, run, run... ")

    def frenar(self):
        print("ñiiii... frenó.")
    
    def acelerar(self):
        print("El coche aceleró en 25 kms/h")

# La subclases concretas deben implementar todos los methodos abstractos y en orden para ser validas


    