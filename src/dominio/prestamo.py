from .socio import Socio
from .libro import Libro
import datetime

class Prestamo:

    MULTA_POR_DIA = 50.0
    
    def __init__(self, id_prestamo, socio, libro):
        self.id_prestamo = id_prestamo
        self.socio = socio
        self.libro = libro
        self.fecha_prestamo = datetime.date.today()
        self.fecha_devolucion_limite = self.fecha_prestamo + datetime.timedelta(days=14)
        self.esta_activo = True
        
        
    def marcar_como_devuelto(self):
        self.esta_activo = False
        print(f'\nPréstamo con id {self.id_prestamo} devuelto.')
    
    def calcular_multa(self, fecha_hoy):
        
        if not self.esta_activo:
            return 0.0
        
        dias_retraso = (fecha_hoy - self.fecha_devolucion_limite).days
        
        if dias_retraso > 0:
            multa = dias_retraso * self.MULTA_POR_DIA
            print(f'\n Dias de retraso: {dias_retraso} | Valor de la multa: ${multa}')
            return multa
        
        else:
            return 0.0