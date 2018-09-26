import pyautogui
from tkinter import Tk
from time import sleep

def ps(times : int = 1000,time : float = 1.5):
    for i in range(times):
        sleep(time)
        pname = Tk().clipboard_get()
        if(pname.startswith("p!catch")):
            pyautogui.typewrite(pname)
            pyautogui.press('enter')
        
        pyautogui.typewrite('SPAM')
        pyautogui.press('enter')
    
