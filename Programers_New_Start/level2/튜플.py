from collections import defaultdict


def solution(s):
    data = defaultdict(int)

    for level in s[2:-2].split("},{"):
        for value in level.split(","):
            data[int(value)] += 1

    return [number for number, repeat in sorted(data.items(), key=lambda x: x[1], reverse=True)]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
