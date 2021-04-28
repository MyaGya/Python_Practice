from collections import Counter


def solution(n):
    binary_n = bin(n)[2:]

    find_first_one = False
    for i in range(len(binary_n) - 1, -1, -1):
        if not find_first_one and binary_n[i] == '1':
            find_first_one = True
        if find_first_one and binary_n[i] == '0':
            break
    else:
        num_one = Counter(binary_n[i + 1:])["1"]
        num_zero = len(binary_n[i + 1:]) - num_one + 1
        return int("1" + "0" * num_zero + "1" * num_one, 2)

    num_one = Counter(binary_n[i + 1:])["1"] - 1
    num_zero = len(binary_n[i + 1:]) - num_one

    return int(binary_n[:i] + "1" + "0" * num_zero + "1" * num_one, 2)


print(solution(6))
