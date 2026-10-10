from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()


    try:
        # Abrimos SauceDemo e iniciamos sesión
        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Esperamos que aparezca el título del inventario
        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        # Seleccionamos el primer producto y guardamos su nombre
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        # Añadir un producto al carrito haciendo clic en el botón correspondiente (consigna)
        # Agrega primer producto (criterio mínimo)
        primer_producto.find_element(By.TAG_NAME, "button").click()

        # Verificar que el contador del carrito se incremente correctamente (consgina)
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"

        # Navegar al carrito de compras (consigna)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Guardamos el nombre del producto en el carrito
        producto_carrito = driver.find_element(
            By.CLASS_NAME, "inventory_item_name"
        )

        # Comprobar que el producto añadido aparezca correctamente en el carrito (consigna)(criterio mínimo)
        assert producto_carrito.text == nombre_producto

    finally:
        # Cierra el navegador incluso si una validación falla.
        driver.quit()

