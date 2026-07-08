# Reto Full Stack de E-commerce

Esta es una guía de práctica para desarrolladores full-stack de nivel medio. El objetivo es construir funcionalidades para una aplicación de e-commerce usando React y FastAPI.

> **Inicio Rápido**: Ejecuta `docker-compose up --build` para levantar la app, luego lee los retos abajo. Consulta [QUICK_START.md](QUICK_START.md) para solución de problemas.

## 📋 Descripción General

### Implementación Actual

La aplicación actualmente incluye:

- **Backend (FastAPI)**:
  - API de gestión de productos con SQLAlchemy ORM
  - Gestión de carrito de compras con manejo de sesiones
  - Creación y seguimiento de órdenes
  - Base de datos PostgreSQL con almacenamiento persistente
  - Endpoints RESTful
  - Inicialización automática de la base de datos con productos de ejemplo

- **Frontend (React + Vite)**:
  - Listado de productos con imágenes y detalles
  - Funcionalidad de carrito de compras
  - Creación de órdenes
  - Vista de historial de órdenes
  - Diseño responsivo

### Stack Tecnológico

- **Backend**: FastAPI 0.128.0, Python 3.10+, SQLAlchemy 2.0, PostgreSQL 16
- **Frontend**: React 19.0, Vite 6.0
- **Base de datos**: PostgreSQL 16 (con volumen Docker para persistencia)
- **Contenedores**: Docker & Docker Compose

## 🎯 Tu Misión

Completa **uno o más retos** de las 7 tareas siguientes. Puedes elegir según tu tiempo disponible, tus intereses y tu nivel de experiencia.

### Retos Disponibles

**Frontend (con mockups en la carpeta `/mockups`):**
- **Reto 01**: Animación de Agregar al Carrito (Fácil) - 30 min
- **Reto 02**: Modal de Confirmación de Orden (Medio) - 1 hora
- **Reto 02b**: Vista de Detalle de Orden (Medio) - 1-1.5 horas
- **Reto 03**: Sistema de Autenticación (Difícil, Full Stack) - 3-4 horas

**Backend + Frontend:**
- **Reto 04**: Paginación (Fácil) - 45 min - 1 hora
- **Reto 05**: Gestión de Estado de Órdenes (Fácil) - 1 hora
- **Reto 06**: Búsqueda y Filtrado (Medio) - 2-3 horas
- **Reto 07**: Persistencia del Carrito de Compras (Medio) - 1.5-2 horas

### Cómo Abordarlo

1. **Levanta la app**: `docker-compose up --build`
2. **Elige tus retos**: Según el tiempo disponible (ver estimaciones arriba)
3. **Revisa los mockups** (Retos 01-03): Abre los archivos HTML en la carpeta `mockups/` para ver el comportamiento esperado
4. **Lee los requisitos abajo**: Baja para ver los requisitos detallados de cada reto
5. **Implementa y prueba**: Construye las funcionalidades, pruébalas a fondo, haz commits de tu trabajo

### Combinaciones Recomendadas

**Por Tiempo:**
- **Rápido (1-2 horas):** Elige 1-2 retos fáciles
- **Estándar (3-4 horas):** Elige 2-3 retos de dificultad variada
- **Completo (5+ horas):** Completa 4+ retos incluyendo al menos uno difícil

**Por Especialidad:**
- **Desarrolladores Frontend:** Retos 01, 02, 02b (animaciones, modales, vistas)
- **Desarrolladores Backend:** Retos 04, 05, 06 (paginación, estados, filtrado)
- **Desarrolladores Full Stack:** Retos 02, 03, 05 O 04, 06, 07

---

## 📋 Detalle de los Retos

### Reto 01: Animación de Agregar al Carrito (Fácil)

**Tipo:** Frontend
**Tiempo:** 30 minutos
**Mockup:** [`mockups/01-add-to-cart-animation.html`](mockups/01-add-to-cart-animation.html)

Agrega una animación fluida al botón "Agregar al Carrito" cuando se hace clic.

**Requisitos:**
- Animación de escala del botón (reducción a 0.95x)
- Transición de color de azul a verde
- Animación de ícono de check
- Reinicio automático tras completarse la animación (~600ms)

**Criterios de Aceptación:**
- ✓ El botón se anima suavemente al hacer clic
- ✓ Muestra retroalimentación visual al usuario
- ✓ Vuelve al estado normal automáticamente
- ✓ Funciona con múltiples clics rápidos

