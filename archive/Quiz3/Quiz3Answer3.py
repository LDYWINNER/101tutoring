# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

def processString(string):
    # Implement this function
    for k in range(len(string)):
        if string[k] == '.':
            res = []
            res.append(string[:k])
            res.append(string[k + 2:])

    for i in range(len(res)):
        word_length = []
        word_length.append(len(res[i]))
        for j in word_length:
            word_num = res[i].count(' ')
            final = j / (word_num + 1)
        print("{:.1f}".format(final))

# This should print 4.5 3.0
processString("An example. Two")

# This should print 4.4 5.3 4.5
processString("This is the first sentence. The second sentence starts after the period. Then a final sentence")
