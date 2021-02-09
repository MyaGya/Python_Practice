import math


def solution(s):
    ret = math.inf
    refer = ""

    for i in range(1, len(s) // 2 + 2):
        tmp = ""
        refer = s[0:i]
        cnt = 0
        for j in range(0, len(s), i):
            if refer == s[j:j + i]:
                cnt += 1
            else:
                if cnt - 1:  # 1 번 이상 반복될 경우
                    tmp += str(cnt)
                tmp += refer
                refer = s[j:j+i]
                cnt = 1
        if cnt == 1:
            tmp += refer
        else:
            tmp += str(cnt) + refer
        ret = min(ret,len(tmp))
    return ret


print(solution("aabbaccc"))