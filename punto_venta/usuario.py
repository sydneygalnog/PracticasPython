from abc import ABC, abstractmethod

#clase base
class UsuarioBase(ABC):
    def __init__(self,nombre: str, correo: str):
        self.nombre=nombre
        self.correo=correo
    
    @abstractmethod
    def mostrar_info(self) -> str:
        pass
