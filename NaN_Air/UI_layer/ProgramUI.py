from Create import Create
from Update import Update
from View import View

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
            View.viewMenu()
            ProgramUI.mainMenu()
        elif mainMenuInput == "2":
            Create.createMenu()
            ProgramUI.mainMenu()
        elif mainMenuInput == "3":
            Update.updateMenu()
            ProgramUI.mainMenu()
        elif mainMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            print(mainMenuInput)
            ProgramUI.mainMenu()
        return mainMenuInput

    loginWindow()
    mainMenu()
