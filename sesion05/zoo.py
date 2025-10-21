	# Definición
class Animal:
    def __init__(self, especie):
        self.especie = especie
 
    def mostrar(self): # Nuevo método
        print(f"Especie: {self.especie}")
class Mamifero(Animal):
    def __init__(self, especie, tipo):
        super().__init__(especie) # Constructor Padre
        self.tipo = tipo
    def amamantar(self):
        print(f"{self.especie} amamanta 🍼 a crías")
 
    def mostrar(self):
        super().mostrar()
        print(f"Tipo: {self.tipo}")
        self.amamantar()
 
class Ave(Animal):
    def __init__(self, especie, volar):
        super().__init__(especie) 
        self.volar = volar
    def poner_huevo(self):
        print(f"{self.especie} pone huevos 🥚")
    
    def mostrar(self): # Método sobreescrito
        super().mostrar()  # Llamada al método del padre
        print(f"Puede volar: {self.volar}")
        self.poner_huevo()
 
class Reptil(Animal):
    def __init__(self, especie, tipo, venenoso):
        super().__init__(especie)
        self.tipo = tipo
        self.venenoso = venenoso
    def reptar(self):
        print(f"{self.especie} se arrastra 🐍")
 
    def mostrar(self): # Método sobreescrito
        super().mostrar()  # Llamada al método del padre
        print(f"Tipo: {self.tipo}, venenoso: {self.venenoso}")
        self.reptar()
# Uso
caballo = Mamifero("Caballo", "Terrestre")
caballo.mostrar()
paloma = Ave("Paloma", True)
paloma.mostrar()
coco = Reptil("Cocodrilo", "Acuático", False)
coco.mostrar()
# Uso isinstance()
caballo_es_mamifero = isinstance(caballo, Mamifero)
print("Caballo Es Mamifero: ", caballo_es_mamifero)
caballo_es_animal = isinstance(caballo, Animal)
print("Caballo Es Animal: ", caballo_es_animal)
caballo_es_ave = isinstance(caballo, Ave)
print("Caballo Es Ave: ", caballo_es_ave)
# Uso issubclass()
mamifero_es_animal = issubclass(Mamifero, Animal)
print("Mamifero Es Animal: ", mamifero_es_animal)
mamifero_es_ave = issubclass(Mamifero, Ave)
print("Mamifero Es Ave: ", mamifero_es_ave)

# # Definición
# class Animal:
#     def __init__(self, especie):
#         self.especie = especie
 
#     def mostrar(self): # Nuevo método
#         print(f"Especie: {self.especie}")
# class Mamifero(Animal):
#     def __init__(self, especie, tipo):
#         super().__init__(especie) # Constructor Padre
#         self.tipo = tipo
#     def amamantar(self):
#         print(f"{self.especie} amamanta 🍼 a crías")
 
#     def mostrar(self):
#         super().mostrar()
#         print(f"Tipo: {self.tipo}")
#         self.amamantar()
 
# class Ave(Animal):
#     def __init__(self, especie, volar):
#         super().__init__(especie) 
#         self.volar = volar
#     def poner_huevo(self):
#         print(f"{self.especie} pone huevos 🥚")
    
#     def mostrar(self): # Método sobreescrito
#         super().mostrar()  # Llamada al método del padre
#         print(f"Puede volar: {self.volar}")
#         self.poner_huevo()
 
# class Reptil(Animal):
#     def __init__(self, especie, tipo, venenoso):
#         super().__init__(especie)
#         self.tipo = tipo
#         self.venenoso = venenoso
#     def reptar(self):
#         print(f"{self.especie} se arrastra 🐍")
 
#     def mostrar(self): # Método sobreescrito
#         super().mostrar()  # Llamada al método del padre
#         print(f"Tipo: {self.tipo}, venenoso: {self.venenoso}")
#         self.reptar()
# # Uso
# caballo = Mamifero("Caballo", "Terrestre")
# caballo.mostrar()
# paloma = Ave("Paloma", True)
# paloma.mostrar()
# coco = Reptil("Cocodrilo", "Acuático", False)
# coco.mostrar()
# # Uso isinstance()
# caballo_es_mamifero = isinstance(caballo, Mamifero)
# print("Caballo Es Mamifero: ", caballo_es_mamifero)
# caballo_es_animal = isinstance(caballo, Animal)
# print("Caballo Es Animal: ", caballo_es_animal)
# caballo_es_ave = isinstance(caballo, Ave)
# print("Caballo Es Ave: ", caballo_es_ave)

# # # Definición
# # class Animal:
# #     def __init__(self, especie):
# #         self.especie = especie
 
# #     def mostrar(self): # Nuevo método
# #         print(f"Especie: {self.especie}")
# # class Mamifero(Animal):
# #     def __init__(self, especie, tipo):
# #         super().__init__(especie) # Constructor Padre
# #         self.tipo = tipo
# #     def amamantar(self):
# #         print(f"{self.especie} amamanta 🍼 a crías")
 
# #     def mostrar(self):
# #         super().mostrar()
# #         print(f"Tipo: {self.tipo}")
# #         self.amamantar()
 
# # class Ave(Animal):
# #     def __init__(self, especie, volar):
# #         super().__init__(especie) 
# #         self.volar = volar
# #     def poner_huevo(self):
# #         print(f"{self.especie} pone huevos 🥚")
    
# #     def mostrar(self): # Método sobreescrito
# #         super().mostrar()  # Llamada al método del padre
# #         print(f"Puede volar: {self.volar}")
# #         self.poner_huevo()
 
