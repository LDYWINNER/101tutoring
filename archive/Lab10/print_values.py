
def print_values(**kwargs):
    for key, value in kwargs.items():
        #print("The value of {} is {}".format(key, value))
        print("The key is", key, "and value is", value)

print_values(my_name="Sammy", your_name="Casey")

print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
    )