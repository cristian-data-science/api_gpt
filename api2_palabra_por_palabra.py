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

    # este codigo permite el headless
    webdriver = uc.Chrome(enable_cdp_events=True, headless=False, version_main=112)

    webdriver.get('https://chat.forefront.ai/')
    sleep(3)
    input_text = webdriver.find_element(By.XPATH, value='/html/body/div[1]/main/div[1]/div[3]/div[2]/div[2]/div/div[1]/div/div/div')
    input_text.click()  # Hacer clic en el elemento


    csv = """Resumen de juegos de tronos"""

    texto = csv
    #texto = csv.to_string(index=False)  # Convierte el DataFrame a una cadena de texto sin índices
    #print(csv)



    # Hacer clic en el campo de entrada
    input_text.click()

 
    #input_text.send_keys(texto)
    sleep(0.5)
    # Definimos un tamaño de segmento adecuado, puedes ajustarlo según necesites
    segment_size = 50

    # Dividimos el texto en segmentos
    segments = [texto[i:i+segment_size] for i in range(0, len(texto), segment_size)]

    # Enviamos cada segmento por separado
    for segment in segments:
        input_text.send_keys(segment)
        #sleep(0.03)  # Aquí añadimos una pausa pequeña entre cada segmento

    input_text.send_keys(Keys.ENTER)

    import sys

    palabra_parcial = ''
    respuesta = ''

    while True:
        try:
            elements = WebDriverWait(webdriver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div[4]/div/div[2]/div[1]'))
            )
            nueva_respuesta = ' '.join([element.text for element in elements])

            if nueva_respuesta != respuesta:
                dif_respuesta = nueva_respuesta[len(respuesta.rstrip('.')):]

                if dif_respuesta == "":  # Si no hay texto nuevo, rompe el ciclo
                    break

                for letra in dif_respuesta:
                    if letra == ' ':
                        print(palabra_parcial, end='')
                        sys.stdout.flush()
                        sleep(0.08)
                        palabra_parcial = ''
                        print(' ', end='')
                    else:
                        palabra_parcial += letra
                respuesta = nueva_respuesta
            else:
                sleep(2)
                elements = webdriver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div[4]/div/div[2]/div[1]')
                nueva_respuesta = ' '.join([element.text for element in elements])

                if nueva_respuesta == respuesta:
                    break
                else:
                    dif_respuesta = nueva_respuesta[len(respuesta):]

                    if dif_respuesta == "":  # Si no hay texto nuevo, rompe el ciclo
                        break

                    for letra in dif_respuesta:
                        if letra == ' ':
                            print(palabra_parcial, end='')
                            sys.stdout.flush()
                            sleep(0.08)
                            palabra_parcial = ''
                            print(' ', end='')
                        else:
                            palabra_parcial += letra
                    respuesta = nueva_respuesta
        except:
            pass

    # Imprimir la última palabra parcial si existe
    if palabra_parcial:
        print(palabra_parcial)  


    webdriver.close()

      
    #print(texto)
    #sleep(3000)
