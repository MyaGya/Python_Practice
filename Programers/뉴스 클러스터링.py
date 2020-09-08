from collections import defaultdict


def solution(str1, str2):
    history1 = defaultdict(int)
    history2 = defaultdict(int)
    # make alpha
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            history1[str1[i:i + 2].lower()] += 1
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            history2[str2[i:i + 2].lower()] += 1
    union = 0
    intersection = 0

    # make intersection
    for L in history1.items():
        intersection += min(L[1], history2[L[0]])
    # make union
    for L in history2.items():
        history1[L[0]] = max(history1[L[0]],L[1])
    for i in history1.values():
        union += i

    return int(intersection / union * 65536) if union != 0 else 65536
print(solution('aa1+aa2	',"AAAA12"))
