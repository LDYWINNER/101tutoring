# Part 1
def dictionary_test():

    d = {'one': 'hana',
         'two': 'dul',
         'three': 'set'}

    # As you try these 6 examples below, be sure to understand what
    # each example is trying to teach you about dictionaries.

    print('\n1. keys')
    for key in d:
        print(key)

    # one
    # two
    # three

    """ Uncomment one more example at a time until you are done with Part 0. """

    print('\n2. keys once more')
    for key in d.keys():
        print(key)

    # one
    # two
    # three

    print('\n3. values')
    for value in d.values():
        print(value)

    # hana
    # dul
    # set

    print('\n4. items')
    for item in d.items():
        print(item)

    # (one, hana)
    # (two, dul)
    # (three, set)

    print('\n5. items once more')
    for item in d.items():
        print(item[0], item[1])

    # one hana
    # two dul
    # three set

    print('\n6. items yet once more')
    for key, value in d.items():
        print(key, value)

    # one hana
    # two dul
    # three set

    return None

# Part 2
def price_check():
    prices = {
        "banana": 4,
        "apple": 2,
        "kiwi": 6,
        "orange": 1.5,
        "pear": 3.3,
        "mango": 4.5,
    }

    orange_price = prices["orange"] # 1.5
    print("Orange: ", orange_price) # Orange: 1.5

    # Write code to calculate the price of a pear
    #  by using the prices dictionary
    pear_price = prices["pear"]
    print("Pear: ", pear_price) # Pear: 3.3

    # Write code to calculate the price of a banana + apple
    #  by using the prices dictionary
    total = prices["banana"] + prices["apple"]
    print("Banana + Apple = ", total) # Banana + Apple = 6

    # Write code to check for the price of a papaya, which
    #  is not in the dictionary. This will crash your program
    #  so use an if statement check if papaya is in the dictionary
    #  and print out -1 when the price does not exist
    papaya_price = 0

    if "papaya" in prices:
        papaya_price = prices["papaya"]
    else:
        papaya_price = -1

    print("Papaya: ", papaya_price) # Papaya: -1

    # Set papaya to have a price of 5 in the dictionary
    prices.setdefault("papaya", 5)

    # Now copy the above code that checks for the price of papaya
    #  and run it again. Confirm the price is 5
    papaya_price = prices["papaya"]

    print("Papaya (after adding a price): ", papaya_price) # Papaya (after adding a price): 5

# Part 3
# Implement this function as described in the lab instructions
def destination(max_distance, places):
    # make a dict with the items that have a value that is smaller than "max_distance"
    # find the maximum with in that dict <----

    distances = {'Busan': 330, 'Incheon': 27, 'Daegu': 237, 'Addis Ababa': 9230,
                'Bishkek': 4409, 'Nay Pyi Taw': 3572, 'Taipei': 1482,
                'London': 8845, 'New York City': 11038, 'Shanghai': 867,
                'Mumbai': 5587, 'Buenos Aires': 19406, 'Paris': 8945}

    fit = {}

    for item in places.items():
        if item[1] < max_distance:
            fit.setdefault(item[0], item[1])

    max = 0
    values = list(fit.values())
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]

    keys = list(places.keys())

    for key in places:
        if places[key] == max:
            return key

    if max_distance != 0:
        return "Nowhere"
    else:
        return None


# Part 4
# Implement this function as described in the lab instructions.
def shop(filename, shopping_list):
    prices = {}
    for line in open(filename):
        line_split = line.split(",")
        prices.setdefault(line_split[0], float(line_split[1]))

    shopping_list_split = shopping_list.split(",")
    shopping_dict = {}
    for i in range(0, len(shopping_list_split) - 1, 2):
        shopping_dict.setdefault(shopping_list_split[i], float(shopping_list_split[i + 1]))

    price = 0
    for key in shopping_dict:
        if key in prices:
            price += prices[key] * shopping_dict[key]

    return price


def main():
    # Part 1
    dictionary_test()
    print()

    """ Uncomment one part at a time until you are done. """
    # Part 2
    price_check()
    print()

    # Part 3

    # This is a dictionary of distances from Seoul to other cities (in kilometers)
    distances = {'Busan': 330, 'Incheon': 27, 'Daegu': 237, 'Addis Ababa': 9230,
                 'Bishkek': 4409, 'Nay Pyi Taw': 3572, 'Taipei': 1482,
                 'London': 8845, 'New York City': 11038, 'Shanghai': 867,
                 'Mumbai': 5587, 'Buenos Aires': 19406, 'Paris': 8945}

    print("The farthest city <= 400 km: ", destination(400, distances)) # prints Busan
    print("The farthest city <= 0 km: ", destination(0, distances))  # prints None
    print("The farthest city <= 4500 km: ", destination(4500, distances)) # prints Bishkek
    print("The farthest city <= 10 km: ", destination(10, distances)) # prints "Nowhere"

    # Part 4
    # Be sure to import the prices1.txt, prices2.txt, and prices3.txt files

    list1 = ''
    list2 = 'Ketchup,4,Mustard,10,tooth paste,1,Avocados,1'
    list3 = 'Tuna,1,Honey,1,Free Rice,79,Ginger Bread,4'

    print("Shopping with prices1.txt: ", shop('prices1.txt', list1)) # returns 0.0
    print("Shopping with prices2.txt: ", shop('prices2.txt', list2)) # returns 29.11
    print("Shopping with prices3.txt: ", shop('prices3.txt', list3)) # returns 1.87

    # end of block comment

if __name__ == '__main__':
    main()