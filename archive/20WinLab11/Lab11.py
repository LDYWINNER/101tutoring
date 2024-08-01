
def print_hex(string):
    nums = []
    result = []
    for letter in string:
        nums.append(ord(letter))
    #print(nums)

    for num in nums:
        result.append(HEX(num))
    #print(result)
    print(' '.join(result))


def HEX(num):
    final = []
    decimal_to_hex_string_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                                  7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                                  13: 'D', 14: 'E', 15: 'F'}
    while num >= 16:
        final.append(decimal_to_hex_string_dict[num % 16])
        num //= 16
    final.insert(0, decimal_to_hex_string_dict[num])
    #final.reverse()
    #print(final)
    return ''.join(final)

print_hex("Hello")  # This should print "48 65 6C 6C 6F"