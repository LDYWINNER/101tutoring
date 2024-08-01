
def days_for_target(initial_weight, target_weight):
    day = 0
    currentWeight = initial_weight
    while currentWeight > target_weight:
        if day % 7 not in [5, 6]:
            currentWeight -= 10
            day += 1
        else:
            currentWeight += 8
            day += 1
    print(day)

days_for_target(3040, 3000)
days_for_target(3040, 2980)
days_for_target(3500, 2950)
days_for_target(2940, 2938)
days_for_target(2107, 1969)
days_for_target(2178, 1784)
days_for_target(2834, 2697)
days_for_target(2220, 1790)
days_for_target(3845, 3397)
days_for_target(2078, 1883)