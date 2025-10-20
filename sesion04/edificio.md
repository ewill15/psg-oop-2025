# Análisis
Requisitos:
- Un edificio necesita un sistema de control de acceso
- Existe un pin de desbloqueo privado
- Se puede ver el pin de desbloqueo mediante método público
- Se puede cambiar el pin de desbloqueo mediante método público
- El pin de desbloqueo debe ser máximo 4 dígitos
- El pin inicial será 1234
- El edificio tendrá un número telefónico
- Cualquiera puede ver el número telefónico 
- Cualquiera puede cambiar el número telefónico
Objetos:
- Edificio
Características:
- Edificio:
    - pin: String
    - telefono: String
Acciones:
- Edificio:
    - get_pin()
    - set_pin(nuevo_pin)
    - get_telefono()
    - set_telefono(nuevo_telefono)
```mermaid
classDiagram
    class Edificio {
        -pin: String
        -telefono: String
        +get_pin()
        +set_pin(nuevo_pin)
        +get_telefono()
        +set_telefono(nuevo_telefono)
    }
```
<br>
<br>
Un edificio necesita un sistema de control de acceso,
existe un pin de desbloqueo privado,
cualquier persona puede ver el pin de desbloqueo 
cualquier persona puede cambiar el pin
el pin de desbloqueo debe ser máximo 4 dígitos
el pin inicial será 1234

# Análisis
Requisitos:
- Un edificio necesita un sistema de control de acceso
- Existe un pin de desbloqueo privado
- Se puede ver el pin de desbloqueo mediante método público
- Se puede cambiar el pin de desbloqueo mediante método público
- El pin de desbloqueo debe ser máximo 4 dígitos
- El pin inicial será 1234
Objetos:
- Edificio
Características:
- Edificio:
    - pin: String
Acciones:
- Edificio:
    - get_pin()
    - set_pin(nuevo_pin)
  - ```mermaid
classDiagram
    class Edificio {
        -pin: String
        +get_pin()
        +set_pin(nuevo_pin)
    }
```