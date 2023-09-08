def warehouse():
    # wrote inside intentionally. dictionary needs to reset on every call
    costumelist = {
        'id': [],
        'name': [],
        'brand': [],
        'price': [],
        'quantity': []
    }
    """initializes the values of lists by reading the file and using proper data structures"""
    f = open("python.txt")
    content = [c.strip("\n") for c in f.readlines()]  # read and strip down line breaks, store lines in an array
    f.close()
    for i in range(len(content)):
        j = 0  # internal counter
        for c in content[i].split(","):
            if j == 0:  # for first element(there should normally be 5 because it is separated by comma in file)
                costumelist['id'].append(int(c))  # 1d list
            elif j == 1:
                costumelist['name'].append(c)
            # convert to int before appending
            elif j == 2:
                costumelist['brand'].append(c)
            elif j == 3:
                costumelist['quantity'].append(int(c))
            # convert to float since price can be in decimal as well
            elif j == 4:
                costumelist['price'].append(float(c.strip().strip("$")))  # remove/strip down $ chars
            j += 1
    return costumelist
