def filter_valid(lst, error_symbol):
    result = '"'
    bool = False
    for word in lst:
        if len(word) < 4:
            bool = True
        else:
            for letter in word:
                if letter == error_symbol:
                    bool = True
        if bool == False:
            result += word
            result += " "
        bool = False
    return result + '"'


lst = ["ACC", "BBDXA", "EFGGH", "ABCDEFGHI"]
error_symbol = 'X'
print(filter_valid(lst, error_symbol))