from dominio.repositorios import IRepositorioSocios
from dominio.socio import Socio

class ServicioGestionSocios:
    
    def __init__(self, repo_socios):
        self.repo_socios = repo_socios
        
    
    def alta_socio(self, nombre, dni):
        
        socio_existente = self.repo_socios.obtener_por_dni(dni)
        
        if socio_existente:
            return f'\nEl socio con DNI {dni} ya existe.'
        
        nuevo_socio = Socio(id_socio=None, nombre=nombre, dni=dni)
        
        self.repo_socios.guardar(nuevo_socio)
        
        print('\nSocio dado de alta con éxito.')
        return f'\nSocio {nombre} dado de alta.'
    
    def inhabilitar_socio_por_multa(self, id_socio):
        
        socio = self.repo_socios.obtener_por_id(id_socio)
        
        if not socio:
            
            return '\nSocio no encontrado.'
        
        socio.inhabilitar()
        
        self.repo_socios.guardar(socio)
        return f'\nSocio {socio.nombre} fue inhabilitado.'
    
    def habilitar_socio(self, id_socio):
        
        socio = self.repo_socios.obtener_por_id(id_socio)
        
        if not socio:
            return '\nSocio no encontrado'
        
        socio.habilitar()
        
        self.repo_socios.guardar(socio)
        return f'\nSocio {socio.nombre} fue habilitado.'
    
    