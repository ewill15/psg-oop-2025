# Definiendo la clase
class Persona:
    def __init__(self, nombre): # Constructor
        self.nombre = nombre
 
    def saludar(self): # Método de instancia
        print(f"Hola, soy {self.nombre}")
        
    def dormir(self, horas): # Nuevo Método de instancia
        print(f"{self.nombre} duerme por {horas} hrs.")
        print(f"{self.nombre} se ha despertado")
 
# Instanciando un objeto
jhon = Persona("Jhon")
jhon.saludar()
# Llamando al método de la instancia
jhon.dormir(8)