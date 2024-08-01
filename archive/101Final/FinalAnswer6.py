# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def modifyString(string):
    count = {}
    final = ''
    for letter in string:
        count.setdefault(letter, 0)
        count[letter] += 1
        final += letter * int(count[letter])
    #print(count)
    print(final)

# Test
modifyString("ohoh")
modifyString("repetitive")
