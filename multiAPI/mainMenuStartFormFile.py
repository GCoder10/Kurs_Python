import os
from mainMenuStartFormClasses import ShowMainMenuFormInStartFile
from pynput.keyboard          import Key, Controller


clearTerminalScreenConsole = lambda: os.system('cls')
keyboard                   = Controller()


showMenu = ShowMainMenuFormInStartFile()
while True:
    showMenu.showMainMenuFormInStartFile()
    if showMenu.exitProgram:
        try:
            showMenu.exitProgram = False
            break
        finally:
            keyboard.press(Key.ctrl_l)
            keyboard.press('c')   
            keyboard.release('c')
            keyboard.release(Key.ctrl_l)   