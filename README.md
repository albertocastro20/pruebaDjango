# pruebaDjango
# Prueba Técnica - Microservicio de Productos

Este proyecto es una API RESTful desarrollada con Django y Django REST Framework para la gestión de productos.

## Instrucciones de Instalación con Docker

**Nota Importante:** La configuración para Docker y Docker Compose ha sido implementada en su totalidad para cumplir con los requisitos del proyecto. Sin embargo, debido a problemas persistentes con mi entorno local de Docker Desktop en Windows, no pude realizar la verificación final del comando `docker compose up`. Confío en que la configuración es correcta y debería funcionar en un entorno Docker estándar. Como alternativa fiable y probada, he incluido las instrucciones para la ejecución en un entorno local.

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DE-TU-REPOSITORIO>
    cd <nombre-del-repositorio>
    ```

2.  **Construye e inicia los contenedores:**
    ```bash
    docker compose up --build
    ```
    La API debería estar disponible en `http://localhost:8000/api/productos/`.

---

## Instrucciones de Instalación Local (Verificado)

Este método ha sido probado y es 100% funcional.

1.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecuta las migraciones y el servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
    La API estará disponible en `http://127.0.0.1:8000/api/productos/`.

---

## Ejecutar las Pruebas

Para correr las pruebas, ejecuta el siguiente comando en el entorno que hayas activado (local o Docker):
```bash
python manage.py test
```
