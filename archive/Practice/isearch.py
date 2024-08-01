def isearch(a, x):
    i = 0
    while i < len(a):
        print('looking in location', i)
        if a[i] == x:
            return i
        i += 1
    return None

alkali = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']

print(isearch(alkali, 'K'))