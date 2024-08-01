# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

alice = {
  "first": "Alice",
  "last": "Lee",
  "result": [0, 1, 2, 1, 0, 2, 4, 0, 1]
}
bob = {
  "first": "Bob",
  "last": "Kim",
  "result": [0, 4, 0, 4, 0, 4]
}

def get_statistics(dict):
    full_name = str(dict['first']) +' ' + str(dict['last'])

    gradeList = dict['result']
    total = 0
    for k in range(len(gradeList)):
        num = len(gradeList)
        total += gradeList[k]
        final = total / num
        if final > 0:
            finalResult = round(final, 2)

    greaterthanZero = 0
    for k in range(len(gradeList)):
        if gradeList[k] > 0:
            greaterthanZero += 1
        percentBigThanZero = 0
        percentBigThanZero = greaterthanZero / (len(gradeList))
        percentage = 0
        if percentBigThanZero > 0:
            percentage = round(percentBigThanZero, 2)

    return full_name, finalResult, percentage

print(get_statistics(bob))
print(get_statistics(alice))
