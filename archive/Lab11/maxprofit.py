# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def Solution(A):
    formerValue = A[0]
    max = 0
    for i in A[1:]:
        profit = i - formerValue
        if profit > 0:
            if profit >= max:
                max = profit
        else:
            formerValue = i

    return print(max)

Solution([23171, 21011, 21123, 21366, 21013, 21367])
#Result == 356