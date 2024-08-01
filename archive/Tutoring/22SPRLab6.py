# Name:
# SBUID:

def to_int(s):
    temp = s

    for letter in s:
        boolean = False
        for k in range(9):
            if str(k) == letter:
                boolean = True
                break
        if not boolean:
            return None

    if len(temp) == 1:
        for j in range(9):
            if str(j) == temp:
                temp = j
        return temp
    else:
        length = len(temp)
        first_letter = temp[0]
        temp = temp[1:]
        for i in range(9):
            if str(i) == first_letter:
                first_letter = i
        return first_letter * (10 ** (length - 1)) + to_int(temp)



s1 = '4321'
s2 = '234.3'   # should result in None
s3 = 'abc'   # should result in None


print(to_int(s1)) # Should print 4321
print(type(to_int(s1)))
print(to_int(s2))
print(type(to_int(s2)))
print(to_int(s3))
print(type(to_int(s3)))