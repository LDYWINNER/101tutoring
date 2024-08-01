# CSE 101
# Name: DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

# Part 1
wolfie = {'I':1, 'IF': 3, 'F':4, 'IE':7, 'E':8, 'ET':24, 'T':32, 'ES': 56, 'S':64}
Re_wolfie = {1:'I', 3:'IF', 4:'F', 7:'IE', 8:'E', 24:'ET', 32:'T', 56:'ES', 64:'S'}
number = list(wolfie.values())
number.reverse()
letter = list(wolfie.keys())

def arabic2wolfie(num):
    temp = []
    answer = ''
    while num > 0:
        for numb in number:
            while numb <= num:
                temp.append(numb)
                num = num - int(temp[-1])
                answer += Re_wolfie[temp[-1]]
    return answer

# Part 2
def wolfie2arabics(numerals):
    total = 0
    for i in numerals:
        if i in letter:
            total += wolfie[i]
    return total

def wolfie2arabic(numerals):
    total = 0
    while len(numerals) > 0:
        if numerals[0:2] in letter:
            total += wolfie[numerals[0:2]]
            numerals = numerals[2:]
        elif numerals[0] in letter:
            total += wolfie[numerals[0]]
            numerals = numerals[1:]
    return total

def main():

    # Part 1
    print("Testing Part 1")
    print('Testing arabic2wolfie() with num = 10: ' + str(arabic2wolfie(10)))
    print('Testing arabic2wolfie() with num = 14: ' + str(arabic2wolfie(14)))
    print('Testing arabic2wolfie() with num = 22: ' + str(arabic2wolfie(22)))
    print('Testing arabic2wolfie() with num = 28: ' + str(arabic2wolfie(28)))
    print('Testing arabic2wolfie() with num = 30: ' + str(arabic2wolfie(30)))
    print('Testing arabic2wolfie() with num = 54: ' + str(arabic2wolfie(54)))
    print()

    # Part 2
    print("Testing Part 2")
    print("Testing wolfie2arabic() with wolfie = 'EII': " + str(wolfie2arabic('EII')))
    print("Testing wolfie2arabic() with wolfie = 'EFII': " + str(wolfie2arabic('EFII')))
    print("Testing wolfie2arabic() with wolfie = 'EEFII': " + str(wolfie2arabic('EEFII')))
    print("Testing wolfie2arabic() with wolfie = 'ETF': " + str(wolfie2arabic('ETF')))
    print("Testing wolfie2arabic() with wolfie = 'ETFII': " + str(wolfie2arabic('ETFII')))
    print("Testing wolfie2arabic() with wolfie = 'TEEFII': " + str(wolfie2arabic('TEEFII')))
    print()


if __name__ == '__main__':
    main()