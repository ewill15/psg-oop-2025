El sistema operativo tendrá una batería, 
sólo el sistema operativo cargará la batería,
mediante un método público podemos conocer
el porcentaje de batería y mediante otro
método público podremos cargar la batería,
de manera similar a un puerto de carga

	# Análisis
Requisitos:
- Tiene un nombre
- Tiene un fondo de pantalla
- Cualquiera puede cambiar el fondo de pantalla
- Tiene un reloj
- Existe un método ver hora 
- Tiene una batería
- Existe un método estado_batería
- Existe un método cargador para cargar la batería
Objetos:
- SistemaOperativo
Características:
- SistemaOperativo:
    - nombre: String
    - fondo_pantalla: String
    - reloj: String
    - bateria: int
Acciones:
- SistemaOperativo:
    - cambiar_fondo_pantalla(imagen)
    - ver_hora()
    - estado_bateria()
    - cargador(cantidad)

```mermaid 
classDiagram
    class SistemaOperativo {
        +nombre: String
        #reloj: String
        +fondo_pantalla: String
        -bateria: int
        +cambiar_fondo_pantalla(imagen)
        +ver_hora()
        +estado_bateria()
        +cargador(cantidad)
    }
```
<br>
<br>
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
- Tiene un reloj
- Existe un método ver hora 
  
Objetos:
- SistemaOperativo
  
Características:
- SistemaOperativo:
    - nombre: String
    - fondo_pantalla: String
    - reloj: String

Acciones:
- SistemaOperativo:
    - cambiar_fondo_pantalla(imagen)
    - ver_hora()
```mermaid
classDiagram
    class SistemaOperativo {
        +nombre: String
        #reloj: String
        +fondo_pantalla: String
        +cambiar_fondo_pantalla(imagen)
        +ver_hora()
    }
```