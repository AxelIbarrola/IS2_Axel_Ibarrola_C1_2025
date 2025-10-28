import datetime

from dominio.repositorios import (
    IRepositorioSocios,
    IRepositorioLibros,
    IRepositorioPrestamos
)

from dominio.prestamo import Prestamo

class ServicioPrestamo:
    
    def __init__(self, repo_socios, repo_libros, repo_prestamos):
        self.repo_socios = repo_socios
        self.repo_libros = repo_libros
        self.repo_prestamos = repo_prestamos
        
    
    def realizar_prestamo(self, id_socio, id_libro):
        
        socio = self.repo_socios.obtener_por_id(id_socio)
        if not socio: return '\nSocio no encontrado'

        libro = self.repo_libros.obtener_por_id(id_libro)
        if not libro: return '\nLibro no encontrado'
        
        prestamos_activos = self.repo_prestamos.obtener_activos_por_socio(id_socio)
        
        if not libro.esta_disponible():
            return f'\nEl libro {libro.titulo} no está disponible.'
        
        if not socio.puede_pedir_prestamo(len(prestamos_activos)):
            return f'\nEl socio {socio.nombre} no puede pedir más libros.'
        
        nuevo_prestamo = Prestamo(id_prestamo=None, socio = socio, libro = libro)
        libro.marcar_como_prestado()
        
        self.repo_prestamos.guardar(nuevo_prestamo)
        self.repo_libros.guardar(libro)
        
        print('\nPréstamo realizado con éxito.')
        return f'\nPréstamo del libro "{libro.titulo}" registrado a {socio.nombre}'
    
    def registrar_devolucion(self, id_prestamo, fecha_hoy):
        prestamo = self.repo_prestamos.obtener_por_id(id_prestamo)
        
        if not prestamo:
            return '\nPréstamo no encontrado.'
        if not prestamo.esta_activo:
            return '\nEste préstamo ya fue devuelto.'
        
        multa = prestamo.calcular_multa(fecha_hoy)
        
        prestamo.marcar_como_devuelto()
        prestamo.libro.marcar_como_disponible()
        
        mensaje = f'\nDevolución registrada para "{prestamo.libro.titulo}".'
        
        if multa > 0:
            
            prestamo.socio.inhabilitar()
            self.repo_socios.guardar(prestamo.socio)
            mensaje += f'Multa de ${multa}. El socio {prestamo.socio.nombre} ha sido inhabilitado.'
        
        else:
            
            mensaje += 'Sin multa. Socio sigue habilitado.'
        
        self.repo_prestamos.guardar(prestamo)
        self.repo_libros.guardar(prestamo.libro)
        
        print('\nDevolución registrada con éxito.')
        
        return mensaje