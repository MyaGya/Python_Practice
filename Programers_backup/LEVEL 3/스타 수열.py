from collections import Counter


def solution(a):
    answer = 0
    elements = Counter(a)

    for key in elements.keys():
        if elements[key] * 2 <= answer:
            continue

        common_count = 0
        idx = 0
        while idx < len(a) - 1:
            if a[idx] != key and a[idx + 1] != key or (a[idx] == a[idx + 1]):  # fail case
                idx += 1
                continue

            # success case
            common_count += 2
            idx += 2
        answer = max(common_count, answer)
    return answer


print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
