# Análisis

Requisitos:
- Crear personas
- Las personas tienen un nombre
- Las personas pueden saludar
- Las personas pueden dormir
- Tiene un constructor que crea personas con nombre
  
Objetos:
- Persona
  
Características:
- Persona: Nombre, cansancio
  
Acciones:
- Persona: Saludar, cansancio
```mermaid
classDiagram
    class Persona {
        String nombre
        saludar()
        dormir(horas)
    }
```