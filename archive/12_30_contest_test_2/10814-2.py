# using sorted function
N = int(input())

lst = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    lst.append((i, age, name))

answer = sorted(lst, key=lambda x: (x[1], x[0]), reverse=False)
for output in answer:
    print(f"{output[1]} {output[2]}")