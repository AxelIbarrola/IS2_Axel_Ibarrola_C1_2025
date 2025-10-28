from dominio.repositorios import IRepositorioLibros
from dominio.libro import Libro

class ServicioCatalogoLibros:
    
    def __init__(self, repo_libros):
        self.repo_libros = repo_libros
        
    
    def agregar_nuevo_libro(self, titulo, autor, isbn):
        
        nuevo_libro = Libro(id_libro=None, isbn=isbn, titulo=titulo, autor=autor)
        
        self.repo_libros.guardar(nuevo_libro)
        
        return f'\nLibro "{titulo} agregado al catálogo.'
    
    
    def buscar_por_titulo(self, titulo):
        
        libro = self.repo_libros.buscar_por_titulo(titulo)
        
        return libro
    
    def obtener_detalle_libro(self, id_libro):
        
        libro = self.repo_libros.obtener_por_id(id_libro)
        return libro  