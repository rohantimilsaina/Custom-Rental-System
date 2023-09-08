import DateTime as dt
import Warehouse


def rent_costume(CostumeList):
    """Handles operations for renting costume"""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    #using 4 spaces instead of tab characters everywhere because 2tabs are not treated like 8spaces in most ides by default
    rent_rec = f"rented-{first_name}.txt"
    f = open(rent_rec, "w")
    f.write(f'''Costume Rental Department: \n\n
    rented by: {first_name} {last_name} 
    Date: {dt.getCurrentDate()}
    Time: {dt.getCurrentTime()}
    {"_"*77}
    S.N.{" "*4}Costume Name{" "*18}Price{" "*4}{" "*4}Quantity{' '*4}
    {"_"*77}\n''')
    f.close()

    count_ = 1
    total = 0.0
    rented_quantity = 0
    while True:  # until break
        print("Please select an option: ")
        [print(f"Enter {i} to rent costume {CostumeList['name'][i]}") for i in range(len(CostumeList['name']))]
        print("Enter other numbers to return to main menu")

        try:
            index = int(input("Please enter costume ID: "))
            if index < 0:
                # throw index error, which is handled in main method
                raise IndexError 
                
            f = open(rent_rec)
            content = f.read()
            f.close()

            if CostumeList['name'][index] in content:
                print("\n\nThis costume has already been rented.\n")
                continue

            qn = int(input("Enter the quantity of costumes you want to rent: "))

            if CostumeList['quantity'][index] > qn:
                print(f'''{"-"*10}The Costume is available.{"-"*10}''')

                rented_quantity = qn
                f = open(rent_rec, "a")  # in append mode


                tab = f"{' '*12}{' '*8}"
                if len(CostumeList['name'][index]) > 14:
                    tab = f" {' '*8}"

                f.write(
                    f"{' '*4}  {count_} {' '*4}{CostumeList['name'][index]}{tab}{CostumeList['price'][index]}"
                     f"{' '*8}|{' '*4}{rented_quantity}{' '*4}\n")
                f.close()

                total += CostumeList['price'][index]*qn

                CostumeList['quantity'][index] -=  qn
                f = open("python.txt", "w")
                # can get size from any key. they all have the same length
                size = len(CostumeList["name"])
                for i in range(size):
                    f.write(
                        f"{CostumeList['id'][i]},{CostumeList['name'][i]},{CostumeList['brand'][i]},"
                        f"{CostumeList['quantity'][i]},${CostumeList['price'][i]}\n")
                f.close()

                yn = input("Do you want to rent another costume?(y/n): ")
                if yn.lower() != "y":
                    break  # end loop
                count_ += 1

            else:
                print(f'''{"-"*10}The Costume is not available in stock.{"-"*10}''')
        except ValueError:
            print(f"\nPlease enter a valid number.")

    # after while loop ends
    f = open(rent_rec, "a+") # open in read and append mode
    f.write(f"{' ' * 4}{'_'*77}\n{' '*4}{' '*60}Total: ${total}{' '*4}\n{' '*4}{'_'*77}")
    # return to top of file, by default it is at end when we are appending
    f.seek(0)
    print(f.read())
    f.close()
