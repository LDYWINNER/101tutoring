# Name:Seong Joon Kim
# SBUID: 115504349

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Extract statistical information from a list -----------------
# TODO: Complete the implementation of listStatistic() and listStd().

def listStatistic(list_in):
    list_max = 0
    for v in list_in:
        if list_max < v:
            list_max = v
    list_min = 10
    for v in list_in:
        if list_min > v:
            list_min = v
    all_value = 0
    for i in range(len(list_in)):
        all_value += list_in[i]
    list_average = all_value / (len(list_in))

    return list_max, list_min, list_average


def listStd(list_in):
    var = 0
    for i in range(len(list_in)):
        var += abs(int(list_in[i]) - int(listStatistic(list_in)[2])) ** 2
    standard_deviation = (var / (len(list_in) - 1)) ** 0.5
    return standard_deviation


# ---------------------------- Exercise II --------------------------------------
# -----------------         Implement the Lunh Algorithm        -----------------
# TODO: Complete the implementation of reverseList(), doubleOddIndex()
# digitSum(), replaceDoubleDigit(), isCardValid() and lunhAlgorithm()

def reverseList(list_in):
    first_half_stored = list_in[0:int(len(list_in) / 2)]
    for i in range(int(len(list_in) / 2)):
        list_in[i] = list_in[int(len(list_in) - i - 1)]
    first_half = list_in[0:int(len(list_in) / 2)]
    new_list = list_in[int(len(list_in) / 2):] + first_half_stored
    for i in range(int(len(list_in) / 2)):
        new_list[i] = new_list[int(len(new_list) - i - 1)]
    second_half = new_list[0:int(len(new_list) / 2)]
    complete_version = first_half + second_half
    return complete_version


def doubleOddIndex(list_in):
    for i in range(len(list_in)):
        if i % 2 == 1:
            list_in[i] = list_in[i] * 2
        else:
            list_in[i] = list_in[i]
    return list_in


def digitSum(value):
    result = value // 10 + value % 10
    return result


def replaceDoubleDigit(list_in):
    for i in range(len(list_in)):
        list_in[i] = digitSum(list_in[i])
    return list_in


def isCardValid(list_in):
    sum_value = 0
    for i in range(len(list_in)):
        sum_value += int(list_in[i])
    if sum_value % 10 == 0:
        return True
    else:
        return False


def lunhAlgorithm(card_nb):
    reversed_card_nb = reverseList(card_nb)
    lunh_product = doubleOddIndex(reversed_card_nb)
    single_digit_prod = replaceDoubleDigit(lunh_product)
    validity = isCardValid(single_digit_prod)
    return reversed_card_nb, lunh_product, single_digit_prod, validity


# ---------------------------- MAIN FCT ---------------------------------
def main():
    # Exercise 1 main
    my_list = [1, 2, 3, 4, 5, 6]
    list_max, list_min, list_average = listStatistic(my_list)
    print("The max of the list is: ", list_max)
    print("The min of the list is: ", list_min)
    print("The average of the list is: ", list_average)
    list_std = listStd(my_list)
    print("The std of the list is: ", list_std)

    # Exercise 2 main
    card_number = [4, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

    ''' Step-by-step tests (you can remove these  tests when you
    are done with the final function lunhAlgorithm )
    '''
    print("Here is the original card number: ", card_number)
    reversed_card_nb = reverseList(card_number)
    print("Here is the reversed card number: ", reversed_card_nb)
    lunh_product = doubleOddIndex(reversed_card_nb)
    print("One in two element is multipled by 2: ", lunh_product)
    print("Sum the digit in a number: ", digitSum(18))
    single_digit_prod = replaceDoubleDigit(lunh_product)
    print("Replace the double digits in the vector: ", single_digit_prod)
    validity = isCardValid(single_digit_prod)
    print("Is the card valid??", validity)

    # execute the final code
    # print("Is the card valid??", lunhAlgorithm(card_number))


# Run the main code
main()
