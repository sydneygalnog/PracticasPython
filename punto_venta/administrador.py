#importar la clase Usuario (plantilla base)
from usuario import UsuarioBase

class Administrador(UsuarioBase):
    def __init__(self, nombre:str, correo: str,permisos: list[str]):
        super().__init__(nombre, correo)
        self.permisos=permisos
    
    def mostrar_info(self) -> str:
        return f"Administrador: {self.usuario}, correo: {self.correo}, permisos:{','.join(self.permisos)}"