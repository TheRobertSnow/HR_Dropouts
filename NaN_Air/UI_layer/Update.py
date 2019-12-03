class Update():
    def updateMenu():
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
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "2":
            print("")
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "3":
            print("")
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "4":
            print("")
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "5":
            print("")
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "b":
            return updateMenuInput
        elif updateMenuInput == "q":
            return updateMenuInput
        else:
            print("Wrong input, try again")
            updateMenuInput = Update.updateMenu()
        return updateMenuInput