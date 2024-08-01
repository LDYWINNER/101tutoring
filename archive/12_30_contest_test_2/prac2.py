import sys
input = sys.stdin.readline

T = int(input())

for t in range(0, T):
    a, b, c = map(int, input().split())
    sl = 0
    temp1 = 10
    length = 1
    temp4 = 0
    while sl < c:
        if temp4 == 0:
            temp2 = temp1 // b
            temp4 += 1
        else:
            temp3 = temp2
            temp2 = temp1 // b - temp3
        sl += length * temp2
        temp1 *= 10
        length += 1
        print(sl, temp2)


