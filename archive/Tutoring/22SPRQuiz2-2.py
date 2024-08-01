def filter_valid(lst, error_symbol):
    result = ""
    for word in lst:
        if len(word) >= 4 and error_symbol not in word:
            result += word
            result += " "
    return result


lst = ["ACC", "BBDXA", "EFGGH", "ABCDEFGHI"]
error_symbol = 'X'
print(filter_valid(lst, error_symbol))