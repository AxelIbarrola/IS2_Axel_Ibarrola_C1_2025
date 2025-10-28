import abc
from .socio import Socio
from .libro import Libro
from .prestamo import Prestamo

class IRepositorioSocios(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def obtener_por_id(self, id_socio):
        pass
    
    @abc.abstractmethod
    def obtener_por_dni(self, dni):
        pass
    
    @abc.abstractmethod
    def guardar(self, socio):
        pass

class IRepositorioLibros(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def obtener_por_id(self, id_libro):
        pass
    
    @abc.abstractmethod
    def buscar_por_titulo(self, titulo):
        pass
    
    @abc.abstractmethod
    def guardar(self, libro):
        pass
    


class IRepositorioPrestamos(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def obtener_activos_por_socio(self, id_socio):
        pass
    
    @abc.abstractmethod
    def obtener_por_id(self, id_prestamo):
        pass
    
    
    @abc.abstractmethod
    def guardar(self, prestamo):
        pass
    