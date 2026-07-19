from modelos.producto import Producto


class Bebida(Producto):

    def __init__(self, nombre, precio, disponible, mililitros):
       
        super().__init__(nombre, precio, disponible)
        self.mililitros = mililitros

    def mostrar_informacion(self):
        
        estado = "Disponible" if self.disponible else "No disponible"
        print("\n=== BEBIDA ===")
        print(f"Nombre       : {self.nombre}")
        print(f"Precio       : ${self.obtener_precio():.2f}")
        print(f"Estado       : {estado}")
        print(f"Tamaño       : {self.mililitros} ml")