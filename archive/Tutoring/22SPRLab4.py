# Name:
# SBUID:

# TODO: Complete this function for task 1
def find_max(lst):
    ind = -1
    max_val = 0

    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            ind = i
    # TODO: Fill here
    return ind, max_val


# TODO: Complete this function for task 2
def print_sums(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i] + lst[j])


lst = [1, 2, 3]
print(find_max(lst))  # Should print out (2, 3)

print_sums(lst)  # See the slides for a printout
