import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)  # espera abrir

pyautogui.write("calc")
pyautogui.press("enter")
time.sleep(2)  # espera a calculadora abrir

# mandar ele apertar e fazer o cálculo 8 + 2
pyautogui.write("8")
pyautogui.press("+")
pyautogui.write("2")
pyautogui.press("enter")

time.sleep(3)
