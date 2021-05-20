import os
from registerFormClasses import ShowRegisterFormInRegisterFormFile


clearTerminalScreenConsole = lambda: os.system('cls')


showMenu = ShowRegisterFormInRegisterFormFile() 
while True:
    showMenu.showRegisterFormInRegisterFormFile()
    if showMenu.exitRegisterForm:
        showMenu.exitRegisterForm = False
        break