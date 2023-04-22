import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_prime(min=2, max=200):
    while True:
        num = random.randint(min, max)
        if is_prime(num):
            return num

def generate_private_key():
    max = 10 ** 5
    return random.randint(2, max)
