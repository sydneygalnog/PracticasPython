#importar la clase Usuario (plantilla base)
from usuario import UsuarioBase

class Cliente(UsuarioBase):
    def __init__(self, nombre:str, correo: str,saldo: float):
        super().__init__(nombre, correo)
        self.saldo=saldo 
    
    def mostrar_info(self) -> str:
        return f"Cliente: {self.nombre}\nCorreo: {self.correo}\nSaldo: ${self.saldo:.2f}"