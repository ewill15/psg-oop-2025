# Análisis
Requisitos:
- Crear un gato
- Los gatos tienen un nombre y color
- Los gatos pueden maullar
- Los gatos nacen como cachorros
- Los gatos pueden hacer `miau` y `ronroneo`
- Los gatos pueden crecer con el tiempo
Objetos:
- Gato
Características:
- Gato: nombre, color, edad
Acciones:
- Gato: nacer, crecer, maullar, sonidos
<br>
<br>

```mermaid
classDiagram
    class Gato {
        String nombre
        String color
        int edad
        nacer(nombre, color)
        crecer(tiempo)
        maullar()
        sonidos()
    }
```
<br>
<br>

***
Análisis para Perro  
***
# Análisis
Requisitos:
- Crear un perro
- Los perros tienen un nombre
- Los perros pueden ladrar
- Los perros nacen como cachorros
- La edad de un perro es 7 veces menor que la de un humano
Objetos:
- Perro
Características:
- Perro: nombre, edad
Acciones:
- Perro: ladrar, nacer, crecer, edad_a_humano
```mermaid
classDiagram
    class Perro {
        String nombre
        int edad
        ladrar()
        nacer(nombre)
        crecer(tiempo)
        edad_a_humano(perro)
    }
```
  
<br><br>

***
Análisis para Personas
***
# Análisis

Requisitos:
- Crear personas
- Las personas tienen un nombre
- Las personas pueden saludar
- Las personas pueden dormir
- Las personas pueden comer
- Al despertar tienen hambrenombre
  
Objetos:
- Persona
  
Características:
- Persona: Nombre, cansancio, hambre
  
Acciones:
- Persona: Saludar, cansancio, comer
```mermaid
classDiagram
    class Persona {
        String nombre
        bool hambre
        saludar()
        dormir(horas)
        comer(comida)
    }
```