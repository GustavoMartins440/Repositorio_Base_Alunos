import pyautogui
from datetime import datetime

# Pega data e hora atual formatada
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Define o nome do arquivo
filename = f"screenshot_{timestamp}.png"

# Tira o print da tela
screenshot = pyautogui.screenshot()

# Salva o arquivo
screenshot.save(filename)

print(f"Screenshot salva como {filename}")
