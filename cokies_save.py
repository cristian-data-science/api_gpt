from selenium import webdriver
import pickle
from time import sleep

driver = webdriver.Chrome()  # Reemplaza 'Chrome' con el navegador que estés utilizando
driver.get("https://chat.forefront.ai")

# Inicia sesión aquí como lo hagas normalmente. Puedes automatizar esto con Selenium si lo prefieres.

sleep(40)
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.close()