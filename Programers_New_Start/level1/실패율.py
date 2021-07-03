from collections import defaultdict


def solution(N, stages):
    running_stage = defaultdict(int)

    for stage in stages:
        running_stage[stage] += 1

    clear_user = len(stages)
    non_clear_user = 0
    fail_rate = {}
    for i in range(1, N + 1):
        if clear_user == 0:
            fail_rate[i] = 0
            continue

        if i in running_stage:
            non_clear_user = running_stage[i]
            fail_rate[i] = non_clear_user / clear_user
            clear_user -= running_stage[i]

        else:
            fail_rate[i] = 0 / clear_user
    ans = list(fail_rate.items())
    ans.sort(key=lambda x: (-x[1], x[0]))
    return list(map(lambda x: x[0], ans))


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]	))
