Un pequeño equipo de desarrolladores decidió crear
un sistema operativo para un celular,
inicialmente sólo tendrá un fondo de pantalla
Todos podemos ver y cambiar el fondo de pantalla,
el SO se llamará `PyPhoneOS`
tendrá un fondo inicial de `gatitos.jpg`

# Análisis
Requisitos:
- Tiene un nombre
- Tiene un fondo de pantalla
- Cualquiera puede cambiar el fondo de pantalla
Objetos:
- SistemaOperativo
Características:
- SistemaOperativo:
    - nombre: String
    - fondo_pantalla: String
Acciones:
- SistemaOperativo:
    - cambiar_fondo_pantalla(imagen)
  - ```mermaid
classDiagram
    class SistemaOperativo {
        +nombre: String
        +fondo_pantalla: String
        +cambiar_fondo_pantalla(imagen)
    }
```