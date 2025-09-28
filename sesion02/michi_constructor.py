class Gato:
    def __init__(self, color, genero, edad, castrado):
        self.color = color
        self.genero = genero
        self.edad = edad
        self.castrado = castrado


# Instanciar
pelusa = Gato("Negro", "hembra", 2, False)
miauricio = Gato("Naranja", "macho", 1, True)


# Mostrar atributos
print("Pelusa: ",pelusa)
print(pelusa.color)
print(pelusa.genero)
print(pelusa.edad)
print(pelusa.castrado)
print("Miauricio: ",miauricio)
print(miauricio.color)
print(miauricio.genero)
print(miauricio.edad)
print(miauricio.castrado)


# Del ejemplo 06 modificaremos la clase Gato agregando el 
# atributo de clase "especie" por que todos los 
# gatos son felinos.
# Después instanciaremos dos gatos.

# Requisitos:
# - Recolectar gatos
# - Registrar los atributos de cada gato
# - Todos los gatos son felinos

# Objetos:
# - Gato

# Características:
# - Gato
#     - Especie
#     - Color
#     - Género
#     - Edad
#     - Castrado

# Acciones:
# - (No hay acciones)

# Clase con atributo de clase y atributos de instancia
class Gato:
    especie = "felino"
    def __init__(self, color, genero, edad, castrado):
        self.color = color
        self.genero = genero
        self.edad = edad
        self.castrado = castrado
 
michi = Gato("Negro", "hembra", 2, False)
miauricio = Gato("Naranja", "macho", 1, True)
print("Michi: ", michi.especie)
print(michi.color)
print(michi.genero)
print(michi.edad)
print(michi.castrado)
print("Miauricio: ", miauricio.especie)
print(miauricio.color)
print(miauricio.genero)
print(miauricio.edad)
print(miauricio.castrado)
print("Gato es: ", Gato.especie)