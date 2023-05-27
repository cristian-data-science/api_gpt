
import streamlit as st
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import sys
import textwrap
from typing import Optional

driver: Optional[webdriver.Chrome] = None

def prender_ia():
    global driver
    st.info("Encendiendo la IA... por favor espere.")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    driver = uc.Chrome(enable_cdp_events=True, headless=False, version_main=112)
    driver.get('https://chat.forefront.ai/')
    sleep(3)

def envia_texto(texto_usuario):
    global driver
    if driver is None:
        raise Exception("No se ha iniciado la IA")

    input_text = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[2]/div[2]/div/div[1]/div/div/div')
    input_text.click()
    segment_size = 50
    segments = [texto_usuario[i:i+segment_size] for i in range(0, len(texto_usuario), segment_size)]
    for segment in segments:
        input_text.send_keys(segment)
        sleep(0.5)
    input_text.send_keys(Keys.ENTER)

def recibe_texto():
    global driver
    if driver is None:
        raise Exception("No se ha iniciado la IA")

    respuesta = ''
    output = st.empty()
    palabra_parcial = ''
    texto_cache = ''
    while True:
        try:
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div[4]/div/div[2]/div[1]'))
            )
            nueva_respuesta = ' '.join([element.text for element in elements])

            if nueva_respuesta != respuesta:
                dif_respuesta = nueva_respuesta[len(respuesta.rstrip('.')):]

                if dif_respuesta == "":
                    break

                for letra in dif_respuesta:
                    if letra == ' ':
                        texto_cache += palabra_parcial + ' '
                        output.text(textwrap.fill(texto_cache, 80))
                        palabra_parcial = ''
                        sleep(0.1)
                    else:
                        palabra_parcial += letra
                respuesta = nueva_respuesta
            else:
                sleep(2)
                elements = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div[4]/div/div[2]/div[1]')
                nueva_respuesta = ' '.join([element.text for element in elements])

                if nueva_respuesta == respuesta:
                    break
                else:
                    dif_respuesta = nueva_respuesta[len(respuesta):]

                    if dif_respuesta == "":
                        break

                    for letra in dif_respuesta:
                        if letra == ' ':
                            texto_cache += palabra_parcial + ' '
                            output.text(textwrap.fill(texto_cache, 80))
                            palabra_parcial = ''
                            sleep(0.1)
                        else:
                            palabra_parcial += letra
                    respuesta = nueva_respuesta
        except:
            pass

    if palabra_parcial:
        texto_cache += palabra_parcial
    output.text(textwrap.fill(texto_cache, 80))