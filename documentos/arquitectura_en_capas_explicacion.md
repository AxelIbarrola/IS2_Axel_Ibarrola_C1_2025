# Contexto

Debemos diseñar un sistema de gestión para una biblioteca (préstamos de libros, registro de socios, devoluciones, etc.).

## Arquitectura en capas

Dado el contexto del sistema he decido aplicar una arquitectura en capas que permite separar las responsabilidades sin que las capas interfieran con las demás. En este caso voy a trabajar con 4 capas:

- **Capa de presentación**: es la capa encargada de mostrar y solicitar datos. En esta capa no se encuentra la lógica de negocio, simplemente interactúa con el usuario (en este caso el bibliotecario).

- **Capa de servicio**: podríamos ver a esta capa como la orquestadora de nuestro sistema. Su responsabilidad principal es recibir ordenes de la capa de presentación y utiliza las entidades de dominio para ejecutar procesos. Recibe datos simples de la UI y los usa para llamar al dominio al igual que recibe objetos complejos del dominio y los convierte en un objeto simple que la presentación necesita.

- Capa de dominio: esta capa es el corazón de nuestra aplicación puesto que va a contener la definición de las entidades ('Socio, Libro y Préstamo') y la validación interna de los datos dentro de las mismas junto con los métodos que representan sus reglas de negocio.

- Capa de datos: esta capa tiene como mayor responsabilidad la abstracción de la persistencia, es decir, su trabajo más importante es ocultar los detalles de cómo se guardan los datos. Contiene las clases que implementan las interfaces de los repositorios.

Este diseño arquitectónico nos ofrece diversas ventajas a la hora del desarrollo:

- Testeabilidad: nos permite probar cada capa de forma aislada.

- Mantenibilidad: el código es más fácil de entender, encontrar y modificar.

- Bajo acoplamiento: las capas están desacopladas por lo que no dependen fuertemente unas de otras. Solo se comunican a través de interfaces bien definidos.

- Reusabilidad: Como la lógica de negocio y los casos de uso están centralizados, son fácilmente reutilizables por diferentes partes del sistema.

- Trabajo en equipo: Esta separación permite que diferentes equipos trabajen al mismo tiempo sin pisarse.

## Clases principales divididas por capas

### Clases de la capa de dominio

- Socio

  - Propiedades: `idSocio, nombre, dni, estadoSocio`

  - Métodos: `puedePedirPrestamo(cantidadPrestamosActuales), inhabilitar(), habilitar()`

- Libro:

  - Propiedades: `idLibro`, `isbn`, `titulo`, `autor`, `estadoLibro`.

  - Métodos: `estaDisponible()`, `marcarComoPrestado()`, `marcarComoDisponible()`.

- Prestamo:

  - Propiedades: `idPrestamo`, `socio` (referencia a `Socio`), `libro` (referencia a `Libro`), `fechaPrestamo`, `fechaDevolucionLimite`, `estaActivo`.

  - Métodos: `calcularMulta(fechaHoy)`, `marcarComoDevuelto()`.

### Clases de la capa de aplicación

- ServicioPrestamo:
  - Métodos: `realizarPrestamo(idLibro, idSocio)`, `registrarDevolucion(idPrestamo)`.
- ServicioGestionSocios:
  - Métodos: `altaSocio(nombreSocio, dniSocio)`, `inhabilitarSocioPorMulta(idSocio)`, `habilitarSocio(idSocio)`.
- ServicioCatalogoLibros:
  - Métodos: `agregarNuevoLibro(titulo, autor, isbn)`, `buscarLibrosPorTitulo(textoBusqueda)`, `obtenerDetalleLibro(idLibro)`.

## Clases de la capa de acceso a datos

Los repositorios son las clases que actúan como intermediario entre la lógica de negocio y el sistema de almacenamiento.

**INTERFACES**

- `IRepositorioSocios`:
  - Métodos: `obtenerPorId(idSocio)`, `obtenerPorDNI(dni)`, `guardar(socio)`.
- `IRepositorioLibros`:
  - Métodos: `obtenerPorId(idLibro)`, `buscarPorTitulo(titulo)`, `guardar(libro)`.
- `IRepositorioPrestamos`:
  - Métodos: `obtenerActivosPorSocio(idSocio)`, `obtenerPorId(idPrestamo)`, `guardar(prestamo)`.

**CLASES QUE IMPLEMENTAN LAS INTERFACES**

- SociosRepository:
  - Implementa `IRepositorioSocios`.
- LibrosRepository:
  - Implementa `IRepositorioLibros`.
- PrestamosRepository:
  - Implementa `IRepositorioPrestamos`.
