from UI_layer import Create
from UI_layer import View
from UI_layer import Update

class ProgramUI():
    def login():
        print('''NaN Air flights system
--------------------------------------------
Input your ID to login''')

        loginIDinput = input("Input: ")
        ProgramUI.mainMenu()
        return loginIDinput

    def mainMenu():
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
                ProgramUI.mainMenu()
        elif mainMenuInput == "2":
            createMenuOutput = Create.Create.createMenu()
            if createMenuOutput == "b":
                ProgramUI.mainMenu()
        elif mainMenuInput == "3":
            updateMenuOutput = Update.Update.updateMenu()
            if updateMenuOutput == "b":
                ProgramUI.mainMenu()
        elif mainMenuInput == "q":
            return mainMenuInput
        else:
            print("Wrong input, try again")
            ProgramUI.mainMenu()
        return mainMenuInput