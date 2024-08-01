# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

def sum_all_digits(n):
    if (n // 10) == 0:
        return n
    if (n // 10) >= 1:
        k = n % 10
        n = n // 10
        return k + sum_all_digits(n)

print(sum_all_digits(157))

print(sum_all_digits(6))

print(sum_all_digits(4222))