import Warehouse, Display, Rent, Return

def init():
    while True: #infinite loop
        print(f'''
Welcome to Costume Rental Department
{"-" * 80}
Enter your choice
1:  Enter 1 to Rent.
2:  Enter 2 to Return.
3:  Enter 3 to Exit.
{"-" * 80}
''')

        try:
            choice = int(input("Please select your choice: "))
            if choice == 3:
                 print("Thank you for visiting.")
                 exit()

            costumelist = Warehouse.warehouse() #initialize values of global lists
            if choice == 1:
                try:
                    Display.display(costumelist)
                    Rent.rent_costume(costumelist)
                except IndexError:
                    print("Invalid Costume ID. Restarting...")
                    init() #recurse
            elif choice == 2:
                Display.display(costumelist)
                Return.return_costume(costumelist)
            else:
                print("\n\nInvalid number. Please read instructions carefully.\n")
        except ValueError as e:  # if input can not be parsed
            print(f"\n\nPlease input a valid number. {e}")

#initialize the program
init()
