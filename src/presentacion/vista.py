import datetime

from servicio.servicio_prestamo import ServicioPrestamo
from servicio.servicio_socios import ServicioGestionSocios
from servicio.servicio_libro import ServicioCatalogoLibros


class VistaOperaciones:
    
    def __init__(self, servicio_prestamo, servicio_socios, servicio_catalogo):
        
        self.servicio_prestamo = servicio_prestamo
        self.servicio_socios = servicio_socios
        self.servicio_catalogo = servicio_catalogo

    def _mostrar_resultado(self, operacion, resultado):
        
        print(f'\nResultado de {operacion}: ')
        print(f"\n'{resultado}'")


    def simular_click_prestar(self, id_socio, id_libro):
        print(f'\nUsuario intenta prestar (Socio: {id_socio}, Libro: {id_libro})')
        resultado = self.servicio_prestamo.realizar_prestamo(id_socio, id_libro)
        self._mostrar_resultado("Realizar Préstamo", resultado)

    def simular_click_devolver(self, id_prestamo: int):

        print(f'\nUsuario intenta devolver (Préstamo ID: {id_prestamo})')
      
        fecha_devolucion_simulada = datetime.date(2025, 11, 15) 
        
        resultado = self.servicio_prestamo.registrar_devolucion(id_prestamo, fecha_devolucion_simulada)
        self._mostrar_resultado("Registrar Devolución", resultado)


    def simular_click_alta_socio(self, nombre, dni):
        print(f'\nUsuario intenta crear socio (DNI: {dni})')
        resultado = self.servicio_socios.alta_socio(nombre, dni)
        self._mostrar_resultado("Alta de Socio", resultado)
    
    
    def simular_busqueda_libro(self, titulo):
        
        print(f'Usuario busca libros por título: "{titulo}"')
        libros_encontrados = self.servicio_catalogo.buscar_por_titulo(titulo)
        
        print(f"\n--- Búsqueda de Libros ---")
        if not libros_encontrados:
            print("\nNo se encontraron libros con ese título.")
        else:
            print(f"\nSe encontraron {len(libros_encontrados)} libros:")
            for libro in libros_encontrados:
                print(f"\n  - ID: {libro.id_libro}, Título: {libro.titulo}, Autor: {libro.autor}")
        print("-------------------------------------------")