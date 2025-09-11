import pyautogui
import time 

print("Você tem 5 segundos para posicionar o mouse em um lugar ...")
time.sleep(5)
print("posicao do mouse", pyautogui.position())