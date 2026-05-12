# Pre-entrega Automation Testing - SauceDemo

**Estudiante:** Wolf Marcelo Andres  
**Perfil:** Licenciado en Sistemas / Functional Analyst

## 🎯 Propósito del Proyecto
Este proyecto tiene como objetivo automatizar el flujo principal de compra en la plataforma [SauceDemo](https://www.saucedemo.com/). La suite de pruebas valida el ciclo de vida básico del usuario: inicio de sesión, navegación por el catálogo, agregado de productos al carrito y validación de persistencia de datos. 

Se aplicó una estructura modular para separar la lógica de los tests de las configuraciones y utilitarios, asegurando un código mantenible y escalable.

## 🛠️ Tecnologías Utilizadas
*   **Python 3.13**: Lenguaje de programación principal.
*   **Selenium WebDriver**: Automatización de interacciones con el navegador.
*   **Pytest**: Framework de pruebas para la ejecución y aserciones.
*   **Pytest-HTML**: Generación de reportes dinámicos en formato HTML.
*   **Webdriver-Manager**: Gestión automatizada del driver de Chrome para asegurar compatibilidad.

## 📁 Estructura del Repositorio
*   `tests/`: Contiene el archivo `test_saucedemo.py` con la lógica de las pruebas y las fixtures del driver.
*   `utils/`: Carpeta para funciones auxiliares y constantes (selectores, URLs, credenciales).
*   `reports/`: Almacena el reporte `reporte.html` generado tras la ejecución.
*   `requirements.txt`: Listado de librerías y versiones necesarias.

## 📥 Instalación de Dependencias
Para configurar el entorno de trabajo y descargar las librerías necesarias, ejecute el siguiente comando en la terminal:

```bash
pip install -r requirements.txt

Ejecución de la prueba: pytest tests/test_saucedemo.py -v --html=reports/reporte.html

<img width="1521" height="184" alt="image" src="https://github.com/user-attachments/assets/d606e225-0cf0-466a-824c-a5ed55ee066b" />

