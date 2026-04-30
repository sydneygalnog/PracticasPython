from producto import Producto
from cliente import Cliente
from datetime import datetime #importar la libreria de datetime para tomar el valor de la fecha

class Venta:
    def __init__(self,cliente: Cliente):
        self.cliente=cliente
        self.productos: list[Producto]=[]
        self.fecha=datetime.today()
    
    #función par agregar un producto nuevo a la lista
    def agregar_producto(self,producto: Producto)-> None:
        self.productos.append(producto)

    def total(self)-> float:
        return sum(p.precio for p in self.productos)
    
    #función para mostrar la info de la venta
    def mostrar_info_venta(self):
        print("~"*35)
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Fecha de la compra: {self.fecha.strftime("%Y-%m-%d")}")
        print("~"*35)
        print("Detalle de la compra:")
        print(f"{'Producto':<20}{'Precio':>20}")
        for producto in self.productos:
            print(f"{producto.nombre:<20}      {producto.precio:>15.2f}")
        print(f"{'Total de la venta:':<20} {self.total():>20.2f}")

