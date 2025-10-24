# Entrenar: aumenta su fuerza, pero consume energía.
# Descansar: recupera energía.
# Comer: solo puede consumir hamburguesas, lo que también le ayuda a recuperar energía.

class Atleta:
    fuerza = 100
    def __init__(self,nombre):
        self.nombre = nombre
        self.energia = 0

    def entrenar(self,energia,fuerza):
        print(f"Incrementando fuerza en {fuerza}, Disminuyendo energia {energia}")
        self.fuerza += fuerza
        self.energia -= energia

    @staticmethod
    def descansar(self):
        return self.energia
    
    def comer(self,comida): #metodo de instancia
        print(f"comsumiendo {comida}")
        print("despues de comer descansa incrementado su energia")
        self.descansar()

personaje_1 = Atleta('Mario')
personaje_1.entrenar(50,10)
# personaje_1.descansar(5)
personaje_1.comer("Hamburquesa")
