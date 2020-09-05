from itertools import combinations


def make_prime_number(MAX):
    data = [True for i in range(MAX + 1)]
    data[1] = False  # 1은 소수가 아니다
    for i in range(2, MAX // 2):
        if data:
            for j in range(i + i, MAX + 1, i):
                data[j] = False
    return data


def solution(nums):
    prime_number = make_prime_number(3000)
    check_number = combinations(nums, 3)
    ans = 0
    for L in check_number:
        if prime_number[sum(L)]:
            ans += 1
    return ans
