import os
from loginFormClasses import ShowLoginFormInLoginFormFile


clearTerminalScreenConsole = lambda: os.system('cls')


showMenu = ShowLoginFormInLoginFormFile()
while True:
    showMenu.showLoginFormInLoginFormFile()