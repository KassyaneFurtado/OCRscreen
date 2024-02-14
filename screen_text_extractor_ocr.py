import pyautogui
import pytesseract
import time
from dotenv import load_dotenv
import os
import pandas
import pandas as pd
from PIL import Image


# Abrir o prontuário eletrônico
pyautogui.PAUSE=1
pyautogui.click(x=1365, y=757)
pyautogui.doubleClick(x=1313, y=530) #click duplo para abrir o software
time.sleep(10)
pyautogui.click(x=607, y=372)
load_dotenv()
pyautogui.write(os.getenv("usuariomvpep"))
pyautogui.press("tab")
pyautogui.write(os.getenv("senhamvpep"))
pyautogui.press("enter")
# Procurar por cada prontuário usando a base de dados
time.sleep(20)
pyautogui.click(x=563, y=716)
time.sleep(2)
pyautogui.click(x=342, y=191)
pyautogui.click(x=406, y=315)
pyautogui.click(x=120, y=252)
pyautogui.click(x=172, y=353)
pyautogui.click(x=178, y=192)
tabela = pandas.read_csv("PCU.csv")
for linha in tabela.index:
    prontuario = tabela.loc[linha,"PRONTUARIO"]
    pyautogui.write(str(int(tabela.loc[linha,"PRONTUARIO"])))
    pyautogui.press("enter")
    # Coordenadas do canto superior esquerdo
    x1, y1 = 902, 242
    # Coordenadas do canto inferior direito
    x2, y2 = 990, 267
    # Calcula a largura e a altura
    width = x2 - x1
    height = y2 - y1
    # Captura a screenshot da área específica
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    # Salve ou processe a screenshot conforme necessário
    screenshot.save("data_nascimento.png")
    pytesseract.pytesseract.tesseract_cmd = "C:/tesseract/tesseract.exe"
    text = pytesseract.image_to_string("data_nascimento.png")
    print(text)
    df = pd.DataFrame(data=text,columns="DATANASCIMENTO")
    df.head()
