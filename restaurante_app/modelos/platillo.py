from modelos.producto import Producto


class Platillo(Producto):

    def __init__(self, nombre, precio, disponible, tiempo_preparacion):
       
        super().__init__(nombre, precio, disponible)
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self):
      
        estado = "Disponible" if self.disponible else "No disponible"
        print("\n=== PLATILLO ===")
        print(f"Nombre       : {self.nombre}")
        print(f"Precio       : ${self.obtener_precio():.2f}")
        print(f"Estado       : {estado}")
        print(f"Preparación  : {self.tiempo_preparacion} min")