
def largestGap(n):
    primes = []
    gaps = []
    for i in range(2, n + 1):
        if isPrime(i) == True:
            primes.append(i)

    for x in range(0, len(primes) - 1):
        gaps.append(primes[x+1] - primes[x])
    return biggest(gaps)

def biggest(nums):
    big = nums[0]
    for num in nums:
        if num > big:
            big = num
    return big

def isPrime(num):
    for x in range(2, round(num / 2)):
        if num % x == 0:
            return False
    return True


print(largestGap(12))
print(largestGap(100))
print(largestGap(1000))
print(largestGap(10000))