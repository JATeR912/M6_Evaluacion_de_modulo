# Gestor de Tareas

## Descripción
Gestor de Tareas es una aplicación web desarrollada en Django que permite a los usuarios registrar, listar, editar y eliminar sus tareas personales. Cada usuario puede gestionar únicamente sus propias tareas, con autenticación segura mediante el sistema de usuarios de Django.

La interfaz utiliza **Bootstrap 5** para un diseño responsivo y amigable.

---

## Características
- Registro, inicio y cierre de sesión de usuarios.
- Gestión de tareas privadas por usuario:
  - Listar tareas.
  - Agregar nuevas tareas.
  - Editar tareas existentes.
  - Eliminar tareas.
- Vista de detalle de cada tarea.
- Interfaz responsiva con Bootstrap.
- Simulación de entorno de producción usando **WhiteNoise** para servir archivos estáticos.

---

## Tecnologías
- Python 3.x
- Django 5.2.7
- Bootstrap 5
- WhiteNoise 6.11.0
- SQLite (base de datos por defecto, para fines educativos)
  
Dependencias adicionales están listadas en `requirements.txt`.

---

## Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/JATeR912/M6_Evaluacion_de_modulo
cd gestor_tareas
```

2. **Crear un entorno virtual**

```bash
python -m venv venv
```

- Activar el entorno virtual:

```bash
# Linux/macOS
source venv/bin/activate
```

```bash
# Windows
venv\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Migrar la base de datos**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (opcional)**

```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor de desarrollo**

```bash
python manage.py runserver
```

- Acceder a la aplicación en: http://127.0.0.1:8000/

---

## Rutas URL

- Página principal: `/`
- Registro de usuario: `/registro/`
- Inicio de sesión: `/login/`
- Lista de tareas: `/lista/`

### Gestión de tareas
- Agregar tarea: `/agregar/`
- Editar tarea: `/tarea/<id>/`
- Eliminar tarea: `/eliminar/<id>/`

> Nota: Solo los usuarios autenticados pueden acceder a la lista y gestionar sus tareas.

---

## Estructura del Proyecto

```bash
gestor_tareas/
├─ gestor_tareas/         # Proyecto Django
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ tareas/                # Aplicación de tareas
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  ├─ urls.py
│  └─ templates/
│      ├─ base.html
│      ├─ index.html
│      ├─ lista.html
│      ├─ detalle.html
│      ├─ agregar.html
│      ├─ eliminar.html
│      ├─ login.html
│      ├─ logout.html
│      └─ registro.html
├─ manage.py
├─ requirements.txt
└─ db.sqlite3
```

---

## Configuración de Producción (Educativa)

Para simular un entorno de producción en máquina local, en `settings.py`:

```bash
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```