---

### Reto 02: Modal de Confirmación de Orden (Medio)

**Tipo:** Frontend
**Tiempo:** 1 hora
**Mockup:** [`mockups/02-order-confirmation-modal.html`](mockups/02-order-confirmation-modal.html)

Reemplaza el `alert()` del navegador por un componente modal personalizado.

**Requisitos:**
- Componente modal personalizado con animación de aparición gradual
- Fondo semitransparente
- Mostrar ID de orden y mensaje de éxito
- Botones "Ver Orden" y "Continuar Comprando"
- Cierre al hacer clic fuera o con la tecla Escape
- Diseño responsivo

**Criterios de Aceptación:**
- ✓ El modal aparece con una animación suave
- ✓ Se puede cerrar de varias formas
- ✓ Funciona en dispositivos móviles
- ✓ No se usan alertas del navegador

---

### Reto 02b: Vista de Detalle de Orden (Medio)

**Tipo:** Frontend
**Tiempo:** 1-1.5 horas
**Mockup:** [`mockups/02b-order-detail-view.html`](mockups/02b-order-detail-view.html)

Crea una vista detallada de orden que muestre la información completa de la misma.

**Requisitos:**
- Encabezado de orden con ID y badge de estado
- Grid de información de la orden (fecha, cantidad de ítems, estado de pago, estado de entrega)
- Lista de ítems con imágenes, cantidades y precios
- Resumen de orden con subtotal, envío, impuestos y total
- Botones de acción (Descargar Factura, Rastrear Orden)
- Navegación de regreso
- Badges de estado con colores

