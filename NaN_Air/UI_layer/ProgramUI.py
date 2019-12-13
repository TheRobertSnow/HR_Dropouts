from UI_layer import Create
from UI_layer import View
from UI_layer import Update
import UIAPI

class ProgramUI:
    def __init__(self):
        self.object = UIAPI.UIAPI()

    def login(self):
        print("""
     $$   $$   $$$$   $$   $$    $$$$   $$  $$$$$
     $$$  $$  $$  $$  $$$  $$   $$  $$  $$  $$  $$
     $$ $ $$  $$$$$$  $$ $ $$   $$$$$$  $$  $$$$$
     $$  $$$  $$  $$  $$  $$$   $$  $$  $$  $$  $$
     $$   $$  $$  $$  $$   $$   $$  $$  $$  $$  $$
     
 $$$$   $$  $$$$$   $$      $$  $$   $$  $$$$$$   $$$$
$$  $$  $$  $$  $$  $$      $$  $$$  $$  $$      $$
$$$$$$  $$  $$$$$   $$      $$  $$ $ $$  $$$$$    $$$$ 
$$  $$  $$  $$  $$  $$      $$  $$  $$$  $$          $$
$$  $$  $$  $$  $$  $$$$$$  $$  $$   $$  $$$$$$   $$$$ 

                        |__^__|
                           |
                       /‾‾‾‾‾‾‾\\
                      /  _____  \\
                     /  |_____|  \\
   \\----+--/‾\\--+--<|             |>--+--/‾\\--+----/
    \\---+--\\_/--+--<|             |>--+--\\_/--+---/
                     \\           /
                     /\\_________/\\
                   !!!     |     !!!
                          !!!
          
--------------------------------------------------------
Input your SSN to login""") 
        
        while True:
            loginSSNinput = input("Input SSN(1234512345 given for testing purposes): ")
            manager = self.object.viewWorkerBySSn(loginSSNinput, "Manager")
            if type(manager) != str:
                print("\nLogin Successfull!\n")
                break
            else:
                print("Wrong input, try again!")
        ProgramUI.mainMenu(self)
        return loginSSNinput

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
            viewMenuOutput = View.View.viewMenu(self.object)
            if viewMenuOutput == "b":
                ProgramUI.mainMenu(self)
        elif mainMenuInput == "2":
            createMenuOutput = Create.Create.createMenu(self.object)
            if createMenuOutput == "b":
                ProgramUI.mainMenu(self)
        elif mainMenuInput == "3":
            updateMenuOutput = Update.Update.updateMenu(self.object)
            if updateMenuOutput == "b":
                ProgramUI.mainMenu(self)
        elif mainMenuInput == "q":
            return mainMenuInput
        else:
            print("Wrong input, try again")
            ProgramUI.mainMenu(self)
        return mainMenuInput
