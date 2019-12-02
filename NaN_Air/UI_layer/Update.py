class Update():
    def updateMenu(self):
        print('''Update Data
--------------------------------------------
  1. Update Worker
  2. Update Current Airplanes
  3. Update Current Flights routes
  4. Update Voyages
  5. Update Flights
--------------------------------------------''')
        
        updateMenuInput = input("Input choice(q to Quit, b for Back): ")
        updateMenuInput = updateMenuInput.lower()
        if updateMenuInput == "1":
            print("")
            Update.updateMenu()
        elif updateMenuInput == "2":
            print("")
            Update.updateMenu()
        elif updateMenuInput == "3":
            print("")
            Update.updateMenu()
        elif updateMenuInput == "4":
            print("")
            Update.updateMenu()
        elif updateMenuInput == "5":
            print("")
            Update.updateMenu()
        elif updateMenuInput == "b":
            return None
        elif updateMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateMenu()
        return updateMenuInput
