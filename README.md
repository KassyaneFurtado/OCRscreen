# OCRscreen

##### Este projeto realiza a extração de dados de um software ou arquivo, utilizando a biblioteca pytesseract para reconhecimento de texto em imagens.

## Pré-requisitos

##### Certifique-se de ter o Python instalado em seu ambiente. Você pode baixá-lo em [python.org](https://www.python.org/)
##### Além disso, você precisará algumas bibliotecas. Instale-as pelo terminal utilizando os seguintes comandos:
- pip install pytesseract
- pip install python-dotenv
- pip install pandas
- pip install pyautogui 
##### Certifique-se também de ter o Tesseract OCR instalado em seu sistema:  
O arquivo executável do Tesseract OCR foi obtido do repositório mantido pela Universidade de Mannheim [1].

[1] Universidade de Mannheim. Tesseract OCR Repository. Disponível em: https://digi.bib.uni-mannheim.de/tesseract/. Acesso em: 14/02/2024.

## Uso
##### O código realiza a captura de imagem de uma área específica da tela e utiliza o pytesseract para extrair texto dessa imagem, os resultados são salvos em um novo arquivo CSV.
##### *Lembre-se de adaptar as coordenadas de cliques (pyautogui.click), para isso use o arquivo "click_position_finder.py".
