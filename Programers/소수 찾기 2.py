def solution(n):
    prime_number = [0 for _ in range(n + 1)]
    for i in range(2, n//2 + 2):
        for j in range(i+i, n + 1, i):
            prime_number[j] = 1

    return prime_number.count(0) - 2

print(solution(10))