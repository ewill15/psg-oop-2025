	# Definiendo la clase
class SistemaOperativo:
    def __init__(self, nombre, fondo_pantalla):
        self.nombre = nombre
        self.fondo_pantalla = fondo_pantalla
    def cambiar_fondo_pantalla(self, imagen):
        self.fondo_pantalla = imagen
        print(f"Nuevo fondo: {self.fondo_pantalla}")
        return self.fondo_pantalla
# Implementando la clase
so = SistemaOperativo("PyPhoneOS", "gatitos.jpg")
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.cambiar_fondo_pantalla("perritos.jpg")
so.fondo_pantalla = "paisajes.jpg"  # Cambiando directamente
print(f"Fondo de pantalla: {so.fondo_pantalla}")