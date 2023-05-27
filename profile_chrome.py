from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Ruta del perfil de usuario. Asegúrate de cerrar todas las instancias de Chrome antes de ejecutar el script.
# De lo contrario, obtendrás un error. Además, cambia '/path/to/profile' a la ruta de tu perfil de Chrome.
user_data_dir = r'C:\Users\Cristian Gutierrez\AppData\Local\Google\Chrome\User Data\Profile 1'

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + user_data_dir)
s=Service(r'C:\chrome_driver\chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options)
sleep(2)
driver.get('https://chat.forefront.ai')
sleep(40)