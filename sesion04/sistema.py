# Definiendo la clase
class SistemaOperativo:
    def __init__(self, nombre, fondo_pantalla, reloj):
        self.nombre = nombre 
        self.fondo_pantalla = fondo_pantalla 
        self.reloj = reloj 
    def cambiar_fondo_pantalla(self, nuevo_fondo):
        self.fondo_pantalla = nuevo_fondo
        print(f"Nuevo fondo: {self.fondo_pantalla}")
        return self.fondo_pantalla
    def ver_hora(self):
        print(f"La hora actual es: {self.reloj}")
        return self.reloj
# Implementando la clase
so = SistemaOperativo("PyPhoneOS", "gatitos.jpg", "12:00 PM")
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.cambiar_fondo_pantalla("perritos.jpg")
so.fondo_pantalla = "paisajes.jpg"
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.ver_hora()