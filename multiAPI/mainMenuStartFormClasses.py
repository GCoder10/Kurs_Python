import keyboard
import os
from loginFormFile    import showMenu as showMenuVariableFromLoginFormFile
from registerFormFile import showMenu as showMenuVariableFromRegisterFormFile


clearTerminalScreenConsole = lambda: os.system('cls')


class ShowMainMenuFormInStartFile():
    exitProgram: bool     = False
    firstProgramRun: bool = True

    
    def showMainMenuFormInStartFile(self) -> None:
        self.firstProgramRun = False
        print("------------------------------------------------------------------")
        print("| System v. 1.0       |   MultiAPI            |   ESC - Exit     |")
        print("| by Imie Nazwisko    |   Choose one option   |                  |")
        print("| All rights reserved |   _________________   |                  |")
        print("------------------------------------------------------------------")
        print("| L -   Login                                                    |")
        print("| R -   Register                                                 |")
        print("| ESC - Exit                                                     |")
        print("------------------------------------------------------------------")
        print("Please choose one of the options: ")


        while True:
            try:
                if keyboard.is_pressed('L'):
                    clearTerminalScreenConsole()
                    while True:
                        showMenuVariableFromLoginFormFile.showLoginFormInLoginFormFile()
                        if showMenuVariableFromLoginFormFile.exitLoginForm:
                            showMenuVariableFromLoginFormFile.exitLoginForm = False
                            break
                    break
                if keyboard.is_pressed('l'):
                    clearTerminalScreenConsole()
                    while True:
                        showMenuVariableFromLoginFormFile.showLoginFormInLoginFormFile()
                        if showMenuVariableFromLoginFormFile.exitLoginForm:
                            showMenuVariableFromLoginFormFile.exitLoginForm = False
                            break                       
                    break
                if keyboard.is_pressed('R'):
                    clearTerminalScreenConsole()
                    while True:
                        showMenuVariableFromRegisterFormFile.showRegisterFormInRegisterFormFile()
                        if showMenuVariableFromRegisterFormFile.exitRegisterForm:
                            showMenuVariableFromRegisterFormFile.exitRegisterForm = False
                            break 
                    break
                if keyboard.is_pressed('r'):
                    clearTerminalScreenConsole()
                    while True:
                        showMenuVariableFromRegisterFormFile.showRegisterFormInRegisterFormFile()
                        if showMenuVariableFromRegisterFormFile.exitRegisterForm:
                            showMenuVariableFromRegisterFormFile.exitRegisterForm = False
                            break
                    break
                if keyboard.is_pressed('ESC'):
                    self.exitProgram = True
            except:
                break