# Pre-entrega de QA Automation

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar tests funcionales de la página [SauceDemo](https://www.saucedemo.com/) con Selenium y pytest.

Se implementan tests para verificar el inicio de sesión, la navegación por el catálogo de productos y la interacción con el carrito de compras.

## Tecnologías utilizadas

* **Python:** lenguaje de programación utilizado para desarrollar las pruebas.
* **Selenium WebDriver:** automatización de la interacción con el navegador.
* **pytest:** ejecución y organización de las pruebas automatizadas.
* **pytest-html:** generación de reportes HTML.
* **Google Chrome:** navegador utilizado para ejecutar las pruebas.

## Instalación de dependencias

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/GreatBahamut/pre-entrega-automation-testing-julian-bustos.git
   ```

2. Entrar en la carpeta del proyecto:

   ```bash
   cd preentrega
   ```

3. Instalar las dependencias:

   ```bash
   pip install selenium pytest pytest-html
   ```

También es necesario tener Google Chrome instalado y disponer de un controlador compatible con el navegador. Selenium puede gestionar el controlador automáticamente en las versiones compatibles.

## Pruebas automatizadas

El proyecto contiene las siguientes pruebas:

* **Login (`test_login.py`):** verifica el inicio de sesión con credenciales válidas y el acceso al inventario.
* **Catálogo (`test_catalogo.py`):** verifica el título de la página, la presencia de productos, elementos de la interfaz y muestra el nombre y el precio del primer producto.
* **Carrito (`test_carrito.py`):** agrega el primer producto al carrito, verifica el contador y comprueba que el producto aparezca en el carrito.

## Cómo ejecutar las pruebas

Desde la carpeta raíz del proyecto, ejecutar todas las pruebas con:

```bash
pytest -v tests/
```

Para ejecutar una prueba individual:

```bash
pytest -v tests/test_login.py
```

```bash
pytest -v tests/test_catalogo.py
```

```bash
pytest -v tests/test_carrito.py
```

## Generación del reporte HTML

Para ejecutar todas las pruebas y generar un reporte HTML, utilizar:

```bash
pytest -v tests/ --html=reports/reporte.html
```

El reporte se genera en la carpeta `reports`, dentro del proyecto.
