from itertools import permutations


def solution(numbers):
    ans = 0
    primes_max = 10000000
    primes = [True for _ in range(10000000)]
    primes[0] = False
    primes[1] = False

    for i in range(2, primes_max // 2 + 1):
        if primes[i]:
            for j in range(2 * i, primes_max, i):
                primes[j] = False

    for i in range(1, len(numbers) + 1):
        data = list(permutations(numbers, i))
        for L in data:
            if primes[int("".join(L))]:
                ans += 1
                primes[int("".join(L))] = False  # use prime
    return ans


print(solution("011"))
