def printUniqueValues(dic):
    myList = list()
    for x in dic.values():
        if x not in myList:
            myList.append(x)
    print(myList)



printUniqueValues({1: "A101", 2: "B10", 300: "A15", 400: "A101", 500: "A15", 600: "B10", 700: "C15"})
printUniqueValues({20: "Acura", 15: "Audi", 10: "BMW", 18: "Audi", 14: "Buick", 11: "Acura", 16: "Cadilac", 24: "ford"})