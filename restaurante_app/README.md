# Sistema de Gestión de Restaurante

El sistema simula un pequeño restaurante donde es posible registrar platillos y bebidas mediante un menú por consola. Su propósito principal es demostrar cómo aplicar correctamente los principios fundamentales de la Programación Orientada a Objetos dentro de un proyecto organizado y con buenas prácticas de programación.

Estructura del proyecto
restaurante_app/
│
├── main.py
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
└── servicios/
    ├── __init__.py
    └── restaurante.py

El proyecto se encuentra organizado en capas para facilitar la lectura, mantenimiento y escalabilidad del código.

Modelos
La carpeta modelos contiene las clases que representan las entidades principales del sistema.
* Producto: clase padre.
* Platillo: hereda de la clase Producto.
* Bebida: hereda de la clase Producto.
Cada clase define sus propios atributos y métodos, representando objetos del mundo real.

Servicios
La carpeta servicios contiene la lógica principal del sistema.
La clase Restaurante administra la información de los productos registrados durante la ejecución del programa.
Entre sus responsabilidades se encuentran:
* Registrar platillos.
* Registrar bebidas.
* Mostrar la información almacenada.

 Punto de entrada
El archivo main.py representa el punto de inicio del programa.
Desde este archivo se:
* Muestra el menú principal.
* Solicita información al usuario.
* Crea los objetos correspondientes.
* Llama a los métodos definidos en la clase Restaurante.

La ejecución del sistema inicia mediante:
```python
if __name__ == "__main__":
    main()