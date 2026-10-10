from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# automatización de login
def test_login_exitoso():

    driver = webdriver.Chrome()

    try:
        # Navegar a la página de login de saucedemo.com (consgina)
        driver.get("https://www.saucedemo.com")

        # Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")(consigna)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs” (criterio mínimo)
        wait = WebDriverWait(driver, 10)

        titulo = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        # Validar login exitoso verificando que se haya redirigido a la página de inventario (consgina)
        assert "/inventory.html" in driver.current_url
        assert titulo.text == "Products"

    finally:
        # Cierra el navegador incluso si algo falla.
        driver.quit()

