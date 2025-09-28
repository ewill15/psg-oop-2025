# Analisis
# Requisitos:
# - Registrar perros
# - Registrar los atributos de cada perro
# Objetos:
# - Perro
# Características:
# - Perro
#     - Nombre
#     - Edad
#     - Género
#     - Raza
#     - Vacunado
#     - Propietario
# Acciones:
# - (No hay acciones)

class Perro:
    def __init__(self, nombre, edad, genero, raza, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.propietario = propietario

# Instanciar
toby = Perro("Toby", 3, "macho", "labrador", "Juan")
luna = Perro("Luna", 2, "hembra", "pug", "Jane")

# Mostrar atributos
print("Toby: ",toby)
print(toby.nombre)
print(toby.edad)
print(toby.genero)
print(toby.raza)
print(toby.propietario)
print("Luna: ",luna)
print(luna.nombre)
print(luna.edad)
print(luna.genero)
print(luna.raza)
print(luna.propietario)


# Del ejemplo 07 modificar la clase Perro con
# tres atributos de clase. Toma en cuenta que 
# todos los perros son caninos, mamíferos y terrestres
# Después instancia dos perros.

# Requisitos:
# - Registrar perros
# - Registrar los atributos de cada perro
# Objetos:
# - Perro
# Características:
# - Perro
#     - Especie
#     - Tipo
#     - Habitat
#     - Nombre
#     - Edad
#     - Género
#     - Raza
#     - Vacunado
#     - Propietario
# Acciones:
# - (No hay acciones)

class Perro:
    especie = "canino"
    tipo = "mamífero"
    habitat = "terrestre"
    def __init__(self, nombre, edad, genero, raza, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.propietario = propietario
toby = Perro("Toby", 3, "macho", "labrador", "Juan")
luna = Perro("Luna", 2, "hembra", "pug", "Jane")

print("Toby: ",toby.tipo, toby.especie, toby.habitat)
print(toby.nombre)
print(toby.edad)
print(toby.genero)
print(toby.raza)
print(toby.propietario)

print("Luna: ",luna.tipo, luna.especie, luna.habitat)
print(luna.nombre)
print(luna.edad)
print(luna.genero)
print(luna.raza)
print(luna.propietario)

print("Perro es: ", Perro.tipo, "Especie: ", Perro.especie, "Habitat: ", Perro.habitat)
