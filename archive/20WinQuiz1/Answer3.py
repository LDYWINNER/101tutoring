def decision(gpa, interview, test, yearsWorked):
    points = 0                    # Point total accumulator

    if gpa >= 3.8:
        points += 3
    elif gpa >= 3.5:
        points += 2
    elif gpa >= 3:
        points += 1

    if interview >= 9:
        points += 3
    elif interview == 8:
        points += 2
    elif interview == 7:
        points += 1              # note: no else clause

    if test >= 95:
        points = points + 3
    elif test >= 85:
        points += 2
    elif test >= 75:
        points += 1

    if yearsWorked < 1:
        points += 0
    elif 1 <= yearsWorked <= 2:
        points += 1
    elif yearsWorked > 2:
        points += 2

    if points <= 5:
        return 'Not hired'
    elif 6 <= points <= 8:
        return 'Junior Salesperson'
    elif points >= 9:
        return 'Manager-in-Training'

print(decision(4.0, 10, 100, 0))
print(decision(3.0, 6, 70, 1))
print(decision(3.5, 9, 90, 2))