**Colores de Estado:**
- Pendiente: Amarillo (#fef3c7 / #92400e)
- Procesando: Azul (#dbeafe / #1e40af)
- Exitosa: Verde (#d1fae5 / #065f46)
- Cancelada: Gris (#f3f4f6 / #4b5563)
- Fallida: Rojo (#fee2e2 / #991b1b)

**Criterios de Aceptación:**
- ✓ Toda la información de la orden se muestra correctamente
- ✓ El badge de estado muestra el color correcto
- ✓ Es responsivo en móvil
- ✓ Se puede regresar al listado de órdenes

---

### Reto 03: Sistema de Autenticación (Difícil, Full Stack)

**Tipo:** Full Stack
**Tiempo:** 3-4 horas
**Mockup:** [`mockups/03-authentication-system.html`](mockups/03-authentication-system.html)

Implementa un sistema completo de autenticación de usuarios.

**Requisitos de Backend:**
- Agregar tabla `users` al esquema de la base de datos
- Implementar hash de contraseñas (bcrypt/argon2)
- Crear endpoints de auth: POST /api/register, POST /api/login, POST /api/logout
- Implementar tokens JWT O autenticación basada en sesión
- Proteger los endpoints de carrito y órdenes (requerir autenticación)
- Asociar órdenes con usuarios autenticados (agregar clave foránea user_id)

**Requisitos de Frontend:**
- Formularios de Login/Registro con cambio de pestañas
- Validación de formularios
- Manejo de estado de autenticación
- Almacenar y usar tokens de auth
- Rutas/componentes protegidos
- Mostrar usuario autenticado en el header
- Funcionalidad de logout
- Login persistente (localStorage/cookies)

**Cambios en la Base de Datos:**
- Crear tabla `users` con id, email, password_hash, created_at
- Agregar clave foránea `user_id` a la tabla `orders`
- Manejar la migración de órdenes anónimas existentes

**Criterios de Aceptación:**
- ✓ Los usuarios pueden registrarse e iniciar sesión
- ✓ Las contraseñas están hasheadas (nunca en texto plano)
- ✓ Se requiere auth para carrito/órdenes
- ✓ Las órdenes están vinculadas a usuarios
- ✓ El login persiste al refrescar la página
- ✓ Mensajes de error adecuados para credenciales inválidas

---

### Reto 04: Paginación (Fácil)

**Tipo:** Backend + Frontend
**Tiempo:** 45 min - 1 hora

Agrega paginación a los endpoints de listado de productos y órdenes.

**Requisitos de Backend:**

Modifica `GET /api/products`:
- Agregar parámetros de consulta: `page` (default: 1), `limit` (default: 10)
- Formato de respuesta:
```json
{
  "items": [...productos...],
  "total": 156,
  "page": 1,
  "limit": 10,
  "pages": 16
}
```

Modifica `GET /api/orders` con la misma estructura de paginación.

**Pistas de Implementación:**
- Usa SQLAlchemy: `.offset((page - 1) * limit).limit(limit)`
- Calcula las páginas: `math.ceil(total / limit)`
- Valida que la página no exceda el total de páginas
- Retorna un array vacío si está fuera de rango

**Requisitos de Frontend:**
- Controles de paginación (Anterior, Siguiente, números de página)
- Mostrar "Mostrando X-Y de Z productos"
- Actualizar llamadas a la API con parámetros de paginación
- Selector de ítems por página (bonus)

**Criterios de Aceptación:**
- ✓ Los productos se paginan correctamente
- ✓ Las órdenes se paginan correctamente
- ✓ Se retornan los metadatos (total, páginas, etc.)
- ✓ El frontend muestra los controles de paginación
- ✓ La navegación entre páginas funciona

---

### Reto 05: Gestión de Estado de Órdenes (Fácil)

**Tipo:** Full Stack
**Tiempo:** 1 hora

Implementa un flujo de estados de orden con transiciones adecuadas.

**Requisitos de Backend:**

1. **Enum de Estado de Orden:**
   - Estados: `pending`, `processing`, `successful`, `cancelled`, `failed`

2. **Nuevo Endpoint:** `PATCH /api/orders/{order_id}/status`
   - Body: `{"status": "processing"}`
   - Validar las transiciones de estado
   - Retornar la orden actualizada

3. **Reglas de Negocio:**
   - Las órdenes nuevas inician como `pending`
   - Transiciones válidas:
     - `pending` → `processing`, `cancelled`
     - `processing` → `successful`, `failed`, `cancelled`
     - `successful` → no puede cambiar (terminal)
     - `cancelled` → no puede cambiar (terminal)
     - `failed` → no puede cambiar (terminal)

**Requisitos de Frontend:**
- Mostrar el estado con badges de colores (ver Reto 02b para los colores)
- Agregar botones de actualización de estado (para pruebas/administración)
- Filtrar órdenes por estado (bonus)
- Mostrar historial de estados (bonus)

**Criterios de Aceptación:**
- ✓ Las órdenes se crean con estado `pending`
- ✓ El estado se puede actualizar vía API
- ✓ Las transiciones inválidas se rechazan con un error
- ✓ El frontend muestra los colores de estado correctos
- ✓ Se puede filtrar por estado (bonus)

---

### Reto 06: Búsqueda y Filtrado (Medio)

**Tipo:** Full Stack
**Tiempo:** 2-3 horas

Agrega búsqueda y filtrado completos al listado de productos.

**Requisitos de Backend:**

Modifica `GET /api/products` para aceptar:
- `search`: Búsqueda en nombre y descripción (sin distinción de mayúsculas/minúsculas)
- `min_price`, `max_price`: Filtro de rango de precio
- `sort_by`: Ordenar por `price`, `name`, o `stock`
- `order`: Orden ascendente o descendente (`asc`/`desc`)

Ejemplo: `GET /api/products?search=wireless&min_price=20&max_price=150&sort_by=price&order=asc&page=1&limit=10`

Todos los filtros deben funcionar en conjunto con la paginación del Reto 04.

**Requisitos de Frontend:**

1. **Barra de Búsqueda:**
   - Búsqueda en tiempo real (con debounce de 300ms)
   - Botón para limpiar la búsqueda
   - Mensaje de "Sin resultados"

2. **Panel de Filtros:**
   - Slider o inputs de rango de precio
   - Dropdown de ordenamiento (Precio Menor-Mayor, Mayor-Menor, Nombre A-Z, etc.)
   - Botón de limpiar todos los filtros

3. **Resultados:**
   - Mostrar los filtros activos
   - Mostrar la cantidad de resultados
   - Actualizar la URL con los parámetros de filtro (bonus)

**Criterios de Aceptación:**
- ✓ La búsqueda funciona en nombre y descripción
- ✓ El filtrado por rango de precio funciona
- ✓ El ordenamiento funciona correctamente
- ✓ Todos los filtros se pueden combinar
- ✓ La búsqueda tiene debounce
- ✓ Se muestran los filtros activos
- ✓ Limpiar filtros funciona

---

### Reto 07: Persistencia del Carrito de Compras (Medio)

**Tipo:** Full Stack
**Tiempo:** 1.5-2 horas

Mejora la persistencia del carrito con expiración automática y limpieza.

**Situación Actual:**
- El carrito está ligado al session_id (basado en navegador)
- Se pierde si se borran las cookies
- No se sincroniza entre dispositivos

**Requisitos de Backend:**

1. **Mejoras:**
   - El carrito ya está en la base de datos ✓
   - Agregar timestamps `created_at` y `updated_at` al modelo Cart
   - Expiración automática de carritos tras 30 días de inactividad
   - Fusionar carritos cuando el usuario inicia sesión (si se usa el Reto 03)

2. **Endpoint de Limpieza:** `DELETE /api/carts/cleanup`
   - Eliminar carritos con más de 30 días de antigüedad
   - Se puede programar con cron o llamar manualmente

**Requisitos de Frontend:**
- Cargar el carrito al iniciar la app
- Sincronizar el carrito cuando cambian los ítems
- Mostrar la última hora de actualización
- Advertencia si el carrito es antiguo (>7 días)
- Permitir al usuario refrescar el carrito

**Criterios de Aceptación:**
- ✓ El carrito persiste entre sesiones del navegador
- ✓ Los carritos antiguos se limpian automáticamente
- ✓ El carrito muestra la última hora de actualización
- ✓ El carrito se fusiona al iniciar sesión (si se usa auth)

---

## 🚀 Primeros Pasos

### Prerrequisitos

- Docker y Docker Compose instalados
- Node.js 22+ (si se ejecuta localmente)
- Python 3.10+ (si se ejecuta localmente)

### Ejecutar con Docker (Recomendado)

1. Clona el repositorio:
```bash
git clone <repository-url>
cd challenge
```

2. Levanta la aplicación:
```bash
docker-compose up --build
```

Esto iniciará tres servicios:
- **Base de datos PostgreSQL** en el puerto 5432
- **API Backend** en el puerto 8000
- **Frontend** en el puerto 3000

La base de datos se inicializará automáticamente con productos de ejemplo en la primera ejecución.

3. Accede a la aplicación:
   - Frontend: http://localhost:3000
   - API Backend: http://localhost:8000
   - Documentación de la API: http://localhost:8000/docs
   - PostgreSQL: localhost:5432 (credenciales en docker-compose.yml)

4. Detén la aplicación:
```bash
docker-compose down
```

Para eliminar el volumen de la base de datos (reiniciar todos los datos):
```bash
docker-compose down -v
```

### Ejecutar Localmente (Desarrollo)

**Nota**: Para desarrollo local, necesitarás PostgreSQL instalado o usar SQLite.

#### Opción 1: Usar Docker solo para la Base de Datos

```bash
# Iniciar solo PostgreSQL
docker-compose up db

# En otra terminal, ejecuta el backend
cd backend
pip install -r requirements.txt
export DATABASE_URL="postgresql://ecommerce:ecommerce123@localhost:5432/ecommerce"
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# En otra terminal, ejecuta el frontend
cd frontend
npm install
npm run dev
```

#### Opción 2: Usar SQLite (Sin Necesidad de PostgreSQL)

```bash
# Backend
cd backend
pip install -r requirements.txt
export DATABASE_URL="sqlite:///./ecommerce.db"
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

## 📚 Documentación de la API

Una vez que el backend esté corriendo, visita http://localhost:8000/docs para la documentación interactiva de la API (Swagger UI).

### Endpoints Clave

**Productos**
- `GET /api/products` - Listar todos los productos
- `GET /api/products/{id}` - Obtener producto por ID

**Carrito**
- `GET /api/cart/{session_id}` - Obtener carrito
- `POST /api/cart/{session_id}/items` - Agregar ítem al carrito
- `PUT /api/cart/{session_id}/items/{product_id}` - Actualizar ítem del carrito
- `DELETE /api/cart/{session_id}/items/{product_id}` - Eliminar ítem
- `DELETE /api/cart/{session_id}` - Vaciar carrito

**Órdenes**
- `POST /api/orders` - Crear orden
- `GET /api/orders` - Listar todas las órdenes
- `GET /api/orders/{id}` - Obtener orden por ID

## 🏗️ Estructura del Proyecto

```
challenge/
├── backend/
│   ├── main.py              # Punto de entrada de la aplicación FastAPI
│   ├── models.py            # Modelos de base de datos SQLAlchemy
│   ├── schemas.py           # Esquemas de validación Pydantic
│   ├── database.py          # Configuración y sesión de base de datos
│   ├── controllers/         # Lógica de negocio
│   │   ├── products.py
│   │   ├── cart.py
│   │   └── orders.py
│   ├── routes/              # Rutas de la API
│   │   ├── products.py
│   │   ├── cart.py
│   │   └── orders.py
│   ├── requirements.txt     # Dependencias de Python
│   ├── Dockerfile
│   └── .dockerignore
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Componente principal de React
│   │   ├── main.jsx        # Punto de entrada de React
│   │   ├── App.css
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── Dockerfile
│   └── .dockerignore
├── mockups/                 # Mockups HTML interactivos para los retos 01-03
│   ├── 01-add-to-cart-animation.html
│   ├── 02-order-confirmation-modal.html
│   ├── 02b-order-detail-view.html
│   └── 03-authentication-system.html
├── docker-compose.yml       # Orquestación multi-contenedor
├── docker-compose.sqlite.yml # Alternativa con SQLite (backup)
├── .gitignore
├── README.md               # ⭐ Este archivo - Guía completa de retos
├── DATABASE.md             # Documentación del esquema de base de datos
├── QUICK_START.md          # Comandos de Docker y solución de problemas
└── TROUBLESHOOTING.md      # Problemas comunes y soluciones
```

## 📝 Guía de Trabajo

1. **Completa los Retos**
   - Prueba cada reto a fondo antes de pasar al siguiente
   - Sigue los requisitos y criterios de aceptación listados arriba

2. **Calidad de Código**
   - Escribe código limpio y legible
   - Sigue las buenas prácticas de PEP 8 en Python y de JavaScript/React
   - Agrega comentarios para lógica compleja
   - Usa nombres de variables y funciones significativos
   - Aplica principios SOLID y componentes reutilizables

3. **Documentación**
   - Actualiza este README con:
     - **Lista de retos completados** (¡lo más importante!)
     - Cualquier suposición realizada
     - Instrucciones de configuración para nuevas funcionalidades
     - Limitaciones conocidas o mejoras futuras
   - Documenta los nuevos endpoints de la API en el código o en el README
   - Agrega comentarios explicando la lógica de negocio compleja

4. **Flujo de Trabajo con Git**
   - Crea una nueva rama para tu trabajo
   - Haz commits atómicos con mensajes claros
   - Mantén tu historial de commits limpio

5. **Pruebas**
   - Prueba todas las nuevas funcionalidades a fondo
   - Verifica que la configuración de Docker funcione correctamente
   - Confirma que la aplicación funciona de extremo a extremo
   - Prueba en distintos navegadores (para los retos de frontend)

6. **Entregables**
   - Código fuente con tus implementaciones
   - README.md actualizado con una sección de **"Retos Completados"** listando lo que construiste
   - (Opcional) Grabación de pantalla o capturas mostrando las funcionalidades

## 📐 Buenas Prácticas y Recomendaciones

Te recomendamos seguir las buenas prácticas de la industria y demostrar tu comprensión de los principios de ingeniería de software:

### Principios de Calidad de Código

**Código Limpio:**
- Escribe código autoexplicativo con nombres significativos de variables y funciones
- Mantén las funciones pequeñas y enfocadas en una sola responsabilidad
- Evita el anidamiento profundo y los condicionales complejos
- Usa convenciones de nombres consistentes (PEP 8 para Python, Airbnb/Standard para JavaScript)
- Elimina el código comentado y las declaraciones de depuración antes de terminar

**Regla del Boy Scout:**
- *"Deja el código más limpio de como lo encontraste"*
- Si modificas código existente, mejóralo (refactoriza, agrega comentarios, corrige nombres)
- No solo agregues a código desordenado - límpialo mientras avanzas
- Esto demuestra apropiación y cuidado por la calidad del código

### Desarrollo Frontend

**Componentes Reutilizables:**
- Extrae patrones de UI comunes en componentes de React reutilizables
- Ejemplo: componentes `<Button>`, `<Card>`, `<Modal>`, `<Badge>`, `<Input>`
- Usa props para hacer los componentes flexibles y configurables
- Evita duplicar JSX - si copias y pegas, probablemente debería ser un componente
- Mantén los componentes enfocados - un componente debe hacer una sola cosa bien

**Buenas Prácticas de Componentes:**
- Separa los componentes de presentación de los de contenedor
- Usa PropTypes o TypeScript para seguridad de tipos (bonus)
- Mantén los archivos de componentes organizados (un componente por archivo)
- Usa los hooks correctamente (useState, useEffect, hooks personalizados)

### Desarrollo Backend

**Principios SOLID:**

1. **Principio de Responsabilidad Única (SRP)**
   - Cada función/clase debe tener una sola razón para cambiar
   - Ejemplo: Separa la lógica de negocio (controllers) del enrutamiento (routes)
   - No mezcles operaciones de base de datos con lógica de negocio

2. **Principio de Abierto/Cerrado**
   - El código debe estar abierto para extensión, cerrado para modificación
   - Usa herencia y composición para extender funcionalidad

3. **Principio de Sustitución de Liskov**
   - Los subtipos deben ser sustituibles por sus tipos base
   - Asegura jerarquías de herencia adecuadas

4. **Principio de Segregación de Interfaces**
   - Los clientes no deberían depender de interfaces que no usan
   - Crea interfaces específicas en lugar de una de propósito general

5. **Principio de Inversión de Dependencias**
   - Depende de abstracciones, no de implementaciones concretas
   - Usa inyección de dependencias cuando sea apropiado

**Arquitectura Limpia:**
- Mantén la lógica de negocio separada del código de framework
- Los controllers manejan la lógica de negocio, las routes manejan HTTP
- Los models definen la estructura de datos, los schemas manejan la validación
- Usa capas de servicio para operaciones complejas

### Diseño de Base de Datos

**Normalización:**
- Diseña esquemas de base de datos normalizados (al menos 3FN)
- Evita la duplicación de datos entre tablas
- Usa claves foráneas para mantener la integridad referencial
- Piensa en las relaciones: Uno-a-Muchos, Muchos-a-Muchos

**Buenas Prácticas:**
- Usa nombres de tablas y columnas significativos
- Agrega índices para columnas consultadas frecuentemente
- Considera cuidadosamente los tipos de datos (no uses VARCHAR para números)
- Usa restricciones (NOT NULL, UNIQUE, CHECK) para reforzar la integridad de los datos
- Documenta los cambios de esquema si modificas la base de datos

### Ingeniería General

**Manejo de Errores:**
- Maneja los errores adecuadamente con bloques try-catch
- Retorna mensajes de error significativos
- Usa los códigos de estado HTTP apropiados
- Registra los errores para depuración

**Seguridad:**
- Valida todas las entradas de usuario
- Sanitiza los datos para prevenir inyección SQL y XSS
- No expongas información sensible en los mensajes de error
- Usa variables de entorno para secretos

**Rendimiento:**
- Evita problemas de consultas N+1
- Usa índices de base de datos de forma inteligente
- Implementa paginación para conjuntos de datos grandes (Reto 04)
- Minimiza los re-renders innecesarios en React

**Pruebas:**
- Escribe pruebas para la lógica de negocio crítica
- Prueba casos límite y escenarios de error
- Usa descripciones de prueba significativas
- Apunta a una alta cobertura en las rutas de código importantes

## 💡 Consejos

- **Lee este README a fondo**: Todos los requisitos, pistas y criterios de aceptación están documentados aquí
- **Elige con criterio**: Elige los retos que mejor demuestren tus fortalezas (no necesitas completar los 7)
- **Calidad sobre cantidad**: Unos pocos retos bien implementados son mejores que muchos hechos con prisa
- **Abre los mockups**: Para los Retos 01-03, abre los archivos HTML en `/mockups` para ver el comportamiento esperado
- **Prueba a fondo**: Asegúrate de que la configuración de Docker funcione y que todas las funcionalidades operen correctamente
- **Sigue los diseños de los mockups**: Iguala las animaciones, colores e interacciones mostradas en los mockups
- **Maneja los errores**: Considera casos límite, valida entradas, usa los códigos de estado HTTP apropiados
- **Documenta bien**: Actualiza el README con lo que construiste, las suposiciones realizadas y cómo probar tu trabajo
- **Revisa los criterios de aceptación**: Cada reto tiene criterios específicos - asegúrate de cumplirlos antes de avanzar
- **Aplica buenas prácticas**: Usa código limpio, principios SOLID, componentes reutilizables (ver sección de Buenas Prácticas)

## ❓ ¿Preguntas?

Si tienes dudas sobre los requisitos de algún reto, documenta tus suposiciones en el README.

---

**¡Éxitos! ¡Disfruta construyendo! 🚀**
