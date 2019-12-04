from UI_layer import Create
from UI_layer import View
from UI_layer import Update
import UIAPI

class ProgramUI:
    def __init__(self):
        self.myInstance = Create.Create()

    def login(self):
        print('''NaN Air flights system
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
            viewMenuOutput = View.View.viewMenu()
            if viewMenuOutput == "b":
                ProgramUI.mainMenu(self)
            #elif viewMenuOutput == "q":
                #return viewMenuOutput
        elif mainMenuInput == "2":
            createMenuOutput = Create.Create.createMenu(self.myInstance)
            if createMenuOutput == "b":
                ProgramUI.mainMenu(self)
            #elif createMenuOutput == "q":
                #return createMenuOutput
        """elif mainMenuInput == "3":
            updateMenuOutput = Update.Update.updateMenu()
            if updateMenuOutput == "b":
                ProgramUI.mainMenu()
            #elif updateMenuOutput == "q":
                #return updateMenuOutput
        elif mainMenuInput == "q":
            return mainMenuInput
        else:
            print("Wrong input, try again")
            ProgramUI.mainMenu()
        return mainMenuInput"""

