from enum import Enum

class EstadoSocio(Enum):
    
    HABILITADO = 1
    INHABILITADO = 2
    
class EstadoLibro(Enum):
    
    DISPONIBLE = 1
    PRESTADO = 2