# 실패
def solution(s):
    # 최솟값
    Min = len(s)
    # 1. 문자열 반복 기준
    for loop in range(1,len(s)//2+1):
        prev = s[0:0+loop]
        cnt = 0
        total = 0
        # 2. 반복
        for i in range(0,len(s),loop):
            # 이전값과 같은 경우
            if prev == s[i:i+loop]:
                cnt += 1
            # 이전값과 다른 경우
            else:
                if 1 < cnt:
                    total += 1
                prev = s[i:i + loop]
                cnt = 1
                total += loop
        # 종료시 한번 더 연산
        if 1 < cnt:
            total += 1 + len(s[i:i+loop])
        else:
            total += len(s[i:i+loop])
        Min = min(Min, total)
    return Min
print(solution(""))