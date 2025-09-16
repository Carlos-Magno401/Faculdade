import pyautogui
import time

# pyautogui.click  clica em algum lugar
# pyautogui.press  aperta 1 tecla
# pyautogui.write  escreve um texto
# pyautogui.hotkay aperta uma combinacao de teclas



pyautogui.PAUSE(0.5) # da um pause de X segundos pra cada comando
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
