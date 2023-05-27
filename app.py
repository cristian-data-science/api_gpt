
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

    

    texto_usuario = st.text_input('Introduce tu texto aquí:')

    if texto_usuario:  # Se ejecuta si texto_usuario no está vacío
        
        envio_recibo_texto(texto_usuario)


if __name__ == '__main__':
    main()
