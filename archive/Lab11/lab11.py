# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def print_hex(string):
    decimal_to_hex_string_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6',
                           7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C',
                           13:'D', 14:'E', 15:'F' }
    result = ''
    for c in string:
        x = ord(c)
        quotient = x // 16
        remainder = x % 16

        result += str(quotient)
        result += decimal_to_hex_string_dict[remainder]
        result += ' '

    return print(result)


print_hex("Hello")  # This should print "48 65 6C 6C 6F"

