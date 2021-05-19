import os
from mainMenuStartFormClasses import ShowMainMenuFormInStartFile


clearTerminalScreenConsole = lambda: os.system('cls')


showMenu = ShowMainMenuFormInStartFile()
while True:
    showMenu.showMainMenuFormInStartFile()