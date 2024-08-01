

def reverse_words(string):
    final = []
    temp = string.split()
    print(temp)
    for word in temp:
        temp_string = ""
        for i in range(1, len(word) + 1):
            #print(i)
            temp_string += word[-i]
            #print(temp_string)
        final.append(temp_string)
    return final

ex1 = "What is your name"
ex2 = "553! 9921X &@*"
ex3 = "l n v u"
print(reverse_words(ex1))
print(reverse_words(ex2))
print(reverse_words(ex3))