from UI_layer import Create
from UI_layer import View
from UI_layer import Update
import UIAPI

class ProgramUI:
    def __init__(self):
        self.object = UIAPI.UIAPI()

    def login(self):
        print('''NaN Air flight system
--------------------------------------------
Input your ID to login''')

        loginIDinput = input("Input: ")
        ProgramUI.mainMenu(self)
        return loginIDinput

    def mainMenu(self):
        print('''Main Menu
--------------------------------------------
  1. View Data
  2. Create Data
  3. Update Data
--------------------------------------------''')

        mainMenuInput = input("Input choice(q to Quit): ")
        mainMenuInput = mainMenuInput.lower()
        if mainMenuInput == "1":
            outPut = View.View.viewMenu(self.object)
            if outPut == "b":
                ProgramUI.mainMenu(self)
        elif mainMenuInput == "2":
            outPut = Create.Create.createMenu(self.object)
            if outPut == "b":
                ProgramUI.mainMenu(self)
        elif mainMenuInput == "3":
            outPut = Update.Update.updateMenu(self.object)
            if outPut == "b":
                ProgramUI.mainMenu(self)
        elif mainMenuInput == "q":
            return mainMenuInput
        else:
            print("Wrong input, try again")
            ProgramUI.mainMenu(self)
        if outPut == "q":
            return mainMenuInput
        ProgramUI.mainMenu(self)
