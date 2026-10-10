from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navegacion_catalogo():

    driver = webdriver.Chrome()

    try:
        # Abrimos SauceDemo e iniciamos sesión
        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Esperamos que aparezca el título del inventario
        wait = WebDriverWait(driver, 10)

        titulo = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        # Verificar que el título de la página de inventario sea correcto (consigna)(criterio mínimo)
        assert titulo.text == "Products"

        # Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)(consigna)(criterio mínimo)
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

        assert len(productos) > 0
        assert productos[0].is_displayed()

        # Validar que elementos importantes de la interfaz estén presentes (menú)(consigna)
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

        # Validar que elementos importantes de la interfaz estén presentes (filtro)(consigna)
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

        # obentemos el primer producto
        primer_producto = productos[0]

        # Lista nombre/precio del primero (criterio mínimo)
        nombre = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        precio = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        print(f"nombre del primer producto: {nombre}")
        print(f"Precio del primer producto: {precio}")

    finally:
        # Cierra el navegador incluso si una validación falla.
        driver.quit()

