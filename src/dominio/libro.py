from .enums import EstadoLibro

class Libro:
    
    def __init__(self, id_libro, isbn, titulo, autor):
        self.id_libro = id_libro
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.estado = EstadoLibro.DISPONIBLE
    
    
    def esta_disponible(self):
        
        if self.estado == EstadoLibro.PRESTADO:
            print(f'\nEl libro ({self.titulo}) está prestado.')
            return False
        
        print(f'\nEl libro ({self.titulo}) puede ser prestado.')
        return True
    
    def marcar_como_prestado(self):
        self.estado = EstadoLibro.PRESTADO
        
    def marcar_como_disponible(self):
        self.estado = EstadoLibro.DISPONIBLE
        
    