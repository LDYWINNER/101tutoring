import sys
input = sys.stdin.readline

T = int(input())


def binary_sum(num1, num2):
    length = max(len(str(num1)), len(str(num2)))
    f_num = str(num1)
    s_num = str(num2)
    j = 1
    res = ""
    for i in range(0, length):
        if j > min(len(str(num1)), len(str(num2))):
            if len(str(num1)) > len(str(num2)):
                res = f_num[-j] + res
                break
            else:
                res = s_num[-j] + res
                break
        temp1 = f_num[-j]
        temp2 = s_num[-j]
        if (temp1 == "1" and temp2 == "1") or (temp1 == "0" and temp2 == "0"):
            res = "0" + res
        else:
            res = "1" + res
        j += 1

    return res


for t in range(0, T):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    tempLength = len(nums)
    a = 0
    b = 1
    while True:
        if b >= tempLength:
            a += 1
            b = a + 1
        if a >= tempLength - 1:
            break
        n1, n2 = nums[a], nums[b]
        bin1 = int(str(bin(n1))[2:])
        bin2 = int(str(bin(n2))[2:])
        sumNum = binary_sum(bin1, bin2)
        if int(sumNum, 2) == x:
            count += 1
        b += 1
    print(count)
