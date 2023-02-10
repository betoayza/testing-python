from random import randint
import array
import time
from classes.Persona import Persona
from classes.Student import Student
from classes.Auto import Auto
from classes.Avion import Avion
from classes.Perro import Perro
from classes.Leon import Leon

# Trabajando con variables
print("Probando 1,2,3...")
nombre = "Albert"
print("Mi nombre es: " + nombre)
letras = len(nombre)
print("Mi nombre tiene " + str(letras) + " letras")
nombre2 = "Pepe"
mix_nombres = nombre + " & " + nombre2
print("La combinación de nombres es: " + mix_nombres)

# Trabajando con arrays
mi_array = array.array("i", [1, 2, 3])
print("Mi array es: ", mi_array)

nro = randint(1, 10)

# Trabajando con booleans
esta_habilitado_10 = False

if nro == 10:
    esta_habilitado_10 = True

if esta_habilitado_10:
    print("La tiene el 10, será gol!")
else:
    print("Aun el 10 no la tiene, no será gol.")

# Trabajando con listas
mi_lista_1 = [1, "asd", 3, False]
print("Mi lista es: ", mi_lista_1)

# Trabajando con bucles
print("Recorriendo ", )
for elem in mi_lista_1:
    print(elem)

# Obtener el nombre de una variable local
mi_lista_1_name = list(locals().keys())[list(
    locals().values()).index(mi_lista_1)]

# Trabajando con ids
print("El identificador de ", mi_lista_1_name, "es: ", id(mi_lista_1))

# Trabajando con bloque try/except
try:
    experimento = "Albert" + 1
    print("Experimento exitoso: ", experimento, " !")
except TypeError:
    print("No se puede concantenar una cadena con otro tipo de datos!")
except:
    print("Un error genérico ha ocurrido!")

# Trabajando con entrada/salida --> archivos
with open("/home/alber/Documentos/Algunos apuntes") as file:
    for line in file:
        print(line)

# Trabajando con cadenas
cadena = "    Esta es una cadena     "
# es lo mismo que trim() de JS
print("Cadena con espacios a los extremos: " + cadena)
cadena_sin_espacios = cadena.strip()
print("Esta es una cadena sin espacios: " + "\"" + cadena_sin_espacios + "\"")

# replace() reemplaza un substring por otro
cadena_con_reemplazos = cadena.replace("es", "no es")
cadena_con_reemplazos = cadena.replace("cadena", "string")
print("Cadena con reemplazos: " + cadena_con_reemplazos)

# split() crea un array de strings a partir de una cadena
array_de_strings = cadena.split()
print("Esto es un array de cadenas: ", array_de_strings)

array_strings = ['Peras', 'Manzanas', 'Bananas']
print("Un array de strings: ", array_strings)
combinacion_strings = '-'.join(array_strings)  # similar a JS
print("La combinación de estas cadenas: ", combinacion_strings)

cadena_mayusculas = "palabra".capitalize()  # capitaliza la primer letra
print(cadena_mayusculas)

posicion = cadena_mayusculas.index("bra")
print("La posición es: ", posicion)

# Trabajando con secuencias
print("Aquí trabajando con unas secuencias: ")

for nro in range(5):
    print(nro)

print("\n")

for nro in range(3, 7):
    print(nro)

print("\n")
# Trabajando con delays
print("Imprimiendo cada elemento de una secuencia cada 3 seg... : ")
for nro in range(1, 11):
    print(nro)
    # time.sleep(3);

# Trabajando con tuplas
mi_tupla = (1, False, [1, 2, 3], "Hola")
print("Recorriendo mi tupla: ")
for elem in mi_tupla:
    print(elem)

# Trabajando con diccionarios
meses = dict(Enero=1, Febrero=2, Marzo=3)
print("Recorriendo un diccionario... :")
for mes in meses:
    print(mes)
print("El valor de Febrero es: ", meses["Febrero"])

# Trabajando con conjuntos (sets) --------------------------------
mi_conjunto = {1, 2, 3, 4, 5, 6, 7}
mi_conjunto_2 = {1, 2, 3, 7, 8, 9, 0}
conjunto_union = mi_conjunto.union(mi_conjunto_2)
conjunto_interseccion = mi_conjunto.intersection(mi_conjunto_2)
mi_conjunto_3 = set([1, 'a', "Hola", True])

print("La union de mis conjuntos es: ", conjunto_union)
print("...y la interseccion: ", conjunto_interseccion)
print("Mi conjunto que tiene varios tipos de datos: ", mi_conjunto_3)

# Trabajando con clases -----------------------------

# Herencia:
# los objetos sobreescriben los métodos del padre
persona = Persona('Alberto', 'Ayza', 123123123)
persona.saludar()
print("El dni es: ", persona.get_dni())

estudiante = Student("Alberto", "Ayza", 123123123, 31, 123)
datos_estudiante = str(estudiante)
print(datos_estudiante)

# polimorfismo:
# los objetos implementan los métodos de la interfaz o de la clase abstracta

# Interfaz mediante herencia de clase abstracta:
auto = Auto()
auto.arrancar()
auto.acelerar()
auto.frenar()

avion = Avion()
avion.arrancar()
avion.acelerar()
avion.frenar()

# Interfaz mediante zope:
perro = Perro()
perro.correr()
perro.comer()
perro.realizar_sonido()

leon = Leon()
leon.correr()
leon.comer()
leon.realizar_sonido()
