from .enums import EstadoSocio

class Socio:
    
    def __init__(self, id_socio, nombre, dni):
        self.id_socio = id_socio
        self.nombre = nombre
        self.dni = dni
        self.estado = EstadoSocio.HABILITADO
        
    def puede_pedir_prestamo(self, cantidad_prestamos_actuales):
        
        if self.estado == EstadoSocio.INHABILITADO:
            print(f'\nEl socio ({self.dni} | {self.nombre}) está inhabilitado.')
            return False
        
        if cantidad_prestamos_actuales >= 3:
            print(f'\nEl socio ({self.dni | self.nombre}) alcanzó el límite de préstamos.')
            return False
        
        print('\nEl socio está habilitado para pedir un préstamo.')
        return True
    
    
    def habilitar(self):
        self.estado = EstadoSocio.HABILITADO
    
    def inhabilitar(self):
        self.estado = EstadoSocio.INHABILITADO
        
        
