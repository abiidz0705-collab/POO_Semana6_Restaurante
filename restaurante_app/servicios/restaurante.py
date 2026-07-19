class Restaurante:

    def __init__(self):
        
        self.productos = []

    def registrar_platillo(self, platillo):
       
        self.productos.append(platillo)
        print("\nPlatillo registrado correctamente.")

    def registrar_bebida(self, bebida):
       
        self.productos.append(bebida)
        print("\nBebida registrada correctamente.")

    def mostrar_productos(self):
        
        print("\n========= PRODUCTOS =========")

        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\nDemostración del polimorfismo:\n")
        for producto in self.productos:
            producto.mostrar_informacion()