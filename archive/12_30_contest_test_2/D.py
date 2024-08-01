import sys
input = sys.stdin.readline

T = int(input())

for t in range(0, T):
    a, b, c = map(int, input().split())
    temp = 0
    store = 0
    temp2 = a
    while store < c:
        temp += 1
        temp2 += b
        store += len(str(temp2))
    temp -= 1
    temp2 -= b
    print(store, temp, temp2)
    print(str(temp2)[store - c])
