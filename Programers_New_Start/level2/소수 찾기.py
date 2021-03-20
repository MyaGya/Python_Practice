from itertools import permutations
from math import sqrt

def solution(numbers):
    ans = 0
    primes_max = 10000000
    primes = [True for _ in range(10000000)]
    primes[0] = False
    primes[1] = False
    # make primes
    for i in range(2, int(sqrt(primes_max)) + 1):
        if primes[i]:
            for j in range(2 * i, primes_max, i):
                primes[j] = False

    # run permutations
    for i in range(1, len(numbers) + 1):
        data = list(permutations(numbers, i))
        for L in data:
            if primes[int("".join(L))]:
                ans += 1
                primes[int("".join(L))] = False  # use prime
    return ans


print(solution("011"))
