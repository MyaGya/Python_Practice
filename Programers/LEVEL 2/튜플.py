'''
def solution(s):
    data = []
    tmp = []
    tmp = ("".join((s[:-2].split("{")))).split("},")
    for line in tmp:
        data.append(line.split(","))

    data = sorted(data, key=lambda x: len(x))
    # 차집합 출력
    result = []
    result.append(data[0])
    for i in range(len(data) - 1):
        tmp1 = set(data[i])
        tmp2 = set(data[i + 1])
        result.append(list(tmp2 - tmp1))
    result = [int(s[0]) for s in result]
    return result
'''




from collections import defaultdict


def solution(s):
    data = defaultdict(int)
    s = s[2:-2].split('},{')

    for string in s:
        string = string.split(',')
        for c in string:
            data[c] += 1

    ans = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return [int(L[0]) for L in ans]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))