import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd
from time import sleep





if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    #options.headless = False
    options.add_argument("--start-maximized")
    options.add_argument('--headless=new')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
    #webdriver = uc.Chrome(options=options)

    #webdriver = uc.Chrome(executable_path='C:\\chrome_driver\\chromedriver.exe', enable_cdp_events=True, headless=True, version_main=113)

    # este codigo permite el headless
    webdriver = uc.Chrome(enable_cdp_events=True, headless=True, version_main=113)

    webdriver.get('https://chat.forefront.ai/')
    sleep(3)
    input_text = webdriver.find_element(By.XPATH, value='/html/body/div[1]/main/div[1]/div[3]/div[2]/div[2]/div/div[1]/div/div/div')
    input_text.click()  # Hacer clic en el elemento
    texto = input("Ingrese el texto: ")
    # Envío del texto al campo de entrada
    input_text.send_keys(texto + " .responde en un solo parrafo")

    input_text.send_keys(Keys.ENTER)
    sleep(1)

    import sys

    respuesta = ''
    while True:
        try:
            elements = WebDriverWait(webdriver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div[4]/div/div[2]/div[1]/div'))
            )
            nueva_respuesta = '\n\n'.join([element.text for element in elements]) # Une los elementos de texto con un salto de línea en lugar de un espacio

            if nueva_respuesta != respuesta:
                dif_respuesta = nueva_respuesta[len(respuesta.rstrip('.')):]

                if dif_respuesta.strip() == "":  # Si no hay texto nuevo, rompe el ciclo
                    break
                
                for letra in dif_respuesta:
                    print(letra, end='')
                    sys.stdout.flush()
                    sleep(0.02)
                respuesta = nueva_respuesta
            else:
                sleep(2)  # Espera adicional para darle a la página web la oportunidad de generar más texto
                elements = webdriver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div[4]/div/div[2]/div[1]/div')
                nueva_respuesta = '\n'.join([element.text for element in elements])  # Une los elementos de texto con un salto de línea en lugar de un espacio
                if nueva_respuesta == respuesta:
                    break
                else:
                    dif_respuesta = nueva_respuesta[len(respuesta):]

                    if dif_respuesta.strip() == "":  # Si no hay texto nuevo, rompe el ciclo
                        break

                    for letra in dif_respuesta:
                        print(letra, end='')
                        sys.stdout.flush()
                        sleep(0.02)
                    respuesta = nueva_respuesta
        except:
            pass

    webdriver.close()        
    #print(respuesta)
    #sleep(3000)