# # class Reptil(Animal):
# #     def __init__(self, especie, tipo, venenoso):
# #         super().__init__(especie)
# #         self.tipo = tipo
# #         self.venenoso = venenoso
# #     def reptar(self):
# #         print(f"{self.especie} se arrastra 🐍")
 
# #     def mostrar(self): # Método sobreescrito
# #         super().mostrar()  # Llamada al método del padre
# #         print(f"Tipo: {self.tipo}, venenoso: {self.venenoso}")
# #         self.reptar()
# # # Uso
# # caballo = Mamifero("Caballo", "Terrestre")
# # caballo.mostrar()
# # paloma = Ave("Paloma", True)
# # paloma.mostrar()
# # coco = Reptil("Cocodrilo", "Acuático", False)
# # coco.mostrar()



# # # # Definición
# # # class Animal:
# # #     def __init__(self, especie):
# # #         self.especie = especie
 
# # #     def mostrar(self): # Nuevo método
# # #         print(f"Especie: {self.especie}")
# # # class Mamifero(Animal):
# # #     def __init__(self, especie, tipo):
# # #         super().__init__(especie) # Constructor Padre
# # #         self.tipo = tipo
# # #     def amamantar(self):
# # #         print(f"{self.especie} amamanta 🍼 a crías")
 
# # #     def mostrar(self): # Método sobreescrito
# # #         super().mostrar()
# # #         print(f"Tipo: {self.tipo}")
# # #         self.amamantar()
 
# # # class Ave(Animal):
# # #     def __init__(self, especie, volar):
# # #         super().__init__(especie) 
# # #         self.volar = volar
# # #     def poner_huevo(self):
# # #         print(f"{self.especie} pone huevos 🥚")
 
# # # class Reptil(Animal):
# # #     def __init__(self, especie, tipo, venenoso):
# # #         super().__init__(especie)
# # #         self.tipo = tipo
# # #         self.venenoso = venenoso
# # #     def reptar(self):
# # #         print(f"{self.especie} se arrastra 🐍")
# # # # Uso
# # # caballo = Mamifero("Caballo", "Terrestre")
# # # caballo.mostrar()
# # # paloma = Ave("Paloma", True)
# # # paloma.mostrar()
# # # print(f"Puede volar:{paloma.volar}")
# # # paloma.poner_huevo()
# # # coco = Reptil("Cocodrilo", "Acuático", False)
# # # coco.mostrar()
# # # print(f"tipo:{coco.tipo}, venenoso:{coco.venenoso}")
# # # coco.reptar()

# # # # # Definición
# # # # class Animal:
# # # #     def __init__(self, especie):
# # # #         self.especie = especie
# # # # class Mamifero(Animal):
# # # #     def __init__(self, especie, tipo):
# # # #         super().__init__(especie) # Constructor Padre
# # # #         self.tipo = tipo
# # # #     def amamantar(self):
# # # #         print(f"{self.especie} amamanta 🍼 a crías")
 
# # # # class Ave(Animal):
# # # #     def __init__(self, especie, volar):
# # # #         super().__init__(especie) # Constructor Padre
# # # #         self.volar = volar
# # # #     def poner_huevo(self):
# # # #         print(f"{self.especie} pone huevos 🥚")
 
# # # # class Reptil(Animal):
# # # #     def __init__(self, especie, tipo, venenoso):
# # # #         super().__init__(especie) # Constructor Padre
# # # #         self.tipo = tipo
# # # #         self.venenoso = venenoso
# # # #     def reptar(self):
# # # #         print(f"{self.especie} se arrastra 🐍")
# # # # # Uso
# # # # caballo = Mamifero("Caballo", "Terrestre")
# # # # print(f"Especie: {caballo.especie}, Tipo: {caballo.tipo}")
# # # # caballo.amamantar()
# # # # paloma = Ave("Paloma", True)
# # # # print(f"Especie:{paloma.especie}, puede volar:{paloma.volar}")
# # # # paloma.poner_huevo()
# # # # coco = Reptil("Cocodrilo", "Acuático", False)
# # # # print(f"Especie: {coco.especie} - Tipo: {coco.tipo} - Venenoso: {coco.venenoso}")
# # # # coco.reptar()

# # # # # # Definición
# # # # # class Animal:
# # # # #     def __init__(self, especie):
# # # # #         self.especie = especie
 
# # # # # class Mamifero(Animal):
# # # # #     def __init__(self, especie, tipo): # Constructor hija
# # # # #         super().__init__(especie) # Constructor Padre
# # # # #         self.tipo = tipo
 
# # # # #     def amamantar(self):
# # # # #         print(f"{self.especie} amamanta 🍼 a crías")
# # # # # # class Ave(Animal):
# # # # # #     def poner_huevo(self):
# # # # # #         print(f"{self.especie} pone huevos 🥚")
# # # # # # class Reptil(Animal):
# # # # # #     def reptar(self):
# # # # # #         print(f"{self.especie} se arrastra 🐍")
# # # # # # Uso
# # # # # caballo = Mamifero("Caballo", "Terrestre")
# # # # # print(f"Especie: {caballo.especie}, Tipo: {caballo.tipo}")
# # # # # caballo.amamantar()

# # # # # # paloma = Ave("Paloma")
# # # # # # paloma.volar = True # Asignar atributo
# # # # # # print(f"Especie:{paloma.especie}, puede volar:{paloma.volar}")
# # # # # # paloma.poner_huevo()
# # # # # # coco = Reptil("Cocodrilo")
# # # # # # coco.tipo = "Acuático" # Asignar atributo
# # # # # # coco.venenoso = False # Asignar atributo
# # # # # # print(f"Especie:{coco.especie}, tipo:{coco.tipo}, Venenoso:{coco.venenoso}")
# # # # # # coco.reptar()