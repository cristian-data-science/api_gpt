
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
from funciones import envio_recibo_texto

def main():
    st.title("Aplicación de Chat")

    opciones_ia = ["", "Pata: IA de Patagonia", "Otra opción"]  # Agrega una opción vacía al principio
    seleccion_ia = st.selectbox('Selecciona una IA:', opciones_ia)

    texto_usuario = st.text_input('Introduce tu texto aquí:')

    if texto_usuario and seleccion_ia == "Pata: IA de Patagonia":  
        # Se ejecuta si texto_usuario no está vacío y el usuario seleccionó "Pata: La IA de Patagonia"   
        envio_recibo_texto(texto_usuario)

    # Agrega más condiciones si deseas hacer algo cuando el usuario selecciona otras opciones


if __name__ == '__main__':
    main()
