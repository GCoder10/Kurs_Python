import os
import keyboard


clearTerminalScreenConsole = lambda: os.system('cls')


class RegisterNewUser():
    def __init__(self, 
                 firstName:       str, 
                 lastName:        str, 
                 city:            str, 
                 email:           str, 
                 password:        str, 
                 confirmPassword: str, 
                 username:        str, 
                 age:             int ) -> None:
        self.firstName       = firstName
        self.lastName        = lastName
        self.city            = city
        self.email           = email
        self.password        = password
        self.confirmPassword = confirmPassword
        self.username        = username
        self.age             = age
    def __str__(self) -> str:
        pass
    def __getitem__(self):
        pass
    def __setitem__(self) -> None:
        pass
    def __len__(self) -> int:
        pass


class VerifyDataFromRegisterFormFunctionsMethods():
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


class ShowRegisterFormInRegisterFormFile():
    def showRegisterFormInRegisterFormFile(self) -> None:
        print("------------------------------------------------------------------")
        print("| A - First Name                                                 |")
        print("| B - Last Name                                                  |")
        print("| C - City                                                       |")
        print("| D - E-mail                                                     |")
        print("| E - Password                                                   |")
        print("| F - Confirm Password                                           |")
        print("| G - Username                                                   |")
        print("| H - Age                                                        |")
        print("| I - Finish registration                                        |")
        print("| J - Back                                                       |")
        print("------------------------------------------------------------------")
        print("Please choose one of the options: ")


        while True:
            try:
                if keyboard.is_pressed('A'):
                    clearTerminalScreenConsole()
                    print("A - First Name")
                    input("First Name: ")
                    break
                if keyboard.is_pressed('a'):
                    clearTerminalScreenConsole()
                    print("a - First Name")
                    input("First Name: ")
                    break
                if keyboard.is_pressed('B'):
                    clearTerminalScreenConsole()
                    print("B - Last Name")
                    input("Last Name: ")
                    break
                if keyboard.is_pressed('b'):
                    clearTerminalScreenConsole()
                    print("b - Last Name")
                    input("Last Name: ")
                    break
                if keyboard.is_pressed('C'):
                    clearTerminalScreenConsole()
                    print("C - City")
                    input("City: ")
                    break
                if keyboard.is_pressed('c'):
                    clearTerminalScreenConsole()
                    print("c - City")
                    input("City: ")
                    break
                if keyboard.is_pressed('D'):
                    clearTerminalScreenConsole()
                    print("D - E-mail")
                    input("E-mail: ")
                    break
                if keyboard.is_pressed('d'):
                    clearTerminalScreenConsole()
                    print("d - E-mail")
                    input("E-mail: ")
                    break
                if keyboard.is_pressed('E'):
                    clearTerminalScreenConsole()
                    print("E - Password")
                    input("Password: ")
                    break
                if keyboard.is_pressed('e'):
                    clearTerminalScreenConsole()
                    print("e - Password")
                    input("Password: ")
                    break
                if keyboard.is_pressed('F'):
                    clearTerminalScreenConsole()
                    print("F - Confirm password")
                    input("Confirm password: ")
                    break
                if keyboard.is_pressed('f'):
                    clearTerminalScreenConsole()
                    print("f - Confirm password")
                    input("Confirm password: ")
                    break
                if keyboard.is_pressed('G'):
                    clearTerminalScreenConsole()
                    print("G - Username")
                    input("Username: ")
                    break
                if keyboard.is_pressed('g'):
                    clearTerminalScreenConsole()
                    print("g - Username")
                    input("Username: ")
                    break
                if keyboard.is_pressed('H'):
                    clearTerminalScreenConsole()
                    print("H - Age")
                    input("Age: ")
                    break
                if keyboard.is_pressed('h'):
                    clearTerminalScreenConsole()
                    print("h - Age")
                    input("Age: ")
                    break
                if keyboard.is_pressed('I'):
                    clearTerminalScreenConsole()
                    print("I - Finish registration")
                    input("Finish registration: ")
                    break
                if keyboard.is_pressed('i'):
                    clearTerminalScreenConsole()
                    print("i - Finish registration")
                    input("Finish registration: ")
                    break
                if keyboard.is_pressed('J'):
                    clearTerminalScreenConsole()
                    print("J - Back")
                    break
                if keyboard.is_pressed('j'):
                    clearTerminalScreenConsole()
                    print("j - Back")
                    break
            except:
                break