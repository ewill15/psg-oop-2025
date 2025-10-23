class Vino:
    def __init__(self,nombre,tipo,cepa,anio_produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio_produccion = anio_produccion

class Queso:
    def __init__(self,nombre,variedad,edad,lleva_sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.lleva_sal = lleva_sal

# 4 vinos y 3 quesos

vino_1 = Vino('Tannat Origen', 'Aranjuez', 'Tannat', 2022)
vino_2 = Vino('Altos del Aranjuez', 'Aranjuez', 'Cabernet Sauvignon', 2021)
vino_3 = Vino('Único Tannat', 'Campos de Solana', 'Tannat', 2021)
vino_4 = Vino('Tierra Alta Moscatel', 'Yokich', 'Moscatel de Alejandría', 2023)
print("******* VINOS **********")
print("Vino 1: ",vino_1.nombre," Tipo:",vino_1.tipo," Cepa:",vino_1.cepa," Produccion:",vino_1.anio_produccion)
print("Vino 2: ",vino_2.nombre," Tipo:",vino_2.tipo," Cepa:",vino_2.cepa," Produccion:",vino_2.anio_produccion)
print("Vino 3: ",vino_3.nombre," Tipo:",vino_3.tipo," Cepa:",vino_3.cepa," Produccion:",vino_3.anio_produccion)
print("Vino 4: ",vino_4.nombre," Tipo:",vino_4.tipo," Cepa:",vino_4.cepa," Produccion:",vino_4.anio_produccion)
print("******* QUESOS **********")
queso_1 = Queso('Queso Azul','Azul',6,True)
queso_2 = Queso('Gouda Artesanal','Semiduro',8,True)
queso_3 = Queso('Brie de la Casa','Brie',2,False)
print("Queso 1: ",queso_1.nombre," Variedad:",queso_1.variedad," Edad:",queso_1.edad," Lleva sal:",queso_1.lleva_sal)
print("Queso 2: ",queso_2.nombre," Variedad:",queso_2.variedad," Edad:",queso_2.edad," Lleva sal:",queso_2.lleva_sal)
print("Queso 3: ",queso_3.nombre," Variedad:",queso_3.variedad," Edad:",queso_3.edad," Lleva sal:",queso_3.lleva_sal)

