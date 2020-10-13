import random


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(6):
    num = random.randint(1, 101)
    if is_prime(num):
        print("The random number {} is a prime number".format(num))
    else:
        print("The random number {} is not a prime number".format(num))