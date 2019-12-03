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
            viewMenuInput = View.viewMenu()
        elif viewMenuInput == "2":
            print("")
            viewMenuInput = View.viewMenu()
        elif viewMenuInput == "3":
            print("")
            viewMenuInput = View.viewMenu()
        elif viewMenuInput == "4":
            print("")
            viewMenuInput = View.viewMenu()
        elif viewMenuInput == "5":
            print("")
            viewMenuInput = View.viewMenu()
        elif viewMenuInput == "b":
            return viewMenuInput
        elif viewMenuInput == "q":
            return viewMenuInput
        else:
            print("Wrong input, try again")
            viewMenuInput = View.viewMenu()
<<<<<<< HEAD
        return viewMenuInput
=======
        return viewMenuInput
>>>>>>> d03aad65c30abfcab49244f5b7ac7b4dad3acb78
