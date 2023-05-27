import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse, urljoin
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process

def open_window(url):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    #chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--log-level=3")

    # Cambiando a la clase Service
    s=Service(r'C:\chrome_driver\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.maximize_window()
    # URL del dominio que deseas mapear
    driver.get(url)

    time.sleep(3) # Esperar a que la página se cargue
    element = driver.find_element(By.XPATH, '/html/body/div/header/div/div/div/div/div/div/div[2]/div[1]/ul/li[2]/a')
    element.click()
    
    # Agregar una pausa indefinida
    while True:
        time.sleep(1)

if __name__ == '__main__':
    # Crea y comienza 50 procesos para abrir las ventanas de Chrome
    processes = []
    for _ in range(10):
        p = Process(target=open_window, args=('https://www.puntoticket.com/luis-miguel',))
        p.start()
        processes.append(p)

    # Espera a que todos los procesos terminen
    for p in processes:
        p.join()
