from cliente import Cliente
from producto import Producto
from tienda import Tienda
from venta import Venta


#crear cliente
cliente1=Cliente("Luis","luis@mail.com",1000)

#crear productos
p1=Producto("Teclado",250)
p2=Producto("Mouse",150)

#Crear venta y agregar productos
venta1=Venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)

#crear tienda y registrar venta
tienda=Tienda("TechStore")
tienda.registrar_venta(venta1)

#venta1.mostrar_info_venta()
print(cliente1.mostrar_info())
print(f"total de la venta: {venta1.total():.2f}")
print(f"Ventas registradas: {len(tienda.ventas)}")

venta1.mostrar_info_venta()

#Otros ejemplos
#crear cliente
cliente2=Cliente("Sydney","sydney@mail.com",5000)

#crear productos
p3=Producto("Monitor",1000)
p4=Producto("Regulador",450)

#Crear venta y agregar productos
venta2=Venta(cliente2)
venta2.agregar_producto(p2)
venta2.agregar_producto(p3)
venta2.agregar_producto(p4)

#crear tienda y registrar venta
tienda.registrar_venta(venta2)
venta2.mostrar_info_venta()