
# < Your name >
# < Your SBU email >

alice = {
  "first": "Alice Lee",
  "scores": [15, 1, 2, 12, 0, 20, 4, 16, 1]
}
bob = {
  "first": "Byeon Kim",
  "scores": [12, 4, 0, 4, 11, 4]
}

def calculateStatistics(dict):
    name = ''
    name += dict['first']

    total = 0
    for score in dict['scores']:
        total += int(score)
    result1 = total / len(dict['scores'])

    moreTen = lessTen = 0
    for score in dict['scores']:
        if score > 10:
            moreTen += 1
        else:
            lessTen += 1
    result2 = (moreTen / (lessTen + moreTen))



    return name[0], result1, result2



print(calculateStatistics(alice))
print(calculateStatistics(bob))
