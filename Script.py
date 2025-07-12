from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()

usuario = "GabrielOlmedoITSQMET"
contraseña = "ContraseñaGabrielITSQMET"

driver.find_element(By.ID, "signin2").click()
time.sleep(1)
driver.find_element(By.ID, "sign-username").send_keys(usuario)
driver.find_element(By.ID, "sign-password").send_keys(contraseña)
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(1)

alert = driver.switch_to.alert
alert.accept()
time.sleep(1)

driver.find_element(By.ID, "login2").click()
time.sleep(1)
driver.find_element(By.ID, "loginusername").send_keys(usuario)
driver.find_element(By.ID, "loginpassword").send_keys(contraseña)
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(3)

productos = ["Samsung galaxy s6", "Nexus 6"]

for producto in productos:
    driver.find_element(By.LINK_TEXT, producto).click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(By.ID, "nava").click() 
    time.sleep(2)

driver.find_element(By.ID, "cartur").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
time.sleep(1)
driver.find_element(By.ID, "name").send_keys("Gabriel Olmedo")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Guaranda")
driver.find_element(By.ID, "card").send_keys("1234567890123456")
driver.find_element(By.ID, "month").send_keys("07")
driver.find_element(By.ID, "year").send_keys("2025")
driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
time.sleep(2)

driver.find_element(By.ID, "logout2").click()
time.sleep(2)

driver.quit()