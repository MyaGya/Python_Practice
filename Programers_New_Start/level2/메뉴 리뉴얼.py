from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    num_repeat = defaultdict(int)
    for order in orders:
        order = sorted(list(order))

        # find all combination case
        for num_course in course:
            for combinations_value in combinations(order, num_course):
                num_repeat[combinations_value] += 1
    result = num_repeat.items()

    # find the maximum iteration value
    answer = []
    for num_course in course:
        match_result = list(filter(lambda x: len(x[0]) == num_course, result))
        if not match_result:
            continue
        repeat_max = max(list(zip(*match_result))[1])
        if repeat_max == 1:
            continue
        for combination_case, repeat in match_result:
            if repeat == repeat_max:
                answer.append(combination_case)

    return sorted(list(map("".join, answer)))


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
