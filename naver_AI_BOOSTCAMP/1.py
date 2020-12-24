from collections import Counter
def solution(s):
    ans = 0
    for i in Counter(s).values():
        if i %2 == 1:
            ans += 1
    return ans

print(solution("a"))
