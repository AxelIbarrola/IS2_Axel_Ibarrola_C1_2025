import datetime

from datos.repositorios_prueba import (SociosRepository, LibrosRepository, PrestamosRepository)

from servicio.servicio_prestamo import ServicioPrestamo
from servicio.servicio_socios import ServicioGestionSocios
from servicio.servicio_libro import ServicioCatalogoLibros

from presentacion.vista import VistaOperaciones


if __name__ == "__main__":
    print("\n=============================================")
    print("--- SISTEMA DE BIBLIOTECA ---")
    print("=============================================")
    
    try:
        repo_socios = SociosRepository()
        repo_libros = LibrosRepository()
        repo_prestamos = PrestamosRepository()
    except Exception as e:
        print(f"Error al iniciar repositorios: {e}")
        exit()
        
    print("\nRepositorios Creados")
    
    servicio_prestamo = ServicioPrestamo(repo_socios, repo_libros, repo_prestamos)
    servicio_socios = ServicioGestionSocios(repo_socios)
    servicio_catalogo = ServicioCatalogoLibros(repo_libros)
    
    print("\nServicios Creados")
    
    vista = VistaOperaciones(servicio_prestamo, servicio_socios, servicio_catalogo)
    
    print("\nVista Creada")
    
    print("\n=============================================")
    print("-- INICIO DE LA SIMULACIÓN DE USO ---")
    print("=============================================")
    
    vista.simular_busqueda_libro("Aleph")
    
    vista.simular_click_prestar(id_socio=1, id_libro=101)
    
    vista.simular_click_prestar(id_socio=2, id_libro=102)
    
    vista.simular_click_alta_socio(nombre="Juan Pérez Repetido", dni="789012")
    
    vista.simular_click_alta_socio(nombre="Carlos Gómez", dni="334455")
    
    vista.simular_click_devolver(id_prestamo=1)
    
    print("\nAgregando nuevo libro")
    servicio_catalogo.agregar_nuevo_libro(titulo="Ficciones", autor="Borges", isbn="xyz")
    
    print("\nSocio inhabilitado intenta prestar")
    vista.simular_click_prestar(id_socio=1, id_libro=103)
    
    print("\n=============================================")
    print("--- FIN DE LA SIMULACIÓN ---")
    print("=============================================")