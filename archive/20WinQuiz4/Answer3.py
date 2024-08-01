
def sum_all_digits(number):
    if number // 10 == 0:
        return number
    return (number % 10) + sum_all_digits(number // 10)


print(sum_all_digits(157))  # Adds the digits 1 + 5 + 7 = 13

print(sum_all_digits(6))

print(sum_all_digits(4222)) # Adds the digits 4+2+2+2