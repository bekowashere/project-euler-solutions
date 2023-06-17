# Solution to Project Euler problem 3
# https://github.com/bekowashere/project-euler-solutions

"""
Problem:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math


def smallest_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    # n itself is prime
    return n


def compute():
    n = 600851475143
    while True:
        p = smallest_prime(n)
        if p < n:
            n = n // p
        else:
            return str(n)


print(compute())
