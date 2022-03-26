from math import sqrt


def isPrime(number):
    k = int(sqrt(number + 1))
    for i in range(2, k + 1):
        if number % i == 0:
            return False
    return True


for i in range(100, 200):
    if isPrime(i):
        print(i)
