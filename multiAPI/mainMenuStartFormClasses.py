import keyboard
import os


clearTerminalScreenConsole = lambda: os.system('cls')


class ShowMainMenuFormInStartFile():
    def showMainMenuFormInStartFile(self) -> None:
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
                    print("L - Login")
                    input("Login: ")
                    break
                if keyboard.is_pressed('l'):
                    clearTerminalScreenConsole()
                    print("l - Login")
                    input("Login: ")
                    break
                if keyboard.is_pressed('R'):
                    clearTerminalScreenConsole()
                    print("R - Register")
                    input("Register: ")
                    break
                if keyboard.is_pressed('r'):
                    clearTerminalScreenConsole()
                    print("r - Register")
                    input("Register: ")
                    break
                if keyboard.is_pressed('ESC'):
                    break
            except:
                break