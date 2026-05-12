import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONSTANTES Y SELECTORES (Movidos aquí para evitar errores de importación) ---
USER_INPUT = (By.ID, "user-name")
PASS_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
TITLE_LABEL = (By.CLASS_NAME, "title")
INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_flujo_completo_sauce(driver):
    # --- FASE 1: LOGIN ---
    driver.get("https://www.saucedemo.com/")
    
    # Espera explícita para asegurar que cargó la página
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(USER_INPUT))
    
    driver.find_element(*USER_INPUT).send_keys("standard_user")
    driver.find_element(*PASS_INPUT).send_keys("secret_sauce")
    driver.find_element(*LOGIN_BUTTON).click()

    # Validación de URL e inventario
    assert "inventory.html" in driver.current_url
    header_title = driver.find_element(*TITLE_LABEL)
    assert header_title.text == "Products"

    # --- FASE 2: NAVEGACIÓN Y CATÁLOGO ---
    items = driver.find_elements(*INVENTORY_ITEM)
    assert len(items) > 0
    
    primer_nombre = items[0].find_element(*ITEM_NAME).text
    primer_precio = items[0].find_element(*ITEM_PRICE).text
    print(f"\nProducto: {primer_nombre} | Precio: {primer_precio}")

    # --- FASE 3: CARRITO ---
    items[0].find_element(*ADD_TO_CART_BTN).click()
    
    badge = driver.find_element(*CART_BADGE)
    assert badge.text == "1"

    driver.find_element(*CART_LINK).click()
    assert primer_nombre in driver.page_source