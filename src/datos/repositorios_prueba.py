from dominio.socio import Socio
from dominio.libro import Libro
from dominio.prestamo import Prestamo
from dominio.enums import EstadoLibro

from dominio.repositorios import (
    IRepositorioSocios,
    IRepositorioLibros,
    IRepositorioPrestamos
)

class SociosRepository(IRepositorioSocios):
    
    def __init__(self):
        self._socios = [
            Socio(1, "Marta López", "123456"),
            Socio(2, "Juan Pérez", "789012")
        ]
        
        self._contador_id = 3
        
        print('\nDatos inicializados con 2 socios.')
        
    
    def obtener_por_id(self, id_socio):
        
        for socio in self._socios:
            if socio.id_socio == id_socio:
                return socio
        
        return None
    
    def obtener_por_dni(self, dni):
        
        for socio in self._socios:
            if socio.dni == dni:
                return socio
        
        return None
    
    def guardar(self, socio):
        if socio.id_socio:
            
            print(f'\nSocio {socio.nombre} actualizado')
        
        else:
            socio.id_socio = self._contador_id
            self._contador_id += 1
            self._socios.append(socio)
            print(f'\nSimulando guardado del socio {socio.nombre}')

class LibrosRepository(IRepositorioLibros):
    
    def __init__(self):
        self._libros = [
            Libro(101,"abc", "El Aleph", "Borges"),
            Libro(102, "def", "Cien años de soledad", "García Márquez")
        ]
        
        self._contador_id = 103
        
        self._libros[1].marcar_como_prestado()
        
        print('\nDatos inicializados con 2 libros (uno prestado).')
        
    
    def obtener_por_id(self, id_libro):
        
        for libro in self._libros:
            if libro.id_libro == id_libro:
                return libro
        
        return None
    
    def buscar_por_titulo(self, titulo):

        titulo = titulo.lower()
        
        return [ libro for libro in self._libros if titulo in libro.titulo.lower()]
    
    def guardar(self, libro):
        
        if libro.id_libro and libro in self._libros:
            
            print(f'\nActualizando libro "{libro.titulo}"')
        
        else:
            
            libro.id_libro = self._contador_id
            self._contador_id += 1 
            self._libros.append(libro)
            print(f'\nSimulando guardado del libro "{libro.titulo}"')

class PrestamosRepository(IRepositorioPrestamos):
    
    def __init__(self):
        self._prestamos = []
        self._contador_id = 1
        print('\nDatos inicializados con 0 préstamos.')
        
    
    def obtener_activos_por_socio(self, id_socio):
        activos = [p for p in self._prestamos if p.socio.id_socio == id_socio and p.esta_activo]
        return activos
    
    def obtener_por_id(self, id_prestamo):
        
        for prestamo in self._prestamos:
            if prestamo.id_prestamo == id_prestamo:
                return prestamo
        
        return None       
    
    def guardar(self, prestamo):
        
        if prestamo.id_prestamo and prestamo in self._prestamos:
            
            print('\nActualizando préstamo.')
        
        else:
            
            prestamo.id_prestamo = self._contador_id
            self._contador_id += 1
            self._prestamos.append(prestamo)
            print(f'\nGuardando nuevo préstamo con id {prestamo.id_prestamo}')