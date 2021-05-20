import os
import keyboard


clearTerminalScreenConsole = lambda: os.system('cls')


class LoginUser():
    def __init__(self, 
                 username: str, 
                 password: str ) -> None:
        self.username = username
        self.password = password
    def __str__(self) -> str:
        pass
    def __getitem__(self):
        pass
    def __setitem__(self) -> None:
        pass
    def __len__(self) -> int:
        pass


class VerifyDataFromLoginFormFunctionsMethods():
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __getitem__(self):
        pass
    def __setitem__(self) -> None:
        pass
    def __len__(self) -> int:
        pass


class ShowLoginFormInLoginFormFile():
    exitLoginForm: bool = False
    def showLoginFormInLoginFormFile(self) -> None:
        print("------------------------------------------------------------------")
        print("| U - Username                                                   |")
        print("| P - Password                                                   |")
        print("| I - Finish login                                               |")
        print("| B - Back                                                       |")
        print("------------------------------------------------------------------")	
        print("Please choose one of the options: ")


        while True:
            try:
                if keyboard.is_pressed('U'):
                    clearTerminalScreenConsole()
                    print("U - Username")
                    input("Username: ")
                    break
                if keyboard.is_pressed('u'):
                    clearTerminalScreenConsole()
                    print("u - Username")
                    input("Username: ")
                    break
                if keyboard.is_pressed('P'):
                    clearTerminalScreenConsole()
                    print("P - Password")
                    input("Password: ")
                    break
                if keyboard.is_pressed('p'):
                    clearTerminalScreenConsole()
                    print("p - Password")
                    input("Password: ")
                    break
                if keyboard.is_pressed('I'):
                    clearTerminalScreenConsole()
                    print("I - Finish login")
                    input("Finish login: ")
                    break
                if keyboard.is_pressed('i'):
                    clearTerminalScreenConsole()
                    print("i - Finish login")
                    input("Finish login: ")
                    break
                if keyboard.is_pressed('B'):
                    self.exitLoginForm = True
                if keyboard.is_pressed('b'):
                    self.exitLoginForm = True
            except:
                break