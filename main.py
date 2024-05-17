import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

pywhatkit.sendwhatmsg("+919027456832","This is a automate whatsapp message tutorial",14,46)
time.sleep(10)
pyautogui.click()
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
print("Message sent!")