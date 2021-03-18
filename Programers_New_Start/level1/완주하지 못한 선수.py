from collections import defaultdict


def solution(participant, completion):
    data = defaultdict(int)

    for s in participant:
        data[s] += 1

    for s in completion:
        data[s] -= 1
        if data[s] == 0:
            del (data[s])
    return list(data.keys())[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
