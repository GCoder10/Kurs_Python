import os
from loginFormClasses import ShowLoginFormInLoginFormFile


clearTerminalScreenConsole = lambda: os.system('cls')


showMenu = ShowLoginFormInLoginFormFile()
while True:
    showMenu.showLoginFormInLoginFormFile()
    if showMenu.exitLoginForm:
        showMenu.exitLoginForm = False
        break