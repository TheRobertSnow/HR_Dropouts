#from Create import Create
#from Update import Update
#from View import View
from UI_layer import Create
from UI_layer import Update
from UI_layer import View

class ProgramUI():
    def loginWindow():
        print('''NaN Air flights system
--------------------------------------------
Input your ID to login''')

        loginIDinput = input("Input: ")
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
            viewMenuOutput = View.viewMenu()
            if viewMenuOutput == "b":
                ProgramUI.mainMenu()
            elif viewMenuOutput == "q":
                return viewMenuOutput
        elif mainMenuInput == "2":
            createMenuOutput = Create.createMenu()
            if createMenuOutput == "b":
                ProgramUI.mainMenu()
            elif createMenuOutput == "q":
                return createMenuOutput
        elif mainMenuInput == "3":
            updateMenuOutput = Update.updateMenu()
            if updateMenuOutput == "b":
                ProgramUI.mainMenu()
            elif updateMenuOutput == "q":
                return updateMenuOutput
        elif mainMenuInput == "q":
            return mainMenuInput
        else:
            print("Wrong input, try again")
            ProgramUI.mainMenu()
        return mainMenuInput

    loginWindow()
    mainMenu()
