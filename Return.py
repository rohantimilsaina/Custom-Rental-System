import DateTime as dt

def return_costume(CostumeList):
    """Handles operations for returning costume"""
    count_ = 1
    name = input("Enter your first name: ")
    rent_rec = f"rented-{name}.txt"
    return_rec = f"returned-{name}.txt"
    try:
        f = open(rent_rec)  # opens in read mode by default
        data = f.read()
        f.close()
        f = open(return_rec, "w")
        f.write(f'''Costume Rental Department: \n\n\n
    Returned by: {name} 
    Date: {dt.getCurrentDate()}
    Time: {dt.getCurrentTime()}
    {"_"*77}
    S.N.{' '*4}Costume Name{' '*10}{' '*8}Price{' '*8}{' '*4}Quantity{' '*5}
    {"_"*77}\n''')
        f.close()

        total = 0.0
        # can get size from any key. they all have the same length
        size = len(CostumeList["name"])
        for i in range(size):
            costume = CostumeList['name'][i]
            if costume in data:
                
                f = open(rent_rec)  # open in read mode
                # get how many times this string has repeated in file
                lines = f.readlines()
                f.close()
                
                costume_repeated = 0
                
                for line in lines:
                    
                    if costume in line:
                        
                        num = int(line.split('|')[1].strip())
                        
                        costume_repeated+=num
                
                CostumeList['quantity'][i] += costume_repeated
                f.close()
                
                tab = f"{' '*12}{' '*8}"
                if len(costume) > 14:
                    tab = f" {' '*8}"
                    
                f = open(return_rec, "a")  # open in append mode
                f.write(f"{' '*4}  {count_} {' '*4}{costume}{tab}{CostumeList['price'][i]}{' '*8}{' '*4}{CostumeList['quantity'][i]}{' '*6}\n")
                        # strings can be split without contacting, useful when current line is too long
                        #f"\t\t\t\t{costume_repeated}\n")
                count_ += 1
                f.close()
                total += CostumeList['price'][i] * costume_repeated

        stat = (dt.getDate() - dt.getrentDate(rent_rec)).days
        print(f"You have returned after {stat} days")
        fine = 0
        if stat > 5:
            fine = 2 * (stat - 5)
        f = open(return_rec, "a")
        f.write(f"{' '*4}{'_'*77}\n{' '*4}{' '*60}Fine: ${fine}{' '*7}\n")
        f.close()
        total += fine

        f = open(return_rec, "a+")
        f.write(f"{' '*4}{' '*60}Total: ${total}{' '*4}\n{' '*4}{'_'*77}")
        # return to top of file, by default it is at end when we are appending
        f.seek(0)
        print(f.read())
        f.close()

        f = open("python.txt", "w")  # open in write mode
        # can get size from any key. they all have the same length
        size = len(CostumeList["name"])
        for i in range(size):
            # writing new data to library record file
            f.write(f"{CostumeList['id'][i]},{CostumeList['name'][i]},{CostumeList['brand'][i]},"
                    f"{CostumeList['quantity'][i]},${CostumeList['price'][i]}\n")
        f.close()

    except FileNotFoundError:  # if non existing name is inputted
        print("Please enter correct name")
        return_costume(CostumeList)  # recurse
