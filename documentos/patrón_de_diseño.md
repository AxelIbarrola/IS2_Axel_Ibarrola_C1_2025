# Resolución de problema mediante un patrón de diseño

El problema que seleccione es el acceso centralizado a la base de datos, todas las clases que forman parte de la capa de datos (repositorios) necesitan acceder a la misma base de datos para realizar sus operaciones. Si cada repositorio debe crear una conexión propia a la base de datos cada vez que necesite utilizarla, nos estariamos enfrentando a la ineficiencia, debido a que abrir y cerrar una conexión es una operación lenta y costosa (bajando el rendimiento), y a la falta de control, lo que dificultaría la gestión de transacciones y el mantenimiento.

Necesitamos una forma de asegurar que exista **una única instancia** que gestione la conexión a la base de datos, y que todos los repositorios usen esa misma instancia. Por eso creí que la mejor forma de afrontar este problema era mediante el patrón singleton.

El patrón singleton es un patrón creacional cuyo objetivo es garantizar que una clase tenga una, y solo una, instancia en toda la aplicación, proporcionando así un único punto de acceso global a ella. Es la solución perfecta dado que nos garantizaría tener una única conexión que utilizarán todos los repositorios.

El código, utilizando Python, podría ser el siguiente:

```python
class GestorConexionDB:

    _instance = None

    def getInstance():

        if GestorConexionDB._instance is None:

            GestorConexionDB._instance = GestorConexionDB()

        else:
            print("Devolviendo instancia ya existente.")

        return GestorConexionDB._instance

    def __init__(self):

        self.conexion_activa = True
        self.host = "localhost"
        print(f"Conexión establecida con {self.host}")
```

Y los repositorios podrían utilizar esa instancia:

```python
class SqlSociosRepository(IRepositorioSocios):

    def __init__(self):
        self.conexion = GestorConexionDB.getInstance()
```
