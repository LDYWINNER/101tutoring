# CSE 101
# Lab #5
# Name: < Write your name here >
# Email: < Write your Stony Brook Email here >

# Part 1
def sequence(n):
    result = alphabet(n) + ''
    while n > 1:
        if n % 2 == 1:
            n = n * 3 + 1
            result += alphabet(n)
        elif n % 2 == 0:
            n = n // 2
            result += alphabet(n)
    return result

def alphabet(num):
    total = ''
    if num % 2 == 0:
        total += 'A'
    if num % 3 == 0:
        total += 'B'
    if num % 5 == 0:
        total += 'C'
    if num % 7 == 0:
        total += 'D'
    return total


# Part 2
def session_simulator(clients, regular):
    total = regular
    result = 0
    for client in clients:
        if client <= total:
            total -= client
            result += client
        else:
            if total == 0:
                result += (client // 2)
            else:
                result += (total + ((client - total) // 2))
    return result


# Part 3
def cafe_day(orders):
    total = 0
    for drinks in orders:
        total += drink(drinks)
    return total

def drink(drinks):
    revenue = 0
    revenue += drinks[1] * 3.5
    revenue += drinks[2] * 2.5
    revenue += drinks[3] * 1.25

    if drinks[0] == 'P':
        if drinks[1] >= 3 or drinks[2] >= 4:
            if drinks[3] >= 3:
                revenue -= (1.25 * 3)

    elif drinks[0] == 'G':
        if (drinks[1] + drinks[2] + drinks[3]) >= 10:
            revenue = revenue * 0.8

    elif drinks[0] == 'S':
        revenue = revenue * 0.98

    if len(drinks) != 4 or drinks[0] not in ['P', 'G', 'S'] or drinks[1] < 0 or drinks [2] < 0 or drinks[3] < 0:
        return 0

    return revenue


# Part 4
def premium_airlines(membership, price, points):
    if membership not in ['Diamond', 'Platinum', 'Regular'] or price < 0 or points < 0:
        print('Invalid input')
        return

    if (membership == 'Diamond' or membership == 'Platinum') and price >= 5000:
        points += 35
    elif membership == 'Diamond' and price >= 2000 and points > 300:
        points += 30
    elif membership == 'Platinum' and price >= 2000:
        points += 20
    elif membership == 'Diamond' and price >= 500 and points >= 100:
        points += 10
    elif membership == 'Regular' and price >= 5000:
        points += 5
    elif membership == 'Diamond' and points >= 25:
        points += 2
    else:
        points += 0
    return points


# Part 5
def unfair_hiring_system(applications, mood):
    hired = []
    initialMood = mood
    i = 0
    for application in applications:
        if application == 'Strong':
            hired.append(i)
            mood += 2
            mood -= 1
        elif application == 'Fair' and mood >= (initialMood / 2):
            hired.append(i)
            mood += 1
            mood -= 1
        elif application == 'Fair' and mood < (initialMood / 2):
            mood -= 2
            mood -= 1
        elif application == 'Poor' and mood >= (initialMood * 0.75):
            hired.append(i)
            mood -= 1
            mood -= 1
        elif application == 'Poor' and mood < (initialMood * 0.75):
            mood -= 5
            mood -= 1
        elif application == 'Disaster':
            mood -= 10
            mood -= 1
        else:
            mood -= 1
        i += 1
        
    if mood <= 0:
        return hired

    return hired


def main():
    # Part 1
    print("Testing Part 1")
    print("sequence(4): " + str(sequence(4)))
    print("sequence(12): " + str(sequence(12)))
    print("sequence(24): " + str(sequence(24)))
    print()

    # Part 2
    print("Testing Part 2")
    print("session_simulator([5, 5], 10): " + str(session_simulator([5, 5], 10)))
    print("session_simulator([1, 5, 4, 11], 10): " + str(
        session_simulator([1, 5, 4, 11], 10)))
    print("session_simulator([5, 7, 5, 6], 20): " + str(
        session_simulator([5, 7, 5, 6], 20)))
    print()

    # Part 3
    orders1 = [['P', 5, 0, 4]]
    orders2 = [['S', 1, 2, 3], ['P', 5, 0, 4], ['G', 4, 4, 2]]
    orders3 = [['G', 4, 3, 2], ['S', 0, 0, 10], ['P', 1, 4, 3]]
    print("Testing Part 3")
    print("cafe_day(orders1): " + str(cafe_day(orders1)))
    print("cafe_day(orders2): " + str(cafe_day(orders2)))
    print("cafe_day(orders3): " + str(cafe_day(orders3)))
    print()

    # Part 4
    print("Testing Part 4")
    print("premium_airlines('Diamond', 4999, 700): " + str(premium_airlines('Diamond', 4999, 700)))
    print("premium_airlines('Regular', 5000, 300): " + str(premium_airlines('Regular', 5000, 300)))
    print("premium_airlines('Platinum', 500, 1000): " + str(premium_airlines('Platinum', 500, 1000)))
    print()

    # Part 5
    application1 = ['Strong', 'Fair', 'Disaster']
    application2 = []
    application3 = ['Disaster', 'Poor', 'Disaster', 'Disaster', 'Disaster', 'Poor', 'Disaster', 'Poor']
    print("Testing Part 5")
    print("unfair_hiring_system(application1, 100): ", str(unfair_hiring_system(application1, 100)))
    print("unfair_hiring_system(application2, 50): ", str(unfair_hiring_system(application2, 50)))
    print("unfair_hiring_system(application3, 200): ", str(unfair_hiring_system(application3, 200)))


if __name__ == '__main__':
    main()