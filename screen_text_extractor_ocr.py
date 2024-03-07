# Antes de executar o código abrir o software e deixar na pagina de pesquisa
import pytesseract
from dotenv import load_dotenv
import pandas
import pyautogui
import time
import pandas as pd


time.sleep(3)
pyautogui.PAUSE=1
pytesseract.pytesseract.tesseract_cmd = "C:/tesseract/tesseract.exe"
tabela = pandas.read_csv("PACIENTES.csv", converters={"DATANASCIMENTO": str, "PRONTUARIO": str})
time.sleep(5) # Tempo para trocar para a tela do software
# Adicionar filtros de pesquisa
pyautogui.click(x=344, y=190)
pyautogui.click(x=417, y=314)
pyautogui.click(x=119, y=252)
time.sleep(1)
# Pesquisar prontuarios
pyautogui.click(x=183, y=347)
time.sleep(1)
for i in tabela.index:
    pyautogui.click(x=127, y=188)
    prontuario = tabela.loc[i,"PRONTUARIO"]
    pyautogui.write(prontuario)
    pyautogui.press("enter")
    time.sleep(3)
    # Coordenadas do canto superior esquerdo
    x1, y1 = 902, 242
    # Coordenadas do canto inferior direito
    x2, y2 = 990, 267
    # Calcula a largura e a altura
    width = x2 - x1
    height = y2 - y1
    # Captura a screenshot da área específica
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    tabela.loc[i, "DATANASCIMENTO"] = pytesseract.image_to_string(screenshot).strip()
    pyautogui.doubleClick(x=127, y=188)
    pyautogui.press("delete")
    tabela.to_csv("PACIENTES.csv", index=False)


