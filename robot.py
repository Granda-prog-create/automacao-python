import pyautogui

import pyautogui 

import time

pyautogui.alert("O código vai começar! Não mexa no computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('winleft','d')
pyautogui.moveTo(1168, 445)
pyautogui.mouseDown()
pyautogui.moveTo(1000, 553)
pyautogui.hotkey('alt',  'tab')
time.sleep(1)
pyautogui.mouseUp()
time.sleep(5)
pyautogui.alert("Serviço finalizado!")

pyautogui.position