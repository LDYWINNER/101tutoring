# TODO: Complete this function for task 1
# ??????????????????????????????????????????????????
# Use try-except block to handle errors
def check_number1(s):
    year = s % 100
    if year < 10:
        year = '0' + str(year)


    # TODO: Complete this function for task 2


# Use string methods to handle errors
def check_number2(s):
    ...


def go():
    year = input("Year of birth (YYYY): ")
    month = input("Month of birth (MM): ")
    day = input("Day of birth (DD): ")

    year = check_number1(year)
    month = check_number1(month)
    day = check_number1(day)

    # year = check_number2(year)
    # month = check_number2(month)
    # day = check_number2(day)

    print(year, month, day)  # Should print 020501 for 2002 May 1st


go()
