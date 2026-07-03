# 🗂️ Task Manager API

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.0%2B-E92063?style=flat-square&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-Server-3A7CA5?style=flat-square&logo=uvicorn&logoColor=white)
![Licencia](https://img.shields.io/badge/licencia-MIT-blue?style=flat-square)

---

## 📖 Descripción

**Task Manager API** es una API RESTful ligera y minimalista para la gestión de tareas, construida con **Python** y **FastAPI**. Permite crear, listar, consultar y eliminar tareas de forma sencilla, usando **SQLite** como motor de base de datos y **SQLAlchemy** como ORM. Está diseñada como un proyecto de referencia para aprender los fundamentos de FastAPI, la integración con bases de datos relacionales, y la validación de datos con **Pydantic**.

Ideal para quienes se inician en el desarrollo de APIs con Python o buscan un *boilerplate* limpio para extender con funcionalidades más avanzadas.

---

## 🚀 Tecnologías utilizadas

| Tecnología     | Propósito                               |
|----------------|-----------------------------------------|
| **Python 3.10+**  | Lenguaje de programación              |
| **FastAPI**    | Framework web para construir la API      |
| **SQLAlchemy** | ORM para la interacción con la base de datos |
| **SQLite**     | Motor de base de datos embebido         |
| **Pydantic**   | Validación y serialización de datos     |
| **Uvicorn**    | Servidor ASGI para servir la aplicación |

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/acamilox/Task-Manager-API.git
cd Task-Manager-API
```

### 2. Crear y activar un entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Iniciar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor se levantará en `http://127.0.0.1:8000`. La documentación interactiva (Swagger UI) estará disponible en `http://127.0.0.1:8000/docs`.

---

## 📬 Endpoints

### `POST /tasks/` — Crear una tarea

**Request:**

```json
{
  "title": "Comprar víveres",
  "description": "Leche, pan, huevos y fruta"
}
```

| Campo        | Tipo   | Obligatorio | Descripción          |
|--------------|--------|-------------|----------------------|
| `title`      | string | ✅          | Título de la tarea   |
| `description`| string | ❌          | Descripción detallada |

**Response** `201 Created`:

```json
{
  "id": 1,
  "title": "Comprar víveres",
  "description": "Leche, pan, huevos y fruta",
  "completed": false
}
```

---

### `GET /tasks/` — Listar todas las tareas

**Query parameters:**

| Parámetro | Tipo | Defecto | Descripción                |
|-----------|------|---------|----------------------------|
| `skip`    | int  | `0`     | Número de registros a omitir |
| `limit`   | int  | `100`   | Máximo de registros a devolver |

**Request:**

```
GET /tasks/?skip=0&limit=10
```

**Response** `200 OK`:

```json
[
  {
    "id": 1,
    "title": "Comprar víveres",
    "description": "Leche, pan, huevos y fruta",
    "completed": false
  }
]
```

---

### `GET /tasks/{task_id}` — Obtener una tarea por ID

**Request:**

```
GET /tasks/1
```

**Response** `200 OK`:

```json
{
  "id": 1,
  "title": "Comprar víveres",
  "description": "Leche, pan, huevos y fruta",
  "completed": false
}
```

**Response** `404 Not Found`:

```json
{
  "detail": "Task not found"
}
```

---

### `DELETE /tasks/{task_id}` — Eliminar una tarea

**Request:**

```
DELETE /tasks/1
```

**Response** `200 OK`:

```json
{
  "id": 1,
  "title": "Comprar víveres",
  "description": "Leche, pan, huevos y fruta",
  "completed": false
}
```

**Response** `404 Not Found`:

```json
{
  "detail": "Task not found"
}
```

---

## 📁 Estructura del proyecto

```
Task-Manager-API/
│
├── app/
│   ├── __init__.py          # Convierte app en un paquete Python
│   ├── main.py              # Punto de entrada: instancia FastAPI y define los endpoints
│   ├── database.py          # Configuración de SQLAlchemy + conexión a SQLite
│   ├── models.py            # Modelo ORM Task (id, title, description, completed)
│   ├── schemas.py           # Esquemas Pydantic: TaskBase, TaskCreate, Task
│   └── crud.py              # Operaciones CRUD: get_tasks, create_task, get_task, delete_task
│
├── requirements.txt         # Dependencias del proyecto
├── tasks.db                 # Base de datos SQLite (se genera automáticamente)
├── .gitignore               # Archivos ignorados por Git
└── README.md                # Este archivo
```

### Descripción de los módulos

| Archivo              | Función                                                                  |
|----------------------|--------------------------------------------------------------------------|
| `app/main.py`        | Crea la aplicación FastAPI, define los endpoints y la dependencia `get_db` |
| `app/database.py`    | Configura el motor de SQLite, la sesión y la base declarativa            |
| `app/models.py`      | Define la tabla `tasks` con los campos `id`, `title`, `description`, `completed` |
| `app/schemas.py`     | Define los modelos Pydantic para validación y serialización de datos     |
| `app/crud.py`        | Implementa la lógica de negocio: consultas a la base de datos            |

---

## 🧱 Modelo de datos — Task

| Campo       | Tipo     | Restricciones              |
|-------------|----------|----------------------------|
| `id`        | Integer  | Primary key, autoincremental|
| `title`     | String   | Indexado                   |
| `description`| String  | Nullable, indexado         |
| `completed` | Boolean  | Default: `False`           |

---

## ✅ Mejoras futuras (TODO)

- [ ] Endpoint `PUT /tasks/{task_id}` para actualizar tareas
- [ ] Endpoint `GET /` raíz con mensaje de bienvenida
- [ ] Tests automatizados con `pytest` + `httpx`
- [ ] Contenedor Docker y `docker-compose.yml`
- [ ] Sistema de autenticación (JWT / OAuth2)
- [ ] Paginación con metadatos (total, next, prev)
- [ ] Filtros por estado (`completed=true/false`)
- [ ] Integración continua (CI/CD) con GitHub Actions
- [ ] Migraciones con Alembic

---

## 🤝 Cómo contribuir

1. Haz un *fork* del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz *commit* (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube los cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un *Pull Request*.

Toda contribución es bienvenida. Por favor, asegúrate de que el código siga el estilo existente e incluya tests cuando sea posible.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.
