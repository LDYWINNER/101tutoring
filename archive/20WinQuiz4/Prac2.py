
def isLucky(n):
    if (n % 10 == 0 or n % 10 == 6) and n // 10 == 0:
        return True
    elif n % 10 == 6 or n % 10 == 0:
        return isLucky(n // 10)
    else:
        return False

print(isLucky(12))
print(isLucky(666))
print(isLucky(606))
print(isLucky(2066))


