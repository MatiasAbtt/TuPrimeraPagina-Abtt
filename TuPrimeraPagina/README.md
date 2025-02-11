# TuPrimeraPagina+Abtt

## Descripción del Proyecto
Este proyecto es una aplicación web básica de blog desarrollada en Django utilizando el patrón MVT (Modelo-Vista-Plantilla). La aplicación permite crear autores, categorías y posts, y también buscar posts en la base de datos.

## Requisitos Previos
- Python 3.13+
- Django 5.1.4+
- Navegador web (Chrome, Firefox, etc.)

## Instalación y Configuración
Sigue estos pasos para configurar el proyecto localmente.

1. **Clonar el Repositorio**:
   git clone https://github.com/MatiasAbtt/TuPrimeraPagina-Abtt.git

2. **Crear y activar un entorno virtual**

3. **Instalar las dependencias**
   pip install -r requirements.txt

4. **Realizar las migraciones de la base de datos**
   python manage.py makemigrations
   python manage.py migrate

5. **Ejecutar el servidor**
   python manage.py runserver

6. **Abrir el navegador y visitar**

**USO DEL PROYECTO*
A continuación, se detallan las funcionalidades y el orden para probarlas.

1. **Crear Autor**
URL: http://127.0.0.1:8000/crear_autor/

Descripción: Página para crear un nuevo autor.

Pasos: Rellena el formulario con el nombre y la biografía del autor. Haz clic en "Guardar". Deberías ser redirigido a la página principal.

2. **Crear Categoría**
URL: http://127.0.0.1:8000/crear_categoria/

Descripción: Página para crear una nueva categoría.

Pasos: Rellena el formulario con el nombre de la categoría. Haz clic en "Guardar". Deberías ser redirigido a la página principal.

3. **Crear Post**
URL: http://127.0.0.1:8000/crear_post/

Descripción: Página para crear un nuevo post de blog.

Pasos: Rellena el formulario con el título, contenido, autor y categoría del post. Haz clic en "Guardar". Deberías ser redirigido a la página principal.

4. **Buscar Posts**
URL: http://127.0.0.1:8000/buscar_posts/

Descripción: Página para buscar posts en la base de datos.

Pasos: Utiliza el cuadro de búsqueda para ingresar un término y/o selecciona un post específico del menú desplegable. Haz clic en "Buscar". Deberías ver una lista de posts que coinciden con tu búsqueda.
