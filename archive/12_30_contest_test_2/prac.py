import sys

input = sys.stdin.readline

T = int(input())

for t in range(0, T):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    coms = []
    tempLength = len(nums)
    a = 0
    b = 1
    while True:
        if b >= tempLength:
            a += 1
            b = a + 1
        if a >= tempLength - 1:
            break
        coms.append([nums[a], nums[b]])
        b += 1


    for com in coms:
        n1, n2 = com
        bin1 = int(str(bin(n1))[2:])
        bin2 = int(str(bin(n2))[2:])

        length = max(len(str(bin1)), len(str(bin2)))
        f_num = str(bin1)
        s_num = str(bin2)
        j = 1
        res = ""
        for i in range(0, length):
            if j > min(len(str(bin1)), len(str(bin2))):
                if len(str(bin1)) > len(str(bin2)):
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

        if int(res, 2) == x:
            count += 1
    print(count)
