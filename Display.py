def display(CostumeList):
    size = len(CostumeList["name"])
    print("_" * 75)
    print(f"{' '*2}ID{' '*2}{' '*4}Costume Name{' '*5}{' '*5}Costume Brand{' '*4}{' '*2}Price{' '*4}{' '*4}Quantity{' '*2}")
    print("_" * 75)
    for i in range(size):
        tab = ' '*8
        print(f"{' '*2}{CostumeList['id'][i]}{tab}{CostumeList['name'][i]}{' '*(20-len(CostumeList['name'][i]))}{CostumeList['brand'][i]}{' '*(20-len(CostumeList['brand'][i]))}{CostumeList['price'][i]}{' '*10}{CostumeList['quantity'][i]}{' '*4}")
    print("-" * 368)
    
