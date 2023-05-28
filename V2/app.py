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
from funciones import ChatBot


def get_chat_bot():
    return ChatBot.instance()

def main():
    chat_bot = get_chat_bot()
    st.title("Aplicación de Chat")

    opciones_ia = ["", "Pata: IA de Patagonia", "Otra opción"]
    seleccion_ia = st.selectbox('Selecciona una IA:', opciones_ia)

    if seleccion_ia == "Pata: IA de Patagonia" and chat_bot.driver is None:
        chat_bot.prender_ia()

    texto_usuario = st.text_input('Introduce tu texto aquí:')

    if texto_usuario and seleccion_ia == "Pata: IA de Patagonia":
        chat_bot.envia_texto(texto_usuario)
        chat_bot.recibe_texto()

if __name__ == '__main__':
    main()