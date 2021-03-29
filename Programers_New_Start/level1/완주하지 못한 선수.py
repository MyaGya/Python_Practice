from collections import defaultdict


def solution(participant, completion):
    data = defaultdict(int)
    data2 = defaultdict(int)
    for s in participant:
        data[s] += 1

    for s in completion:
        data2[s] += 1

    return data.items() - data2.items()


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
