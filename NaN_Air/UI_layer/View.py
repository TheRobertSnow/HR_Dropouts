class View():
    def viewMenu():
        print('''View Data
--------------------------------------------
  1. View worker
  2. View Airplane
  3. View Flight routes
  4. View Voyages
  5. View Flight 
--------------------------------------------''')
        
        viewMenuInput = input("Input choice(q to Quit, b for Back): ")
        viewMenuInput = viewMenuInput.lower()
        if viewMenuInput == "1":
            print("")
            View.viewMenu()
        elif viewMenuInput == "2":
            print("")
            View.viewMenu()
        elif viewMenuInput == "3":
            print("")
            View.viewMenu()
        elif viewMenuInput == "4":
            print("")
            View.viewMenu()
        elif viewMenuInput == "5":
            print("")
            View.viewMenu()
        elif viewMenuInput == "b":
            return None
        elif viewMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            View.viewMenu()
        return viewMenuInput
