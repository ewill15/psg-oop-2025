class Persona:
    # Constructor
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad
    # Representacion en cadena de la clase
    def __str__(self): # Método especial
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    # Representacion oficial
    def __repr__(self): # Método especial
        return f"Persona({self.nombre}, {self.edad})"
    # Destructor
    def __del__(self): # Método especial
        print(f"{self.nombre} ha sido eliminado")
    
# Constructor
jhon = Persona("Jhon", 30)
print(jhon.nombre) # Jhon
print(jhon.edad) # 30

# Representacion en cadena de la clase
jhon = Persona("Jhon", 30)
print(jhon) # Nombre: Jhon, Edad: 30
jane = Persona("Jane", 25)
detalle = str(jane)
print(detalle) # Nombre: Jane, Edad: 25

# Representacion oficial
jhon = Persona("Jhon", 30)
print(repr(jhon)) # Persona(Jhon, 30)
jane = Persona("Jane", 25)
print(repr(jane)) # Persona(Jane, 25)

# desctructor
jhon = Persona("Jhon", 30)
print(jhon.nombre) # Jhon
del jhon # Jhon ha sido eliminado
jane = Persona("Jane", 25)
print(jane.nombre) # Jane
del jane # Jane ha sido eliminado

#dictionary
jhon = Persona("Jhon", 30)
print(jhon.__dict__) # {'nombre': 'Jhon', 'edad': 30}
jane = Persona("Jane", 25)
print(jane.__dict__) # {'nombre': 'Jane', 'edad': 25}