def solution(s):
    ans = ['Z']  # 절대로 지워지지 않는 문자
    for i in range(len(s)):
        if s[i] == ans[-1]:
            ans.pop()
        else:
            ans += s[i]
    if 1 < len(ans):
        return 0
    else:
        return 1

print(solution("cdcd"))