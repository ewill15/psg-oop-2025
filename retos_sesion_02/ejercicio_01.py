class Animal:
    origen = "feral"
    def __init__(self,especie,tipo,lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar

mamifero_1 = Animal('leona','mamifero','sabana africana')
mamifero_2 = Animal('llama','mamifero','altiplano boliviano')
print("Mamifero 1: ",mamifero_1.origen, " Especie:",mamifero_1.especie," Tipo:", mamifero_1.tipo," Lugar:", mamifero_1.lugar)
print("Mamifero 2: ",mamifero_2.origen, " Especie:",mamifero_2.especie," Tipo:", mamifero_2.tipo," Lugar:", mamifero_2.lugar)

reptil = Animal('cocodrilo','reptil','rio nilo')
print("Reptil: ",reptil.origen, " Especie:",reptil.especie," Tipo:", reptil.tipo, " Lugar:",reptil.lugar)

ave = Animal('Condor','ave','Altiplano')
print("Ave: ",ave.origen, " Especie:",ave.especie, " Tipo:",ave.tipo, " Lugar:",ave.lugar)